from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.list_public_memory_response_200 import ListPublicMemoryResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    handle: str,
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    tag: list[str] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["prefix"] = prefix

    json_tag: list[str] | Unset = UNSET
    if not isinstance(tag, Unset):
        json_tag = tag


    params["tag"] = json_tag


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/{handle}/memory".format(handle=quote(str(handle), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | ListPublicMemoryResponse200 | None:
    if response.status_code == 200:
        response_200 = ListPublicMemoryResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | ListPublicMemoryResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    handle: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    tag: list[str] | Unset = UNSET,

) -> Response[ErrorEnvelope | ListPublicMemoryResponse200]:
    """ listPublicMemory

    Args:
        handle (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        prefix (str | Unset):
        tag (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListPublicMemoryResponse200]
     """


    kwargs = _get_kwargs(
        handle=handle,
limit=limit,
cursor=cursor,
prefix=prefix,
tag=tag,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    handle: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    tag: list[str] | Unset = UNSET,

) -> ErrorEnvelope | ListPublicMemoryResponse200 | None:
    """ listPublicMemory

    Args:
        handle (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        prefix (str | Unset):
        tag (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListPublicMemoryResponse200
     """


    return sync_detailed(
        handle=handle,
client=client,
limit=limit,
cursor=cursor,
prefix=prefix,
tag=tag,

    ).parsed

async def asyncio_detailed(
    handle: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    tag: list[str] | Unset = UNSET,

) -> Response[ErrorEnvelope | ListPublicMemoryResponse200]:
    """ listPublicMemory

    Args:
        handle (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        prefix (str | Unset):
        tag (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListPublicMemoryResponse200]
     """


    kwargs = _get_kwargs(
        handle=handle,
limit=limit,
cursor=cursor,
prefix=prefix,
tag=tag,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    handle: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    tag: list[str] | Unset = UNSET,

) -> ErrorEnvelope | ListPublicMemoryResponse200 | None:
    """ listPublicMemory

    Args:
        handle (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        prefix (str | Unset):
        tag (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListPublicMemoryResponse200
     """


    return (await asyncio_detailed(
        handle=handle,
client=client,
limit=limit,
cursor=cursor,
prefix=prefix,
tag=tag,

    )).parsed
