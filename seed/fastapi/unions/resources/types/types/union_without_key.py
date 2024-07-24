# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalRootModel, update_forward_refs
from .bar import Bar as resources_types_types_bar_Bar
from .foo import Foo as resources_types_types_foo_Foo

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def foo(self, value: resources_types_types_foo_Foo) -> UnionWithoutKey:
        if IS_PYDANTIC_V2:
            return UnionWithoutKey(root=_UnionWithoutKey.Foo(**value.dict(exclude_unset=True), type="foo"))
        else:
            return UnionWithoutKey(__root__=_UnionWithoutKey.Foo(**value.dict(exclude_unset=True), type="foo"))

    def bar(self, value: resources_types_types_bar_Bar) -> UnionWithoutKey:
        if IS_PYDANTIC_V2:
            return UnionWithoutKey(root=_UnionWithoutKey.Bar(**value.dict(exclude_unset=True), type="bar"))
        else:
            return UnionWithoutKey(__root__=_UnionWithoutKey.Bar(**value.dict(exclude_unset=True), type="bar"))


class UnionWithoutKey(UniversalRootModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[
            typing.Union[_UnionWithoutKey.Foo, _UnionWithoutKey.Bar], pydantic.Field(discriminator="type")
        ]

        def get_as_union(self) -> typing.Union[_UnionWithoutKey.Foo, _UnionWithoutKey.Bar]:
            return self.root

    else:
        __root__: typing_extensions.Annotated[
            typing.Union[_UnionWithoutKey.Foo, _UnionWithoutKey.Bar], pydantic.Field(discriminator="type")
        ]

        def get_as_union(self) -> typing.Union[_UnionWithoutKey.Foo, _UnionWithoutKey.Bar]:
            return self.__root__

    def visit(
        self,
        foo: typing.Callable[[resources_types_types_foo_Foo], T_Result],
        bar: typing.Callable[[resources_types_types_bar_Bar], T_Result],
    ) -> T_Result:
        unioned_value = self.get_as_union()
        if unioned_value.type == "foo":
            return foo(resources_types_types_foo_Foo(**unioned_value.dict(exclude_unset=True, exclude={"type"})))
        if unioned_value.type == "bar":
            return bar(resources_types_types_bar_Bar(**unioned_value.dict(exclude_unset=True, exclude={"type"})))


class _UnionWithoutKey:
    class Foo(resources_types_types_foo_Foo):
        type: typing.Literal["foo"] = "foo"

    class Bar(resources_types_types_bar_Bar):
        type: typing.Literal["bar"] = "bar"


update_forward_refs(UnionWithoutKey)
