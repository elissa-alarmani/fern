# This file was auto-generated by Fern from our API Definition.

from .....core.pydantic_utilities import UniversalBaseModel
from .parameter_id import ParameterId
import pydantic
from ....commons.variable_type import VariableType
from .....core.pydantic_utilities import IS_PYDANTIC_V2
import typing
from .....core.pydantic_utilities import update_forward_refs
from ....commons.list_type import ListType
from ....commons.map_type import MapType


class Parameter(UniversalBaseModel):
    parameter_id: ParameterId = pydantic.Field(alias="parameterId")
    name: str
    variable_type: VariableType = pydantic.Field(alias="variableType")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            extra = pydantic.Extra.allow


update_forward_refs(ListType)
update_forward_refs(MapType)
