# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, UniversalRootModel

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def integer(self, value: int) -> UnionWithPrimitive:
        return UnionWithPrimitive(_UnionWithPrimitive.Integer(type="integer", value=value))

    def string(self, value: str) -> UnionWithPrimitive:
        return UnionWithPrimitive(_UnionWithPrimitive.String(type="string", value=value))


class UnionWithPrimitive(UniversalRootModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[
            typing.Union[_UnionWithPrimitive.Integer, _UnionWithPrimitive.String], pydantic.Field(discriminator="type")
        ]

        def get_as_union(self) -> typing.Union[_UnionWithPrimitive.Integer, _UnionWithPrimitive.String]:
            return self.root

    else:
        __root__: typing_extensions.Annotated[
            typing.Union[_UnionWithPrimitive.Integer, _UnionWithPrimitive.String], pydantic.Field(discriminator="type")
        ]

        def get_as_union(self) -> typing.Union[_UnionWithPrimitive.Integer, _UnionWithPrimitive.String]:
            return self.__root__

    def visit(self, integer: typing.Callable[[int], T_Result], string: typing.Callable[[str], T_Result]) -> T_Result:
        if self.get_as_union().type == "integer":
            return integer(self.get_as_union().value)
        else:
            return string(self.get_as_union().value)


class _UnionWithPrimitive:
    class Integer(UniversalBaseModel):
        type: typing.Literal["integer"] = "integer"
        value: int

        if IS_PYDANTIC_V2:
            model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)  # type: ignore # Pydantic v2
        else:

            class Config:
                frozen = True
                smart_union = True

    class String(UniversalBaseModel):
        type: typing.Literal["string"] = "string"
        value: str

        if IS_PYDANTIC_V2:
            model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)  # type: ignore # Pydantic v2
        else:

            class Config:
                frozen = True
                smart_union = True
