# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .object_with_optional_field import ObjectWithOptionalFieldParams


class NestedObjectWithRequiredFieldParams(UniversalBaseModel):
    string: str
    nested_object: ObjectWithOptionalFieldParams = pydantic.Field(alias="NestedObject")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
