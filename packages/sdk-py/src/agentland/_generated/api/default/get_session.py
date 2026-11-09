from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_session_response_200_type_0 import GetSessionResponse200Type0
from ...models.get_session_response_400 import GetSessionResponse400
from ...models.get_session_response_401 import GetSessionResponse401
from ...models.get_session_response_403 import GetSessionResponse403
from ...models.get_session_response_404 import GetSessionResponse404
from ...models.get_session_response_429 import GetSessionResponse429
from ...models.get_session_response_500 import GetSessionResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/get-session",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetSessionResponse200Type0 | None | GetSessionResponse400 | GetSessionResponse401 | GetSessionResponse403 | GetSessionResponse404 | GetSessionResponse429 | GetSessionResponse500 | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> GetSessionResponse200Type0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = GetSessionResponse200Type0.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSessionResponse200Type0 | None, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetSessionResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetSessionResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetSessionResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetSessionResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GetSessionResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GetSessionResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetSessionResponse200Type0 | None | GetSessionResponse400 | GetSessionResponse401 | GetSessionResponse403 | GetSessionResponse404 | GetSessionResponse429 | GetSessionResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetSessionResponse200Type0 | None | GetSessionResponse400 | GetSessionResponse401 | GetSessionResponse403 | GetSessionResponse404 | GetSessionResponse429 | GetSessionResponse500]:
    """  Get the current session

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSessionResponse200Type0 | None | GetSessionResponse400 | GetSessionResponse401 | GetSessionResponse403 | GetSessionResponse404 | GetSessionResponse429 | GetSessionResponse500]
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

) -> GetSessionResponse200Type0 | None | GetSessionResponse400 | GetSessionResponse401 | GetSessionResponse403 | GetSessionResponse404 | GetSessionResponse429 | GetSessionResponse500 | None:
    """  Get the current session

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSessionResponse200Type0 | None | GetSessionResponse400 | GetSessionResponse401 | GetSessionResponse403 | GetSessionResponse404 | GetSessionResponse429 | GetSessionResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetSessionResponse200Type0 | None | GetSessionResponse400 | GetSessionResponse401 | GetSessionResponse403 | GetSessionResponse404 | GetSessionResponse429 | GetSessionResponse500]:
    """  Get the current session

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSessionResponse200Type0 | None | GetSessionResponse400 | GetSessionResponse401 | GetSessionResponse403 | GetSessionResponse404 | GetSessionResponse429 | GetSessionResponse500]
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

) -> GetSessionResponse200Type0 | None | GetSessionResponse400 | GetSessionResponse401 | GetSessionResponse403 | GetSessionResponse404 | GetSessionResponse429 | GetSessionResponse500 | None:
    """  Get the current session

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSessionResponse200Type0 | None | GetSessionResponse400 | GetSessionResponse401 | GetSessionResponse403 | GetSessionResponse404 | GetSessionResponse429 | GetSessionResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
