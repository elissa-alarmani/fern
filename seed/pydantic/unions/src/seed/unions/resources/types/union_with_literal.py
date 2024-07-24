# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Base(UniversalBaseModel):
    base: typing.Literal["base"] = "base"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            extra = pydantic.Extra.allow


class UnionWithLiteral_Fern(Base):
    value: typing.Literal["fern"]
    type: typing.Literal["fern"] = "fern"


UnionWithLiteral = UnionWithLiteral_Fern
