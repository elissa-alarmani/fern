# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from .test_case_with_actual_result_implementation import (
    TestCaseWithActualResultImplementation,
)
from ......core.pydantic_utilities import IS_PYDANTIC_V2
from .void_function_definition import VoidFunctionDefinition
from ......core.pydantic_utilities import UniversalRootModel
import typing
import typing_extensions
import pydantic
from ......core.pydantic_utilities import update_forward_refs
from .....commons.types.list_type import ListType
from .....commons.types.map_type import MapType

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def with_actual_result(
        self, value: TestCaseWithActualResultImplementation
    ) -> TestCaseFunction:
        if IS_PYDANTIC_V2:
            return TestCaseFunction(
                root=_TestCaseFunction.WithActualResult(
                    **value.dict(exclude_unset=True), type="withActualResult"
                )
            )  # type: ignore
        else:
            return TestCaseFunction(
                __root__=_TestCaseFunction.WithActualResult(
                    **value.dict(exclude_unset=True), type="withActualResult"
                )
            )  # type: ignore

    def custom(self, value: VoidFunctionDefinition) -> TestCaseFunction:
        if IS_PYDANTIC_V2:
            return TestCaseFunction(
                root=_TestCaseFunction.Custom(
                    **value.dict(exclude_unset=True), type="custom"
                )
            )  # type: ignore
        else:
            return TestCaseFunction(
                __root__=_TestCaseFunction.Custom(
                    **value.dict(exclude_unset=True), type="custom"
                )
            )  # type: ignore


class TestCaseFunction(UniversalRootModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[
            typing.Union[_TestCaseFunction.WithActualResult, _TestCaseFunction.Custom],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(
            self,
        ) -> typing.Union[_TestCaseFunction.WithActualResult, _TestCaseFunction.Custom]:
            return self.root
    else:
        __root__: typing_extensions.Annotated[
            typing.Union[_TestCaseFunction.WithActualResult, _TestCaseFunction.Custom],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(
            self,
        ) -> typing.Union[_TestCaseFunction.WithActualResult, _TestCaseFunction.Custom]:
            return self.__root__

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        if IS_PYDANTIC_V2:
            return self.root.dict(**kwargs)
        else:
            return self.__root__.dict(**kwargs)

    def visit(
        self,
        with_actual_result: typing.Callable[
            [TestCaseWithActualResultImplementation], T_Result
        ],
        custom: typing.Callable[[VoidFunctionDefinition], T_Result],
    ) -> T_Result:
        unioned_value = self.get_as_union()
        if unioned_value.type == "withActualResult":
            return with_actual_result(
                TestCaseWithActualResultImplementation(
                    **unioned_value.dict(exclude_unset=True, exclude={"type"})
                )
            )
        if unioned_value.type == "custom":
            return custom(
                VoidFunctionDefinition(
                    **unioned_value.dict(exclude_unset=True, exclude={"type"})
                )
            )


class _TestCaseFunction:
    class WithActualResult(TestCaseWithActualResultImplementation):
        type: typing.Literal["withActualResult"] = "withActualResult"

    class Custom(VoidFunctionDefinition):
        type: typing.Literal["custom"] = "custom"


update_forward_refs(TestCaseFunction)
update_forward_refs(ListType)
update_forward_refs(MapType)
