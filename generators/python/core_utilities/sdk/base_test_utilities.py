import typing
import uuid

from dateutil import parser

import pydantic


def cast_field(json_expectation: typing.Any, type_expectation: typing.Any) -> typing.Any:
    # Cast these specific types which come through as string and expect our
    # models to cast to the correct type.
    if type_expectation == "uuid":
        return uuid.UUID(json_expectation)
    elif type_expectation == "date":
        return parser.parse(json_expectation).date()
    elif type_expectation == "datetime":
        return parser.parse(json_expectation)
    elif type_expectation == "set":
        return set(json_expectation)
    elif type_expectation == "integer":
        # Necessary as we allow numeric keys, but JSON makes them strings
        return int(json_expectation)

    return json_expectation


def validate_field(response: typing.Any, json_expectation: typing.Any, type_expectation: typing.Any) -> None:
    # Allow for an escape hatch if the object cannot be validated
    if type_expectation == "no_validate":
        return

    is_container_of_complex_type = False
    # Parse types in containers, note that dicts are handled within `validate_response`
    if isinstance(json_expectation, list):
        if isinstance(type_expectation, tuple):
            container_expectation = type_expectation[0]
            contents_expectation = type_expectation[1]

            cast_json_expectation = []
            for idx, ex in enumerate(json_expectation):
                if isinstance(contents_expectation, dict):
                    entry_expectation = contents_expectation.get(idx)
                    if isinstance(entry_expectation, dict):
                        is_container_of_complex_type = True
                        validate_response(
                            response=response[idx], json_expectation=ex, type_expectations=entry_expectation
                        )
                    else:
                        cast_json_expectation.append(cast_field(ex, entry_expectation))
                else:
                    cast_json_expectation.append(ex)
            json_expectation = cast_json_expectation

            # Note that we explicitly do not allow for sets of pydantic models as they are not hashable, so
            # if any of the values of the set have a type_expectation of a dict, we're assuming it's a pydantic
            # model and keeping it a list.
            if container_expectation != "set" or not any(
                map(lambda value: isinstance(value, dict), list(contents_expectation.values()))
            ):
                json_expectation = cast_field(json_expectation, container_expectation)
    elif isinstance(type_expectation, tuple):
        container_expectation = type_expectation[0]
        contents_expectation = type_expectation[1]
        if isinstance(contents_expectation, dict):
            json_expectation = {
                cast_field(
                    key, contents_expectation.get(idx)[0] if contents_expectation.get(idx) is not None else None  # type: ignore
                ): cast_field(
                    value, contents_expectation.get(idx)[1] if contents_expectation.get(idx) is not None else None  # type: ignore
                )
                for idx, (key, value) in enumerate(json_expectation.items())
            }
        else:
            json_expectation = cast_field(json_expectation, container_expectation)
    elif type_expectation is not None:
        json_expectation = cast_field(json_expectation, type_expectation)

    # When dealing with containers of models, etc. we're validating them implicitly, so no need to check the resultant list
    if not is_container_of_complex_type:
        assert json_expectation == response, "Primitives found, expected: {0}, Actual: {1}".format(
            json_expectation, response
        )


# Arg type_expectations is a deeply nested structure that matches the response, but with the values replaced with the expected types
def validate_response(response: typing.Any, json_expectation: typing.Any, type_expectations: typing.Any) -> None:
    # Allow for an escape hatch if the object cannot be validated
    if type_expectations == "no_validate":
        return

    if (
        not isinstance(response, list)
        and not isinstance(response, dict)
        and not issubclass(type(response), pydantic.BaseModel)
    ):
        validate_field(response=response, json_expectation=json_expectation, type_expectation=type_expectations)
        return

    if isinstance(response, list):
        assert len(response) == len(json_expectation), "Length mismatch, expected: {0}, Actual: {1}".format(
            len(response), len(json_expectation)
        )
        for idx, item in enumerate(response):
            validate_response(
                response=item, json_expectation=json_expectation[idx], type_expectations=type_expectations[idx]
            )
    else:
        response_json = response
        if issubclass(type(response), pydantic.BaseModel):
            response_json = response.dict(by_alias=True)

        for key, value in json_expectation.items():
            assert key in response_json, "Field {0} not found within the response object: {1}".format(
                key, response_json
            )

            type_expectation = None
            if type_expectations is not None and isinstance(type_expectations, dict):
                type_expectation = type_expectations.get(key)

            # If your type_expectation is a tuple then you have a container field, process it as such
            # Otherwise, we're just validating a single field that's a pydantic model.
            if isinstance(value, dict) and not isinstance(type_expectation, tuple):
                validate_response(
                    response=response_json[key], json_expectation=value, type_expectations=type_expectation
                )
            else:
                validate_field(response=response_json[key], json_expectation=value, type_expectation=type_expectation)

            # Ensure there are no additional fields here either
            del response_json[key]
        assert len(response_json) == 0, "Additional fields found, expected None: {0}".format(response_json)
