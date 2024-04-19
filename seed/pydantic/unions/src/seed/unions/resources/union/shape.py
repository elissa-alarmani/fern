# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .circle import Circle
from .square import Square


class Base(pydantic_v1.BaseModel):
    id: str

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


class Shape_Circle(Circle, Base):
    type: typing.Literal["circle"] = "circle"

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class Shape_Square(Square, Base):
    type: typing.Literal["square"] = "square"

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


Shape = typing.Union[Shape_Circle, Shape_Square]
