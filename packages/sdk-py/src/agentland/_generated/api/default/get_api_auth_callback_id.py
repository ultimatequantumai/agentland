from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_api_auth_callback_id_response_400 import GetApiAuthCallbackIdResponse400
from ...models.get_api_auth_callback_id_response_401 import GetApiAuthCallbackIdResponse401
from ...models.get_api_auth_callback_id_response_403 import GetApiAuthCallbackIdResponse403
from ...models.get_api_auth_callback_id_response_404 import GetApiAuthCallbackIdResponse404
from ...models.get_api_auth_callback_id_response_429 import GetApiAuthCallbackIdResponse429
from ...models.get_api_auth_callback_id_response_500 import GetApiAuthCallbackIdResponse500
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/callback/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetApiAuthCallbackIdResponse400 | GetApiAuthCallbackIdResponse401 | GetApiAuthCallbackIdResponse403 | GetApiAuthCallbackIdResponse404 | GetApiAuthCallbackIdResponse429 | GetApiAuthCallbackIdResponse500 | None:
    if response.status_code == 400:
        response_400 = GetApiAuthCallbackIdResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetApiAuthCallbackIdResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetApiAuthCallbackIdResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetApiAuthCallbackIdResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GetApiAuthCallbackIdResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GetApiAuthCallbackIdResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetApiAuthCallbackIdResponse400 | GetApiAuthCallbackIdResponse401 | GetApiAuthCallbackIdResponse403 | GetApiAuthCallbackIdResponse404 | GetApiAuthCallbackIdResponse429 | GetApiAuthCallbackIdResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetApiAuthCallbackIdResponse400 | GetApiAuthCallbackIdResponse401 | GetApiAuthCallbackIdResponse403 | GetApiAuthCallbackIdResponse404 | GetApiAuthCallbackIdResponse429 | GetApiAuthCallbackIdResponse500]:
    """ 
    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthCallbackIdResponse400 | GetApiAuthCallbackIdResponse401 | GetApiAuthCallbackIdResponse403 | GetApiAuthCallbackIdResponse404 | GetApiAuthCallbackIdResponse429 | GetApiAuthCallbackIdResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetApiAuthCallbackIdResponse400 | GetApiAuthCallbackIdResponse401 | GetApiAuthCallbackIdResponse403 | GetApiAuthCallbackIdResponse404 | GetApiAuthCallbackIdResponse429 | GetApiAuthCallbackIdResponse500 | None:
    """ 
    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthCallbackIdResponse400 | GetApiAuthCallbackIdResponse401 | GetApiAuthCallbackIdResponse403 | GetApiAuthCallbackIdResponse404 | GetApiAuthCallbackIdResponse429 | GetApiAuthCallbackIdResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetApiAuthCallbackIdResponse400 | GetApiAuthCallbackIdResponse401 | GetApiAuthCallbackIdResponse403 | GetApiAuthCallbackIdResponse404 | GetApiAuthCallbackIdResponse429 | GetApiAuthCallbackIdResponse500]:
    """ 
    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthCallbackIdResponse400 | GetApiAuthCallbackIdResponse401 | GetApiAuthCallbackIdResponse403 | GetApiAuthCallbackIdResponse404 | GetApiAuthCallbackIdResponse429 | GetApiAuthCallbackIdResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetApiAuthCallbackIdResponse400 | GetApiAuthCallbackIdResponse401 | GetApiAuthCallbackIdResponse403 | GetApiAuthCallbackIdResponse404 | GetApiAuthCallbackIdResponse429 | GetApiAuthCallbackIdResponse500 | None:
    """ 
    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthCallbackIdResponse400 | GetApiAuthCallbackIdResponse401 | GetApiAuthCallbackIdResponse403 | GetApiAuthCallbackIdResponse404 | GetApiAuthCallbackIdResponse429 | GetApiAuthCallbackIdResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
