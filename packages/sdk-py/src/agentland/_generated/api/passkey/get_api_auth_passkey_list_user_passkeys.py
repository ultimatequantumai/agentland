from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_api_auth_passkey_list_user_passkeys_response_400 import GetApiAuthPasskeyListUserPasskeysResponse400
from ...models.get_api_auth_passkey_list_user_passkeys_response_401 import GetApiAuthPasskeyListUserPasskeysResponse401
from ...models.get_api_auth_passkey_list_user_passkeys_response_403 import GetApiAuthPasskeyListUserPasskeysResponse403
from ...models.get_api_auth_passkey_list_user_passkeys_response_404 import GetApiAuthPasskeyListUserPasskeysResponse404
from ...models.get_api_auth_passkey_list_user_passkeys_response_429 import GetApiAuthPasskeyListUserPasskeysResponse429
from ...models.get_api_auth_passkey_list_user_passkeys_response_500 import GetApiAuthPasskeyListUserPasskeysResponse500
from ...models.passkey import Passkey
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/passkey/list-user-passkeys",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetApiAuthPasskeyListUserPasskeysResponse400 | GetApiAuthPasskeyListUserPasskeysResponse401 | GetApiAuthPasskeyListUserPasskeysResponse403 | GetApiAuthPasskeyListUserPasskeysResponse404 | GetApiAuthPasskeyListUserPasskeysResponse429 | GetApiAuthPasskeyListUserPasskeysResponse500 | list[Passkey] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = Passkey.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetApiAuthPasskeyListUserPasskeysResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetApiAuthPasskeyListUserPasskeysResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetApiAuthPasskeyListUserPasskeysResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetApiAuthPasskeyListUserPasskeysResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GetApiAuthPasskeyListUserPasskeysResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GetApiAuthPasskeyListUserPasskeysResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetApiAuthPasskeyListUserPasskeysResponse400 | GetApiAuthPasskeyListUserPasskeysResponse401 | GetApiAuthPasskeyListUserPasskeysResponse403 | GetApiAuthPasskeyListUserPasskeysResponse404 | GetApiAuthPasskeyListUserPasskeysResponse429 | GetApiAuthPasskeyListUserPasskeysResponse500 | list[Passkey]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetApiAuthPasskeyListUserPasskeysResponse400 | GetApiAuthPasskeyListUserPasskeysResponse401 | GetApiAuthPasskeyListUserPasskeysResponse403 | GetApiAuthPasskeyListUserPasskeysResponse404 | GetApiAuthPasskeyListUserPasskeysResponse429 | GetApiAuthPasskeyListUserPasskeysResponse500 | list[Passkey]]:
    """  List all passkeys for the authenticated user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthPasskeyListUserPasskeysResponse400 | GetApiAuthPasskeyListUserPasskeysResponse401 | GetApiAuthPasskeyListUserPasskeysResponse403 | GetApiAuthPasskeyListUserPasskeysResponse404 | GetApiAuthPasskeyListUserPasskeysResponse429 | GetApiAuthPasskeyListUserPasskeysResponse500 | list[Passkey]]
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

) -> GetApiAuthPasskeyListUserPasskeysResponse400 | GetApiAuthPasskeyListUserPasskeysResponse401 | GetApiAuthPasskeyListUserPasskeysResponse403 | GetApiAuthPasskeyListUserPasskeysResponse404 | GetApiAuthPasskeyListUserPasskeysResponse429 | GetApiAuthPasskeyListUserPasskeysResponse500 | list[Passkey] | None:
    """  List all passkeys for the authenticated user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthPasskeyListUserPasskeysResponse400 | GetApiAuthPasskeyListUserPasskeysResponse401 | GetApiAuthPasskeyListUserPasskeysResponse403 | GetApiAuthPasskeyListUserPasskeysResponse404 | GetApiAuthPasskeyListUserPasskeysResponse429 | GetApiAuthPasskeyListUserPasskeysResponse500 | list[Passkey]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetApiAuthPasskeyListUserPasskeysResponse400 | GetApiAuthPasskeyListUserPasskeysResponse401 | GetApiAuthPasskeyListUserPasskeysResponse403 | GetApiAuthPasskeyListUserPasskeysResponse404 | GetApiAuthPasskeyListUserPasskeysResponse429 | GetApiAuthPasskeyListUserPasskeysResponse500 | list[Passkey]]:
    """  List all passkeys for the authenticated user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthPasskeyListUserPasskeysResponse400 | GetApiAuthPasskeyListUserPasskeysResponse401 | GetApiAuthPasskeyListUserPasskeysResponse403 | GetApiAuthPasskeyListUserPasskeysResponse404 | GetApiAuthPasskeyListUserPasskeysResponse429 | GetApiAuthPasskeyListUserPasskeysResponse500 | list[Passkey]]
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

) -> GetApiAuthPasskeyListUserPasskeysResponse400 | GetApiAuthPasskeyListUserPasskeysResponse401 | GetApiAuthPasskeyListUserPasskeysResponse403 | GetApiAuthPasskeyListUserPasskeysResponse404 | GetApiAuthPasskeyListUserPasskeysResponse429 | GetApiAuthPasskeyListUserPasskeysResponse500 | list[Passkey] | None:
    """  List all passkeys for the authenticated user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthPasskeyListUserPasskeysResponse400 | GetApiAuthPasskeyListUserPasskeysResponse401 | GetApiAuthPasskeyListUserPasskeysResponse403 | GetApiAuthPasskeyListUserPasskeysResponse404 | GetApiAuthPasskeyListUserPasskeysResponse429 | GetApiAuthPasskeyListUserPasskeysResponse500 | list[Passkey]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
