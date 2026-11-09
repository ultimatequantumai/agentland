from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.update_user_body import UpdateUserBody
from ...models.update_user_response_200 import UpdateUserResponse200
from ...models.update_user_response_400 import UpdateUserResponse400
from ...models.update_user_response_401 import UpdateUserResponse401
from ...models.update_user_response_403 import UpdateUserResponse403
from ...models.update_user_response_404 import UpdateUserResponse404
from ...models.update_user_response_429 import UpdateUserResponse429
from ...models.update_user_response_500 import UpdateUserResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UpdateUserBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/update-user",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdateUserResponse200 | UpdateUserResponse400 | UpdateUserResponse401 | UpdateUserResponse403 | UpdateUserResponse404 | UpdateUserResponse429 | UpdateUserResponse500 | None:
    if response.status_code == 200:
        response_200 = UpdateUserResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = UpdateUserResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UpdateUserResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = UpdateUserResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = UpdateUserResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = UpdateUserResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = UpdateUserResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpdateUserResponse200 | UpdateUserResponse400 | UpdateUserResponse401 | UpdateUserResponse403 | UpdateUserResponse404 | UpdateUserResponse429 | UpdateUserResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateUserBody | Unset = UNSET,

) -> Response[UpdateUserResponse200 | UpdateUserResponse400 | UpdateUserResponse401 | UpdateUserResponse403 | UpdateUserResponse404 | UpdateUserResponse429 | UpdateUserResponse500]:
    """  Update the current user

    Args:
        body (UpdateUserBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateUserResponse200 | UpdateUserResponse400 | UpdateUserResponse401 | UpdateUserResponse403 | UpdateUserResponse404 | UpdateUserResponse429 | UpdateUserResponse500]
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
    body: UpdateUserBody | Unset = UNSET,

) -> UpdateUserResponse200 | UpdateUserResponse400 | UpdateUserResponse401 | UpdateUserResponse403 | UpdateUserResponse404 | UpdateUserResponse429 | UpdateUserResponse500 | None:
    """  Update the current user

    Args:
        body (UpdateUserBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateUserResponse200 | UpdateUserResponse400 | UpdateUserResponse401 | UpdateUserResponse403 | UpdateUserResponse404 | UpdateUserResponse429 | UpdateUserResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateUserBody | Unset = UNSET,

) -> Response[UpdateUserResponse200 | UpdateUserResponse400 | UpdateUserResponse401 | UpdateUserResponse403 | UpdateUserResponse404 | UpdateUserResponse429 | UpdateUserResponse500]:
    """  Update the current user

    Args:
        body (UpdateUserBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateUserResponse200 | UpdateUserResponse400 | UpdateUserResponse401 | UpdateUserResponse403 | UpdateUserResponse404 | UpdateUserResponse429 | UpdateUserResponse500]
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
    body: UpdateUserBody | Unset = UNSET,

) -> UpdateUserResponse200 | UpdateUserResponse400 | UpdateUserResponse401 | UpdateUserResponse403 | UpdateUserResponse404 | UpdateUserResponse429 | UpdateUserResponse500 | None:
    """  Update the current user

    Args:
        body (UpdateUserBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateUserResponse200 | UpdateUserResponse400 | UpdateUserResponse401 | UpdateUserResponse403 | UpdateUserResponse404 | UpdateUserResponse429 | UpdateUserResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
