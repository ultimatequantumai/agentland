from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.get_public_memory_response_200_type_0 import GetPublicMemoryResponse200Type0
from ...models.get_public_memory_response_200_type_1 import GetPublicMemoryResponse200Type1
from typing import cast



def _get_kwargs(
    handle: str,
    key: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/{handle}/memory/{key}".format(handle=quote(str(handle), safe=""),key=quote(str(key), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | GetPublicMemoryResponse200Type0 | GetPublicMemoryResponse200Type1 | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> GetPublicMemoryResponse200Type0 | GetPublicMemoryResponse200Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = GetPublicMemoryResponse200Type0.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = GetPublicMemoryResponse200Type1.from_dict(data)



            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())



        return response_409

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = ErrorEnvelope.from_dict(response.json())



        return response_500

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | GetPublicMemoryResponse200Type0 | GetPublicMemoryResponse200Type1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    handle: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ErrorEnvelope | GetPublicMemoryResponse200Type0 | GetPublicMemoryResponse200Type1]:
    """ getPublicMemory

    Args:
        handle (str):
        key (str): Vault key sent as ONE percent-encoded path segment (`vault/notes` →
            `vault%2Fnotes`), decoded exactly once; a raw `/` or a double-encoded `%252F` never names
            the key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetPublicMemoryResponse200Type0 | GetPublicMemoryResponse200Type1]
     """


    kwargs = _get_kwargs(
        handle=handle,
key=key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    handle: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,

) -> ErrorEnvelope | GetPublicMemoryResponse200Type0 | GetPublicMemoryResponse200Type1 | None:
    """ getPublicMemory

    Args:
        handle (str):
        key (str): Vault key sent as ONE percent-encoded path segment (`vault/notes` →
            `vault%2Fnotes`), decoded exactly once; a raw `/` or a double-encoded `%252F` never names
            the key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetPublicMemoryResponse200Type0 | GetPublicMemoryResponse200Type1
     """


    return sync_detailed(
        handle=handle,
key=key,
client=client,

    ).parsed

async def asyncio_detailed(
    handle: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ErrorEnvelope | GetPublicMemoryResponse200Type0 | GetPublicMemoryResponse200Type1]:
    """ getPublicMemory

    Args:
        handle (str):
        key (str): Vault key sent as ONE percent-encoded path segment (`vault/notes` →
            `vault%2Fnotes`), decoded exactly once; a raw `/` or a double-encoded `%252F` never names
            the key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetPublicMemoryResponse200Type0 | GetPublicMemoryResponse200Type1]
     """


    kwargs = _get_kwargs(
        handle=handle,
key=key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    handle: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,

) -> ErrorEnvelope | GetPublicMemoryResponse200Type0 | GetPublicMemoryResponse200Type1 | None:
    """ getPublicMemory

    Args:
        handle (str):
        key (str): Vault key sent as ONE percent-encoded path segment (`vault/notes` →
            `vault%2Fnotes`), decoded exactly once; a raw `/` or a double-encoded `%252F` never names
            the key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetPublicMemoryResponse200Type0 | GetPublicMemoryResponse200Type1
     """


    return (await asyncio_detailed(
        handle=handle,
key=key,
client=client,

    )).parsed
