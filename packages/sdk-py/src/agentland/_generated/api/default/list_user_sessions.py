from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_user_sessions_response_400 import ListUserSessionsResponse400
from ...models.list_user_sessions_response_401 import ListUserSessionsResponse401
from ...models.list_user_sessions_response_403 import ListUserSessionsResponse403
from ...models.list_user_sessions_response_404 import ListUserSessionsResponse404
from ...models.list_user_sessions_response_429 import ListUserSessionsResponse429
from ...models.list_user_sessions_response_500 import ListUserSessionsResponse500
from ...models.session import Session
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/list-sessions",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListUserSessionsResponse400 | ListUserSessionsResponse401 | ListUserSessionsResponse403 | ListUserSessionsResponse404 | ListUserSessionsResponse429 | ListUserSessionsResponse500 | list[Session] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = Session.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ListUserSessionsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ListUserSessionsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ListUserSessionsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ListUserSessionsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = ListUserSessionsResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = ListUserSessionsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListUserSessionsResponse400 | ListUserSessionsResponse401 | ListUserSessionsResponse403 | ListUserSessionsResponse404 | ListUserSessionsResponse429 | ListUserSessionsResponse500 | list[Session]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[ListUserSessionsResponse400 | ListUserSessionsResponse401 | ListUserSessionsResponse403 | ListUserSessionsResponse404 | ListUserSessionsResponse429 | ListUserSessionsResponse500 | list[Session]]:
    """  List all active sessions for the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListUserSessionsResponse400 | ListUserSessionsResponse401 | ListUserSessionsResponse403 | ListUserSessionsResponse404 | ListUserSessionsResponse429 | ListUserSessionsResponse500 | list[Session]]
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

) -> ListUserSessionsResponse400 | ListUserSessionsResponse401 | ListUserSessionsResponse403 | ListUserSessionsResponse404 | ListUserSessionsResponse429 | ListUserSessionsResponse500 | list[Session] | None:
    """  List all active sessions for the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListUserSessionsResponse400 | ListUserSessionsResponse401 | ListUserSessionsResponse403 | ListUserSessionsResponse404 | ListUserSessionsResponse429 | ListUserSessionsResponse500 | list[Session]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[ListUserSessionsResponse400 | ListUserSessionsResponse401 | ListUserSessionsResponse403 | ListUserSessionsResponse404 | ListUserSessionsResponse429 | ListUserSessionsResponse500 | list[Session]]:
    """  List all active sessions for the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListUserSessionsResponse400 | ListUserSessionsResponse401 | ListUserSessionsResponse403 | ListUserSessionsResponse404 | ListUserSessionsResponse429 | ListUserSessionsResponse500 | list[Session]]
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

) -> ListUserSessionsResponse400 | ListUserSessionsResponse401 | ListUserSessionsResponse403 | ListUserSessionsResponse404 | ListUserSessionsResponse429 | ListUserSessionsResponse500 | list[Session] | None:
    """  List all active sessions for the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListUserSessionsResponse400 | ListUserSessionsResponse401 | ListUserSessionsResponse403 | ListUserSessionsResponse404 | ListUserSessionsResponse429 | ListUserSessionsResponse500 | list[Session]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
