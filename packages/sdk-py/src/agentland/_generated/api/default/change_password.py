from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.change_password_body import ChangePasswordBody
from ...models.change_password_response_200 import ChangePasswordResponse200
from ...models.change_password_response_400 import ChangePasswordResponse400
from ...models.change_password_response_401 import ChangePasswordResponse401
from ...models.change_password_response_403 import ChangePasswordResponse403
from ...models.change_password_response_404 import ChangePasswordResponse404
from ...models.change_password_response_429 import ChangePasswordResponse429
from ...models.change_password_response_500 import ChangePasswordResponse500
from typing import cast



def _get_kwargs(
    *,
    body: ChangePasswordBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/change-password",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChangePasswordResponse200 | ChangePasswordResponse400 | ChangePasswordResponse401 | ChangePasswordResponse403 | ChangePasswordResponse404 | ChangePasswordResponse429 | ChangePasswordResponse500 | None:
    if response.status_code == 200:
        response_200 = ChangePasswordResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ChangePasswordResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ChangePasswordResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ChangePasswordResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ChangePasswordResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = ChangePasswordResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = ChangePasswordResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChangePasswordResponse200 | ChangePasswordResponse400 | ChangePasswordResponse401 | ChangePasswordResponse403 | ChangePasswordResponse404 | ChangePasswordResponse429 | ChangePasswordResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ChangePasswordBody,

) -> Response[ChangePasswordResponse200 | ChangePasswordResponse400 | ChangePasswordResponse401 | ChangePasswordResponse403 | ChangePasswordResponse404 | ChangePasswordResponse429 | ChangePasswordResponse500]:
    """  Change the password of the user

    Args:
        body (ChangePasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangePasswordResponse200 | ChangePasswordResponse400 | ChangePasswordResponse401 | ChangePasswordResponse403 | ChangePasswordResponse404 | ChangePasswordResponse429 | ChangePasswordResponse500]
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
    body: ChangePasswordBody,

) -> ChangePasswordResponse200 | ChangePasswordResponse400 | ChangePasswordResponse401 | ChangePasswordResponse403 | ChangePasswordResponse404 | ChangePasswordResponse429 | ChangePasswordResponse500 | None:
    """  Change the password of the user

    Args:
        body (ChangePasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangePasswordResponse200 | ChangePasswordResponse400 | ChangePasswordResponse401 | ChangePasswordResponse403 | ChangePasswordResponse404 | ChangePasswordResponse429 | ChangePasswordResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ChangePasswordBody,

) -> Response[ChangePasswordResponse200 | ChangePasswordResponse400 | ChangePasswordResponse401 | ChangePasswordResponse403 | ChangePasswordResponse404 | ChangePasswordResponse429 | ChangePasswordResponse500]:
    """  Change the password of the user

    Args:
        body (ChangePasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangePasswordResponse200 | ChangePasswordResponse400 | ChangePasswordResponse401 | ChangePasswordResponse403 | ChangePasswordResponse404 | ChangePasswordResponse429 | ChangePasswordResponse500]
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
    body: ChangePasswordBody,

) -> ChangePasswordResponse200 | ChangePasswordResponse400 | ChangePasswordResponse401 | ChangePasswordResponse403 | ChangePasswordResponse404 | ChangePasswordResponse429 | ChangePasswordResponse500 | None:
    """  Change the password of the user

    Args:
        body (ChangePasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangePasswordResponse200 | ChangePasswordResponse400 | ChangePasswordResponse401 | ChangePasswordResponse403 | ChangePasswordResponse404 | ChangePasswordResponse429 | ChangePasswordResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
