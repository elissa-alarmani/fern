# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.problem_id import ProblemId


class PlaylistCreateRequest(pydantic.BaseModel):
    name: str
    problems: typing.List[ProblemId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @PlaylistCreateRequest.Validators.root
            def validate(values: PlaylistCreateRequest.Partial) -> PlaylistCreateRequest.Partial:
                ...

            @PlaylistCreateRequest.Validators.field("name")
            def validate_name(v: str, values: PlaylistCreateRequest.Partial) -> str:
                ...

            @PlaylistCreateRequest.Validators.field("problems")
            def validate_problems(v: typing.List[ProblemId], values: PlaylistCreateRequest.Partial) -> typing.List[ProblemId]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[PlaylistCreateRequest.Partial], PlaylistCreateRequest.Partial]]
        ] = []
        _name_validators: typing.ClassVar[typing.List[PlaylistCreateRequest.Validators.NameValidator]] = []
        _problems_validators: typing.ClassVar[typing.List[PlaylistCreateRequest.Validators.ProblemsValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[PlaylistCreateRequest.Partial], PlaylistCreateRequest.Partial]
        ) -> typing.Callable[[PlaylistCreateRequest.Partial], PlaylistCreateRequest.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"]
        ) -> typing.Callable[
            [PlaylistCreateRequest.Validators.NameValidator], PlaylistCreateRequest.Validators.NameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problems"]
        ) -> typing.Callable[
            [PlaylistCreateRequest.Validators.ProblemsValidator], PlaylistCreateRequest.Validators.ProblemsValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "name":
                    cls._name_validators.append(validator)
                if field_name == "problems":
                    cls._problems_validators.append(validator)
                return validator

            return decorator

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: PlaylistCreateRequest.Partial) -> str:
                ...

        class ProblemsValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[ProblemId], *, values: PlaylistCreateRequest.Partial
            ) -> typing.List[ProblemId]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: PlaylistCreateRequest.Partial) -> PlaylistCreateRequest.Partial:
        for validator in PlaylistCreateRequest.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("name")
    def _validate_name(cls, v: str, values: PlaylistCreateRequest.Partial) -> str:
        for validator in PlaylistCreateRequest.Validators._name_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("problems")
    def _validate_problems(
        cls, v: typing.List[ProblemId], values: PlaylistCreateRequest.Partial
    ) -> typing.List[ProblemId]:
        for validator in PlaylistCreateRequest.Validators._problems_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        name: typing_extensions.NotRequired[str]
        problems: typing_extensions.NotRequired[typing.List[ProblemId]]

    class Config:
        frozen = True
