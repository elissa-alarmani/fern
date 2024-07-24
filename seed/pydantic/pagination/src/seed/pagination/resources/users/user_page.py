# This file was auto-generated by Fern from our API Definition.

import typing
import uuid

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_list_container import UserListContainer


class UserPage(UniversalBaseModel):
    data: UserListContainer
    next: typing.Optional[uuid.UUID] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            extra = pydantic.Extra.allow
