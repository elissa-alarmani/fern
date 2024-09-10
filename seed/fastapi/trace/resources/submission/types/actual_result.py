# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...commons.types.variable_value import VariableValue
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from .exception_info import ExceptionInfo
from .exception_v_2 import (
    ExceptionV2 as resources_submission_types_exception_v_2_ExceptionV2,
)
from ....core.pydantic_utilities import UniversalRootModel
import typing
import typing_extensions
import pydantic
from ....core.pydantic_utilities import UniversalBaseModel
from ....core.pydantic_utilities import update_forward_refs
from ...commons.types.key_value_pair import KeyValuePair
from ...commons.types.map_value import MapValue

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def value(self, value: VariableValue) -> ActualResult:
        if IS_PYDANTIC_V2:
            return ActualResult(root=_ActualResult.Value(type="value", value=value))  # type: ignore
        else:
            return ActualResult(__root__=_ActualResult.Value(type="value", value=value))  # type: ignore

    def exception(self, value: ExceptionInfo) -> ActualResult:
        if IS_PYDANTIC_V2:
            return ActualResult(
                root=_ActualResult.Exception(
                    **value.dict(exclude_unset=True), type="exception"
                )
            )  # type: ignore
        else:
            return ActualResult(
                __root__=_ActualResult.Exception(
                    **value.dict(exclude_unset=True), type="exception"
                )
            )  # type: ignore

    def exception_v_2(
        self, value: resources_submission_types_exception_v_2_ExceptionV2
    ) -> ActualResult:
        if IS_PYDANTIC_V2:
            return ActualResult(
                root=_ActualResult.ExceptionV2(type="exceptionV2", value=value)
            )  # type: ignore
        else:
            return ActualResult(
                __root__=_ActualResult.ExceptionV2(type="exceptionV2", value=value)
            )  # type: ignore


class ActualResult(UniversalRootModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[
            typing.Union[
                _ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2
            ],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(
            self,
        ) -> typing.Union[
            _ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2
        ]:
            return self.root
    else:
        __root__: typing_extensions.Annotated[
            typing.Union[
                _ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2
            ],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(
            self,
        ) -> typing.Union[
            _ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2
        ]:
            return self.__root__

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        if IS_PYDANTIC_V2:
            return self.root.dict(**kwargs)
        else:
            return self.__root__.dict(**kwargs)

    def visit(
        self,
        value: typing.Callable[[VariableValue], T_Result],
        exception: typing.Callable[[ExceptionInfo], T_Result],
        exception_v_2: typing.Callable[
            [resources_submission_types_exception_v_2_ExceptionV2], T_Result
        ],
    ) -> T_Result:
        unioned_value = self.get_as_union()
        if unioned_value.type == "value":
            return value(unioned_value.value)
        if unioned_value.type == "exception":
            return exception(
                ExceptionInfo(
                    **unioned_value.dict(exclude_unset=True, exclude={"type"})
                )
            )
        if unioned_value.type == "exceptionV2":
            return exception_v_2(unioned_value.value)


class _ActualResult:
    class Value(UniversalBaseModel):
        type: typing.Literal["value"] = "value"
        value: VariableValue

    class Exception(ExceptionInfo):
        type: typing.Literal["exception"] = "exception"

    class ExceptionV2(UniversalBaseModel):
        type: typing.Literal["exceptionV2"] = "exceptionV2"
        value: resources_submission_types_exception_v_2_ExceptionV2


update_forward_refs(ActualResult)
update_forward_refs(KeyValuePair)
update_forward_refs(MapValue)
