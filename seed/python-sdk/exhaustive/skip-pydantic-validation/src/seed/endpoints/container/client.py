# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...core.unchecked_base_model import construct_type
from ...types.object.types.object_with_required_field import ObjectWithRequiredField

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ContainerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_and_return_list_of_primitives(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]

        Examples
        --------
        from seed.client import SeedExhaustive

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.container.get_and_return_list_of_primitives(
            request=["string"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "container/list-of-primitives", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.List[str], construct_type(type_=typing.List[str], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_and_return_list_of_objects(
        self,
        *,
        request: typing.Sequence[ObjectWithRequiredField],
        request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ObjectWithRequiredField]:
        """
        Parameters
        ----------
        request : typing.Sequence[ObjectWithRequiredField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ObjectWithRequiredField]

        Examples
        --------
        from seed.client import SeedExhaustive
        from seed.types.object.types import ObjectWithRequiredField

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.container.get_and_return_list_of_objects(
            request=[
                ObjectWithRequiredField(
                    string="string",
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "container/list-of-objects", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.List[ObjectWithRequiredField], construct_type(type_=typing.List[ObjectWithRequiredField], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_and_return_set_of_primitives(
        self, *, request: typing.Set[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Set[str]:
        """
        Parameters
        ----------
        request : typing.Set[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Set[str]

        Examples
        --------
        from seed.client import SeedExhaustive

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.container.get_and_return_set_of_primitives(
            request={"string"},
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "container/set-of-primitives", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.Set[str], construct_type(type_=typing.Set[str], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_and_return_set_of_objects(
        self,
        *,
        request: typing.Sequence[ObjectWithRequiredField],
        request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ObjectWithRequiredField]:
        """
        Parameters
        ----------
        request : typing.Sequence[ObjectWithRequiredField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ObjectWithRequiredField]

        Examples
        --------
        from seed.client import SeedExhaustive
        from seed.types.object.types import ObjectWithRequiredField

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.container.get_and_return_set_of_objects(
            request=[
                ObjectWithRequiredField(
                    string="string",
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "container/set-of-objects", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.List[ObjectWithRequiredField], construct_type(type_=typing.List[ObjectWithRequiredField], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_and_return_map_prim_to_prim(
        self, *, request: typing.Dict[str, str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        request : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]

        Examples
        --------
        from seed.client import SeedExhaustive

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.container.get_and_return_map_prim_to_prim(
            request={"string": "string"},
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "container/map-prim-to-prim", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.Dict[str, str], construct_type(type_=typing.Dict[str, str], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_and_return_map_of_prim_to_object(
        self,
        *,
        request: typing.Dict[str, ObjectWithRequiredField],
        request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, ObjectWithRequiredField]:
        """
        Parameters
        ----------
        request : typing.Dict[str, ObjectWithRequiredField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, ObjectWithRequiredField]

        Examples
        --------
        from seed.client import SeedExhaustive
        from seed.types.object.types import ObjectWithRequiredField

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.container.get_and_return_map_of_prim_to_object(
            request={
                "string": ObjectWithRequiredField(
                    string="string",
                )
            },
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "container/map-prim-to-object", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.Dict[str, ObjectWithRequiredField], construct_type(type_=typing.Dict[str, ObjectWithRequiredField], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_and_return_optional(
        self,
        *,
        request: typing.Optional[ObjectWithRequiredField] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ObjectWithRequiredField]:
        """
        Parameters
        ----------
        request : typing.Optional[ObjectWithRequiredField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ObjectWithRequiredField]

        Examples
        --------
        from seed.client import SeedExhaustive
        from seed.types.object.types import ObjectWithRequiredField

        client = SeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints.container.get_and_return_optional(
            request=ObjectWithRequiredField(
                string="string",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "container/opt-objects", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.Optional[ObjectWithRequiredField], construct_type(type_=typing.Optional[ObjectWithRequiredField], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncContainerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_and_return_list_of_primitives(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]

        Examples
        --------
        import asyncio

        from seed.client import AsyncSeedExhaustive

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoints.container.get_and_return_list_of_primitives(
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "container/list-of-primitives", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.List[str], construct_type(type_=typing.List[str], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_and_return_list_of_objects(
        self,
        *,
        request: typing.Sequence[ObjectWithRequiredField],
        request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ObjectWithRequiredField]:
        """
        Parameters
        ----------
        request : typing.Sequence[ObjectWithRequiredField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ObjectWithRequiredField]

        Examples
        --------
        import asyncio

        from seed.client import AsyncSeedExhaustive
        from seed.types.object.types import ObjectWithRequiredField

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoints.container.get_and_return_list_of_objects(
                request=[
                    ObjectWithRequiredField(
                        string="string",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "container/list-of-objects", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.List[ObjectWithRequiredField], construct_type(type_=typing.List[ObjectWithRequiredField], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_and_return_set_of_primitives(
        self, *, request: typing.Set[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Set[str]:
        """
        Parameters
        ----------
        request : typing.Set[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Set[str]

        Examples
        --------
        import asyncio

        from seed.client import AsyncSeedExhaustive

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoints.container.get_and_return_set_of_primitives(
                request={"string"},
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "container/set-of-primitives", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.Set[str], construct_type(type_=typing.Set[str], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_and_return_set_of_objects(
        self,
        *,
        request: typing.Sequence[ObjectWithRequiredField],
        request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ObjectWithRequiredField]:
        """
        Parameters
        ----------
        request : typing.Sequence[ObjectWithRequiredField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ObjectWithRequiredField]

        Examples
        --------
        import asyncio

        from seed.client import AsyncSeedExhaustive
        from seed.types.object.types import ObjectWithRequiredField

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoints.container.get_and_return_set_of_objects(
                request=[
                    ObjectWithRequiredField(
                        string="string",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "container/set-of-objects", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.List[ObjectWithRequiredField], construct_type(type_=typing.List[ObjectWithRequiredField], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_and_return_map_prim_to_prim(
        self, *, request: typing.Dict[str, str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        request : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]

        Examples
        --------
        import asyncio

        from seed.client import AsyncSeedExhaustive

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoints.container.get_and_return_map_prim_to_prim(
                request={"string": "string"},
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "container/map-prim-to-prim", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.Dict[str, str], construct_type(type_=typing.Dict[str, str], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_and_return_map_of_prim_to_object(
        self,
        *,
        request: typing.Dict[str, ObjectWithRequiredField],
        request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, ObjectWithRequiredField]:
        """
        Parameters
        ----------
        request : typing.Dict[str, ObjectWithRequiredField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, ObjectWithRequiredField]

        Examples
        --------
        import asyncio

        from seed.client import AsyncSeedExhaustive
        from seed.types.object.types import ObjectWithRequiredField

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoints.container.get_and_return_map_of_prim_to_object(
                request={
                    "string": ObjectWithRequiredField(
                        string="string",
                    )
                },
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "container/map-prim-to-object", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.Dict[str, ObjectWithRequiredField], construct_type(type_=typing.Dict[str, ObjectWithRequiredField], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_and_return_optional(
        self,
        *,
        request: typing.Optional[ObjectWithRequiredField] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ObjectWithRequiredField]:
        """
        Parameters
        ----------
        request : typing.Optional[ObjectWithRequiredField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ObjectWithRequiredField]

        Examples
        --------
        import asyncio

        from seed.client import AsyncSeedExhaustive
        from seed.types.object.types import ObjectWithRequiredField

        client = AsyncSeedExhaustive(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoints.container.get_and_return_optional(
                request=ObjectWithRequiredField(
                    string="string",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "container/opt-objects", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.Optional[ObjectWithRequiredField], construct_type(type_=typing.Optional[ObjectWithRequiredField], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
