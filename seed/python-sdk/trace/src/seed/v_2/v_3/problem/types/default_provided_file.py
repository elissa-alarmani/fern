# This file was auto-generated by Fern from our API Definition.

from .....core.pydantic_utilities import UniversalBaseModel
from .file_info_v_2 import FileInfoV2
import typing_extensions
import typing
from .....commons.types.variable_type import VariableType
from .....core.serialization import FieldMetadata
from .....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .....core.pydantic_utilities import update_forward_refs
from .....commons.types.list_type import ListType
from .....commons.types.map_type import MapType


class DefaultProvidedFile(UniversalBaseModel):
    file: FileInfoV2
    related_types: typing_extensions.Annotated[typing.List[VariableType], FieldMetadata(alias="relatedTypes")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ListType)
update_forward_refs(MapType)
