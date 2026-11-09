from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_session_post_body import GetSessionPostBody
from ...models.get_session_post_response_200_type_0 import GetSessionPostResponse200Type0
from ...models.get_session_post_response_400 import GetSessionPostResponse400
from ...models.get_session_post_response_401 import GetSessionPostResponse401
from ...models.get_session_post_response_403 import GetSessionPostResponse403
from ...models.get_session_post_response_404 import GetSessionPostResponse404
from ...models.get_session_post_response_429 import GetSessionPostResponse429
from ...models.get_session_post_response_500 import GetSessionPostResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: GetSessionPostBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/get-session",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetSessionPostResponse200Type0 | None | GetSessionPostResponse400 | GetSessionPostResponse401 | GetSessionPostResponse403 | GetSessionPostResponse404 | GetSessionPostResponse429 | GetSessionPostResponse500 | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> GetSessionPostResponse200Type0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = GetSessionPostResponse200Type0.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSessionPostResponse200Type0 | None, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetSessionPostResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetSessionPostResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetSessionPostResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetSessionPostResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GetSessionPostResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GetSessionPostResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetSessionPostResponse200Type0 | None | GetSessionPostResponse400 | GetSessionPostResponse401 | GetSessionPostResponse403 | GetSessionPostResponse404 | GetSessionPostResponse429 | GetSessionPostResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GetSessionPostBody | Unset = UNSET,

) -> Response[GetSessionPostResponse200Type0 | None | GetSessionPostResponse400 | GetSessionPostResponse401 | GetSessionPostResponse403 | GetSessionPostResponse404 | GetSessionPostResponse429 | GetSessionPostResponse500]:
    """  Get the current session

    Args:
        body (GetSessionPostBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSessionPostResponse200Type0 | None | GetSessionPostResponse400 | GetSessionPostResponse401 | GetSessionPostResponse403 | GetSessionPostResponse404 | GetSessionPostResponse429 | GetSessionPostResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: GetSessionPostBody | Unset = UNSET,

) -> GetSessionPostResponse200Type0 | None | GetSessionPostResponse400 | GetSessionPostResponse401 | GetSessionPostResponse403 | GetSessionPostResponse404 | GetSessionPostResponse429 | GetSessionPostResponse500 | None:
    """  Get the current session

    Args:
        body (GetSessionPostBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSessionPostResponse200Type0 | None | GetSessionPostResponse400 | GetSessionPostResponse401 | GetSessionPostResponse403 | GetSessionPostResponse404 | GetSessionPostResponse429 | GetSessionPostResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GetSessionPostBody | Unset = UNSET,

) -> Response[GetSessionPostResponse200Type0 | None | GetSessionPostResponse400 | GetSessionPostResponse401 | GetSessionPostResponse403 | GetSessionPostResponse404 | GetSessionPostResponse429 | GetSessionPostResponse500]:
    """  Get the current session

    Args:
        body (GetSessionPostBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSessionPostResponse200Type0 | None | GetSessionPostResponse400 | GetSessionPostResponse401 | GetSessionPostResponse403 | GetSessionPostResponse404 | GetSessionPostResponse429 | GetSessionPostResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GetSessionPostBody | Unset = UNSET,

) -> GetSessionPostResponse200Type0 | None | GetSessionPostResponse400 | GetSessionPostResponse401 | GetSessionPostResponse403 | GetSessionPostResponse404 | GetSessionPostResponse429 | GetSessionPostResponse500 | None:
    """  Get the current session

    Args:
        body (GetSessionPostBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSessionPostResponse200Type0 | None | GetSessionPostResponse400 | GetSessionPostResponse401 | GetSessionPostResponse403 | GetSessionPostResponse404 | GetSessionPostResponse429 | GetSessionPostResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
