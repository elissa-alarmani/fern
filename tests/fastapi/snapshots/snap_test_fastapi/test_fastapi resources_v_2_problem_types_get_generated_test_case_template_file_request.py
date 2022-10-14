# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .test_case_template import TestCaseTemplate


class GetGeneratedTestCaseTemplateFileRequest(pydantic.BaseModel):
    template: TestCaseTemplate

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetGeneratedTestCaseTemplateFileRequest.Validators.root
            def validate(values: GetGeneratedTestCaseTemplateFileRequest.Partial) -> GetGeneratedTestCaseTemplateFileRequest.Partial:
                ...

            @GetGeneratedTestCaseTemplateFileRequest.Validators.field("template")
            def validate_template(v: TestCaseTemplate, values: GetGeneratedTestCaseTemplateFileRequest.Partial) -> TestCaseTemplate:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [GetGeneratedTestCaseTemplateFileRequest.Partial], GetGeneratedTestCaseTemplateFileRequest.Partial
                ]
            ]
        ] = []
        _template_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseTemplateFileRequest.Validators.TemplateValidator]
        ] = []

        @classmethod
        def root(
            cls,
            validator: typing.Callable[
                [GetGeneratedTestCaseTemplateFileRequest.Partial], GetGeneratedTestCaseTemplateFileRequest.Partial
            ],
        ) -> typing.Callable[
            [GetGeneratedTestCaseTemplateFileRequest.Partial], GetGeneratedTestCaseTemplateFileRequest.Partial
        ]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["template"]
        ) -> typing.Callable[
            [GetGeneratedTestCaseTemplateFileRequest.Validators.TemplateValidator],
            GetGeneratedTestCaseTemplateFileRequest.Validators.TemplateValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "template":
                    cls._template_validators.append(validator)
                return validator

            return decorator

        class TemplateValidator(typing_extensions.Protocol):
            def __call__(
                self, v: TestCaseTemplate, *, values: GetGeneratedTestCaseTemplateFileRequest.Partial
            ) -> TestCaseTemplate:
                ...

    @pydantic.root_validator
    def _validate(
        cls, values: GetGeneratedTestCaseTemplateFileRequest.Partial
    ) -> GetGeneratedTestCaseTemplateFileRequest.Partial:
        for validator in GetGeneratedTestCaseTemplateFileRequest.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("template")
    def _validate_template(
        cls, v: TestCaseTemplate, values: GetGeneratedTestCaseTemplateFileRequest.Partial
    ) -> TestCaseTemplate:
        for validator in GetGeneratedTestCaseTemplateFileRequest.Validators._template_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        template: typing_extensions.NotRequired[TestCaseTemplate]

    class Config:
        frozen = True
