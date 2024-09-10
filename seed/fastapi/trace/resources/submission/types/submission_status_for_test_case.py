# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from .test_case_result_with_stdout import TestCaseResultWithStdout
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from .test_case_grade import TestCaseGrade
from .traced_test_case import TracedTestCase
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
    def graded(self, value: TestCaseResultWithStdout) -> SubmissionStatusForTestCase:
        if IS_PYDANTIC_V2:
            return SubmissionStatusForTestCase(
                root=_SubmissionStatusForTestCase.Graded(
                    **value.dict(exclude_unset=True), type="graded"
                )
            )  # type: ignore
        else:
            return SubmissionStatusForTestCase(
                __root__=_SubmissionStatusForTestCase.Graded(
                    **value.dict(exclude_unset=True), type="graded"
                )
            )  # type: ignore

    def graded_v_2(self, value: TestCaseGrade) -> SubmissionStatusForTestCase:
        if IS_PYDANTIC_V2:
            return SubmissionStatusForTestCase(
                root=_SubmissionStatusForTestCase.GradedV2(type="gradedV2", value=value)
            )  # type: ignore
        else:
            return SubmissionStatusForTestCase(
                __root__=_SubmissionStatusForTestCase.GradedV2(
                    type="gradedV2", value=value
                )
            )  # type: ignore

    def traced(self, value: TracedTestCase) -> SubmissionStatusForTestCase:
        if IS_PYDANTIC_V2:
            return SubmissionStatusForTestCase(
                root=_SubmissionStatusForTestCase.Traced(
                    **value.dict(exclude_unset=True), type="traced"
                )
            )  # type: ignore
        else:
            return SubmissionStatusForTestCase(
                __root__=_SubmissionStatusForTestCase.Traced(
                    **value.dict(exclude_unset=True), type="traced"
                )
            )  # type: ignore


class SubmissionStatusForTestCase(UniversalRootModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[
            typing.Union[
                _SubmissionStatusForTestCase.Graded,
                _SubmissionStatusForTestCase.GradedV2,
                _SubmissionStatusForTestCase.Traced,
            ],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(
            self,
        ) -> typing.Union[
            _SubmissionStatusForTestCase.Graded,
            _SubmissionStatusForTestCase.GradedV2,
            _SubmissionStatusForTestCase.Traced,
        ]:
            return self.root
    else:
        __root__: typing_extensions.Annotated[
            typing.Union[
                _SubmissionStatusForTestCase.Graded,
                _SubmissionStatusForTestCase.GradedV2,
                _SubmissionStatusForTestCase.Traced,
            ],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(
            self,
        ) -> typing.Union[
            _SubmissionStatusForTestCase.Graded,
            _SubmissionStatusForTestCase.GradedV2,
            _SubmissionStatusForTestCase.Traced,
        ]:
            return self.__root__

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        if IS_PYDANTIC_V2:
            return self.root.dict(**kwargs)
        else:
            return self.__root__.dict(**kwargs)

    def visit(
        self,
        graded: typing.Callable[[TestCaseResultWithStdout], T_Result],
        graded_v_2: typing.Callable[[TestCaseGrade], T_Result],
        traced: typing.Callable[[TracedTestCase], T_Result],
    ) -> T_Result:
        unioned_value = self.get_as_union()
        if unioned_value.type == "graded":
            return graded(
                TestCaseResultWithStdout(
                    **unioned_value.dict(exclude_unset=True, exclude={"type"})
                )
            )
        if unioned_value.type == "gradedV2":
            return graded_v_2(unioned_value.value)
        if unioned_value.type == "traced":
            return traced(
                TracedTestCase(
                    **unioned_value.dict(exclude_unset=True, exclude={"type"})
                )
            )


class _SubmissionStatusForTestCase:
    class Graded(TestCaseResultWithStdout):
        type: typing.Literal["graded"] = "graded"

    class GradedV2(UniversalBaseModel):
        type: typing.Literal["gradedV2"] = "gradedV2"
        value: TestCaseGrade

    class Traced(TracedTestCase):
        type: typing.Literal["traced"] = "traced"


update_forward_refs(SubmissionStatusForTestCase)
update_forward_refs(KeyValuePair)
update_forward_refs(MapValue)
