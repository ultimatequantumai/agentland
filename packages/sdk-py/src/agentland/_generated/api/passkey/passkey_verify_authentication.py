from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.passkey_verify_authentication_body import PasskeyVerifyAuthenticationBody
from ...models.passkey_verify_authentication_response_200 import PasskeyVerifyAuthenticationResponse200
from ...models.passkey_verify_authentication_response_400 import PasskeyVerifyAuthenticationResponse400
from ...models.passkey_verify_authentication_response_401 import PasskeyVerifyAuthenticationResponse401
from ...models.passkey_verify_authentication_response_403 import PasskeyVerifyAuthenticationResponse403
from ...models.passkey_verify_authentication_response_404 import PasskeyVerifyAuthenticationResponse404
from ...models.passkey_verify_authentication_response_429 import PasskeyVerifyAuthenticationResponse429
from ...models.passkey_verify_authentication_response_500 import PasskeyVerifyAuthenticationResponse500
from typing import cast



def _get_kwargs(
    *,
    body: PasskeyVerifyAuthenticationBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/passkey/verify-authentication",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PasskeyVerifyAuthenticationResponse200 | PasskeyVerifyAuthenticationResponse400 | PasskeyVerifyAuthenticationResponse401 | PasskeyVerifyAuthenticationResponse403 | PasskeyVerifyAuthenticationResponse404 | PasskeyVerifyAuthenticationResponse429 | PasskeyVerifyAuthenticationResponse500 | None:
    if response.status_code == 200:
        response_200 = PasskeyVerifyAuthenticationResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PasskeyVerifyAuthenticationResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PasskeyVerifyAuthenticationResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PasskeyVerifyAuthenticationResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PasskeyVerifyAuthenticationResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = PasskeyVerifyAuthenticationResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = PasskeyVerifyAuthenticationResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PasskeyVerifyAuthenticationResponse200 | PasskeyVerifyAuthenticationResponse400 | PasskeyVerifyAuthenticationResponse401 | PasskeyVerifyAuthenticationResponse403 | PasskeyVerifyAuthenticationResponse404 | PasskeyVerifyAuthenticationResponse429 | PasskeyVerifyAuthenticationResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PasskeyVerifyAuthenticationBody,

) -> Response[PasskeyVerifyAuthenticationResponse200 | PasskeyVerifyAuthenticationResponse400 | PasskeyVerifyAuthenticationResponse401 | PasskeyVerifyAuthenticationResponse403 | PasskeyVerifyAuthenticationResponse404 | PasskeyVerifyAuthenticationResponse429 | PasskeyVerifyAuthenticationResponse500]:
    """  Verify authentication of a passkey

    Args:
        body (PasskeyVerifyAuthenticationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PasskeyVerifyAuthenticationResponse200 | PasskeyVerifyAuthenticationResponse400 | PasskeyVerifyAuthenticationResponse401 | PasskeyVerifyAuthenticationResponse403 | PasskeyVerifyAuthenticationResponse404 | PasskeyVerifyAuthenticationResponse429 | PasskeyVerifyAuthenticationResponse500]
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
    body: PasskeyVerifyAuthenticationBody,

) -> PasskeyVerifyAuthenticationResponse200 | PasskeyVerifyAuthenticationResponse400 | PasskeyVerifyAuthenticationResponse401 | PasskeyVerifyAuthenticationResponse403 | PasskeyVerifyAuthenticationResponse404 | PasskeyVerifyAuthenticationResponse429 | PasskeyVerifyAuthenticationResponse500 | None:
    """  Verify authentication of a passkey

    Args:
        body (PasskeyVerifyAuthenticationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PasskeyVerifyAuthenticationResponse200 | PasskeyVerifyAuthenticationResponse400 | PasskeyVerifyAuthenticationResponse401 | PasskeyVerifyAuthenticationResponse403 | PasskeyVerifyAuthenticationResponse404 | PasskeyVerifyAuthenticationResponse429 | PasskeyVerifyAuthenticationResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PasskeyVerifyAuthenticationBody,

) -> Response[PasskeyVerifyAuthenticationResponse200 | PasskeyVerifyAuthenticationResponse400 | PasskeyVerifyAuthenticationResponse401 | PasskeyVerifyAuthenticationResponse403 | PasskeyVerifyAuthenticationResponse404 | PasskeyVerifyAuthenticationResponse429 | PasskeyVerifyAuthenticationResponse500]:
    """  Verify authentication of a passkey

    Args:
        body (PasskeyVerifyAuthenticationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PasskeyVerifyAuthenticationResponse200 | PasskeyVerifyAuthenticationResponse400 | PasskeyVerifyAuthenticationResponse401 | PasskeyVerifyAuthenticationResponse403 | PasskeyVerifyAuthenticationResponse404 | PasskeyVerifyAuthenticationResponse429 | PasskeyVerifyAuthenticationResponse500]
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
    body: PasskeyVerifyAuthenticationBody,

) -> PasskeyVerifyAuthenticationResponse200 | PasskeyVerifyAuthenticationResponse400 | PasskeyVerifyAuthenticationResponse401 | PasskeyVerifyAuthenticationResponse403 | PasskeyVerifyAuthenticationResponse404 | PasskeyVerifyAuthenticationResponse429 | PasskeyVerifyAuthenticationResponse500 | None:
    """  Verify authentication of a passkey

    Args:
        body (PasskeyVerifyAuthenticationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PasskeyVerifyAuthenticationResponse200 | PasskeyVerifyAuthenticationResponse400 | PasskeyVerifyAuthenticationResponse401 | PasskeyVerifyAuthenticationResponse403 | PasskeyVerifyAuthenticationResponse404 | PasskeyVerifyAuthenticationResponse429 | PasskeyVerifyAuthenticationResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
