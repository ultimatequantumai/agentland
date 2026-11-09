from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.verify_password_body import VerifyPasswordBody
from ...models.verify_password_response_200 import VerifyPasswordResponse200
from ...models.verify_password_response_400 import VerifyPasswordResponse400
from ...models.verify_password_response_401 import VerifyPasswordResponse401
from ...models.verify_password_response_403 import VerifyPasswordResponse403
from ...models.verify_password_response_404 import VerifyPasswordResponse404
from ...models.verify_password_response_429 import VerifyPasswordResponse429
from ...models.verify_password_response_500 import VerifyPasswordResponse500
from typing import cast



def _get_kwargs(
    *,
    body: VerifyPasswordBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/verify-password",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> VerifyPasswordResponse200 | VerifyPasswordResponse400 | VerifyPasswordResponse401 | VerifyPasswordResponse403 | VerifyPasswordResponse404 | VerifyPasswordResponse429 | VerifyPasswordResponse500 | None:
    if response.status_code == 200:
        response_200 = VerifyPasswordResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = VerifyPasswordResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = VerifyPasswordResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = VerifyPasswordResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = VerifyPasswordResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = VerifyPasswordResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = VerifyPasswordResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[VerifyPasswordResponse200 | VerifyPasswordResponse400 | VerifyPasswordResponse401 | VerifyPasswordResponse403 | VerifyPasswordResponse404 | VerifyPasswordResponse429 | VerifyPasswordResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: VerifyPasswordBody,

) -> Response[VerifyPasswordResponse200 | VerifyPasswordResponse400 | VerifyPasswordResponse401 | VerifyPasswordResponse403 | VerifyPasswordResponse404 | VerifyPasswordResponse429 | VerifyPasswordResponse500]:
    """  Verify the current user's password

    Args:
        body (VerifyPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VerifyPasswordResponse200 | VerifyPasswordResponse400 | VerifyPasswordResponse401 | VerifyPasswordResponse403 | VerifyPasswordResponse404 | VerifyPasswordResponse429 | VerifyPasswordResponse500]
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
    body: VerifyPasswordBody,

) -> VerifyPasswordResponse200 | VerifyPasswordResponse400 | VerifyPasswordResponse401 | VerifyPasswordResponse403 | VerifyPasswordResponse404 | VerifyPasswordResponse429 | VerifyPasswordResponse500 | None:
    """  Verify the current user's password

    Args:
        body (VerifyPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VerifyPasswordResponse200 | VerifyPasswordResponse400 | VerifyPasswordResponse401 | VerifyPasswordResponse403 | VerifyPasswordResponse404 | VerifyPasswordResponse429 | VerifyPasswordResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: VerifyPasswordBody,

) -> Response[VerifyPasswordResponse200 | VerifyPasswordResponse400 | VerifyPasswordResponse401 | VerifyPasswordResponse403 | VerifyPasswordResponse404 | VerifyPasswordResponse429 | VerifyPasswordResponse500]:
    """  Verify the current user's password

    Args:
        body (VerifyPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VerifyPasswordResponse200 | VerifyPasswordResponse400 | VerifyPasswordResponse401 | VerifyPasswordResponse403 | VerifyPasswordResponse404 | VerifyPasswordResponse429 | VerifyPasswordResponse500]
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
    body: VerifyPasswordBody,

) -> VerifyPasswordResponse200 | VerifyPasswordResponse400 | VerifyPasswordResponse401 | VerifyPasswordResponse403 | VerifyPasswordResponse404 | VerifyPasswordResponse429 | VerifyPasswordResponse500 | None:
    """  Verify the current user's password

    Args:
        body (VerifyPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VerifyPasswordResponse200 | VerifyPasswordResponse400 | VerifyPasswordResponse401 | VerifyPasswordResponse403 | VerifyPasswordResponse404 | VerifyPasswordResponse429 | VerifyPasswordResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
