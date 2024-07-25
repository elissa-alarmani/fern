from __future__ import annotations

from types import TracebackType
from typing import Dict, List, Optional, Sequence, Type

import fern.ir.resources as ir_types

from fern_python.codegen import AST, SourceFile
from fern_python.codegen.ast.references.class_reference import ClassReference
from fern_python.codegen.local_class_reference import LocalClassReference
from fern_python.external_dependencies.typing_extensions import (
    TYPING_EXTENSIONS_DEPENDENCY,
)
from fern_python.source_file_factory.source_file_factory import SourceFileFactory

from ..context import PydanticGeneratorContext

TYPING_EXTENSIONS_MODULE = AST.Module.external(
    module_path=("typing_extensions",),
    dependency=TYPING_EXTENSIONS_DEPENDENCY,
)


class FernTypedDict:
    TYPEDDICT_REFERENCE = AST.ClassReference(
        qualified_name_excluding_import=("TypedDict",),
        import_=AST.ReferenceImport(module=TYPING_EXTENSIONS_MODULE),
    )

    def __init__(
        self,
        context: PydanticGeneratorContext,
        source_file: SourceFile,
        type_name: Optional[ir_types.DeclaredTypeName] = None,
        should_export: bool = True,
        extended_types: Optional[Sequence[ir_types.DeclaredTypeName]] = None,
        extended_references: Optional[Sequence[ClassReference]] = None,
        class_name: Optional[str] = None,
        docstring: Optional[str] = None,
    ):
        self._context = context
        self._type_name = type_name

        extends_crs = list((extended_references or []))
        extends_crs.extend(
            [context.get_class_reference_for_type_id(extended.type_id) for extended in extended_types]
            if extended_types is not None
            else []
        )

        if class_name is None and type_name is None:
            raise ValueError("Either class_name or name must be provided")
        elif class_name is not None:
            self._class_name = class_name
        elif type_name is not None:
            self._class_name = self._context.get_class_name_for_type_id(type_name.type_id, as_request=True)

        self._class_declaration = AST.ClassDeclaration(
            name=self._class_name,
            extends=extends_crs or [FernTypedDict.TYPEDDICT_REFERENCE],
            docstring=AST.Docstring(docstring) if docstring is not None else None,
        )
        self._type_declaration = None
        if type_name is not None:
            self._type_declaration = context.get_declaration_for_type_id(type_name.type_id)

        self._local_class_reference = source_file.add_class_declaration(
            declaration=self._class_declaration, should_export=should_export
        )

    def to_reference(self) -> LocalClassReference:
        return self._local_class_reference

    def _field_type_is_circularly_referened(self, field_types: List[ir_types.TypeId]) -> bool:
        return (
            any(
                [
                    self._context.does_type_reference_other_type(field_type, self._type_name.type_id)
                    for field_type in field_types
                ]
            )
            if self._type_name is not None
            else False
        )

    def _get_type_hint_for_type_reference(
        self, type_reference: ir_types.TypeReference, as_if_type_checking_import: bool
    ) -> AST.TypeHint:
        return self._context.get_type_hint_for_type_reference(
            type_reference,
            as_if_type_checking_import=as_if_type_checking_import,
            in_endpoint=True,
            for_typeddict=True,
        )

    def add_field(
        self,
        *,
        name: str,
        json_field_name: str,
        type_reference: ir_types.TypeReference,
        description: Optional[str] = None,
        # Here to mirror the FernAwarePydanticModel.add_field method signature
        # which makes it easy to spread args from that method to this one.
        pascal_case_field_name: Optional[str] = None,
        default_value: Optional[AST.Expression] = None,
    ) -> None:
        maybe_type_id = self._context.maybe_get_type_ids_for_type_reference(type_reference)
        as_if_type_checking = False
        if maybe_type_id is not None and self._field_type_is_circularly_referened(maybe_type_id):
            # Mark the class reference as if_typechecking since we have a circular ref that we'll
            # need to string reference and import through `if TYPE_CHECKING`.
            as_if_type_checking = True

        type_hint = self._get_type_hint_for_type_reference(type_reference, as_if_type_checking)
        if json_field_name != name:
            field_metadata = self._context.core_utilities.get_field_metadata().get_instance()
            field_metadata.add_alias(json_field_name)

            type_hint = AST.TypeHint.annotated(
                type=type_hint,
                annotation=field_metadata.get_as_node(),
            )

        self._class_declaration.add_class_var(
            AST.VariableDeclaration(
                name=name,
                type_hint=type_hint,
                docstring=AST.Docstring(description) if description is not None else None,
            )
        )

    def to_snippet(self) -> AST.Expression:
        return AST.Expression("TODO")

    def finish(self) -> None:
        if self._type_declaration is not None and len(self._type_declaration.examples) > 0:
            snippet = SourceFileFactory.create_snippet()
            snippet.add_expression(self.to_snippet())
            self._class_declaration.add_snippet(snippet.to_str())

    def __enter__(self) -> FernTypedDict:
        return self

    def __exit__(
        self,
        exctype: Optional[Type[BaseException]],
        excinst: Optional[BaseException],
        exctb: Optional[TracebackType],
    ) -> None:
        self.finish()

    @classmethod
    def _can_be_typeddict_tr(
        cls, tr: ir_types.TypeReference, types: Dict[ir_types.TypeId, ir_types.TypeDeclaration]
    ) -> bool:
        return tr.visit(
            named=lambda nt: FernTypedDict.can_be_typeddict(types[nt.type_id].shape, types),
            container=lambda ct: ct.visit(
                list_=lambda list_tr: FernTypedDict._can_be_typeddict_tr(list_tr, types),
                map_=lambda mt: FernTypedDict._can_be_typeddict_tr(mt.key_type, types)
                or FernTypedDict._can_be_typeddict_tr(mt.value_type, types),
                optional=lambda optional_tr: FernTypedDict._can_be_typeddict_tr(optional_tr, types),
                set_=lambda set_tr: FernTypedDict._can_be_typeddict_tr(set_tr, types),
                literal=lambda _: False,
            ),
            primitive=lambda _: False,
            unknown=lambda: False,
        )

    @classmethod
    def can_be_typeddict(cls, type_: ir_types.Type, types: Dict[ir_types.TypeId, ir_types.TypeDeclaration]) -> bool:
        return type_.visit(
            alias=lambda atd: atd.resolved_type.visit(
                named=lambda nt: nt.shape.visit(
                    enum=lambda: False,
                    object=lambda: True,
                    union=lambda: True,
                    undiscriminated_union=lambda: True,
                ),
                container=lambda ct: ct.visit(
                    list_=lambda list_tr: FernTypedDict._can_be_typeddict_tr(list_tr, types),
                    map_=lambda mt: FernTypedDict._can_be_typeddict_tr(mt.key_type, types)
                    or FernTypedDict._can_be_typeddict_tr(mt.value_type, types),
                    optional=lambda optional_tr: FernTypedDict._can_be_typeddict_tr(optional_tr, types),
                    set_=lambda set_tr: FernTypedDict._can_be_typeddict_tr(set_tr, types),
                    literal=lambda _: False,
                ),
                primitive=lambda _: False,
                unknown=lambda: False,
            ),
            enum=lambda _: False,
            object=lambda _: True,
            union=lambda _: True,
            undiscriminated_union=lambda _: True,
        )
