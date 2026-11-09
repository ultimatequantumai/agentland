from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_api_auth_account_info_response_200 import GetApiAuthAccountInfoResponse200
from ...models.get_api_auth_account_info_response_400 import GetApiAuthAccountInfoResponse400
from ...models.get_api_auth_account_info_response_401 import GetApiAuthAccountInfoResponse401
from ...models.get_api_auth_account_info_response_403 import GetApiAuthAccountInfoResponse403
from ...models.get_api_auth_account_info_response_404 import GetApiAuthAccountInfoResponse404
from ...models.get_api_auth_account_info_response_429 import GetApiAuthAccountInfoResponse429
from ...models.get_api_auth_account_info_response_500 import GetApiAuthAccountInfoResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/account-info",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetApiAuthAccountInfoResponse200 | GetApiAuthAccountInfoResponse400 | GetApiAuthAccountInfoResponse401 | GetApiAuthAccountInfoResponse403 | GetApiAuthAccountInfoResponse404 | GetApiAuthAccountInfoResponse429 | GetApiAuthAccountInfoResponse500 | None:
    if response.status_code == 200:
        response_200 = GetApiAuthAccountInfoResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetApiAuthAccountInfoResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetApiAuthAccountInfoResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetApiAuthAccountInfoResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetApiAuthAccountInfoResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GetApiAuthAccountInfoResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GetApiAuthAccountInfoResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetApiAuthAccountInfoResponse200 | GetApiAuthAccountInfoResponse400 | GetApiAuthAccountInfoResponse401 | GetApiAuthAccountInfoResponse403 | GetApiAuthAccountInfoResponse404 | GetApiAuthAccountInfoResponse429 | GetApiAuthAccountInfoResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetApiAuthAccountInfoResponse200 | GetApiAuthAccountInfoResponse400 | GetApiAuthAccountInfoResponse401 | GetApiAuthAccountInfoResponse403 | GetApiAuthAccountInfoResponse404 | GetApiAuthAccountInfoResponse429 | GetApiAuthAccountInfoResponse500]:
    """  Get the account info provided by the provider

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthAccountInfoResponse200 | GetApiAuthAccountInfoResponse400 | GetApiAuthAccountInfoResponse401 | GetApiAuthAccountInfoResponse403 | GetApiAuthAccountInfoResponse404 | GetApiAuthAccountInfoResponse429 | GetApiAuthAccountInfoResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> GetApiAuthAccountInfoResponse200 | GetApiAuthAccountInfoResponse400 | GetApiAuthAccountInfoResponse401 | GetApiAuthAccountInfoResponse403 | GetApiAuthAccountInfoResponse404 | GetApiAuthAccountInfoResponse429 | GetApiAuthAccountInfoResponse500 | None:
    """  Get the account info provided by the provider

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthAccountInfoResponse200 | GetApiAuthAccountInfoResponse400 | GetApiAuthAccountInfoResponse401 | GetApiAuthAccountInfoResponse403 | GetApiAuthAccountInfoResponse404 | GetApiAuthAccountInfoResponse429 | GetApiAuthAccountInfoResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetApiAuthAccountInfoResponse200 | GetApiAuthAccountInfoResponse400 | GetApiAuthAccountInfoResponse401 | GetApiAuthAccountInfoResponse403 | GetApiAuthAccountInfoResponse404 | GetApiAuthAccountInfoResponse429 | GetApiAuthAccountInfoResponse500]:
    """  Get the account info provided by the provider

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthAccountInfoResponse200 | GetApiAuthAccountInfoResponse400 | GetApiAuthAccountInfoResponse401 | GetApiAuthAccountInfoResponse403 | GetApiAuthAccountInfoResponse404 | GetApiAuthAccountInfoResponse429 | GetApiAuthAccountInfoResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> GetApiAuthAccountInfoResponse200 | GetApiAuthAccountInfoResponse400 | GetApiAuthAccountInfoResponse401 | GetApiAuthAccountInfoResponse403 | GetApiAuthAccountInfoResponse404 | GetApiAuthAccountInfoResponse429 | GetApiAuthAccountInfoResponse500 | None:
    """  Get the account info provided by the provider

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthAccountInfoResponse200 | GetApiAuthAccountInfoResponse400 | GetApiAuthAccountInfoResponse401 | GetApiAuthAccountInfoResponse403 | GetApiAuthAccountInfoResponse404 | GetApiAuthAccountInfoResponse429 | GetApiAuthAccountInfoResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
