from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.sign_in_email_body import SignInEmailBody
from ...models.sign_in_email_response_200 import SignInEmailResponse200
from ...models.sign_in_email_response_400 import SignInEmailResponse400
from ...models.sign_in_email_response_401 import SignInEmailResponse401
from ...models.sign_in_email_response_403 import SignInEmailResponse403
from ...models.sign_in_email_response_404 import SignInEmailResponse404
from ...models.sign_in_email_response_429 import SignInEmailResponse429
from ...models.sign_in_email_response_500 import SignInEmailResponse500
from typing import cast



def _get_kwargs(
    *,
    body: SignInEmailBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/sign-in/email",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SignInEmailResponse200 | SignInEmailResponse400 | SignInEmailResponse401 | SignInEmailResponse403 | SignInEmailResponse404 | SignInEmailResponse429 | SignInEmailResponse500 | None:
    if response.status_code == 200:
        response_200 = SignInEmailResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = SignInEmailResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = SignInEmailResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = SignInEmailResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = SignInEmailResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = SignInEmailResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = SignInEmailResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SignInEmailResponse200 | SignInEmailResponse400 | SignInEmailResponse401 | SignInEmailResponse403 | SignInEmailResponse404 | SignInEmailResponse429 | SignInEmailResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SignInEmailBody,

) -> Response[SignInEmailResponse200 | SignInEmailResponse400 | SignInEmailResponse401 | SignInEmailResponse403 | SignInEmailResponse404 | SignInEmailResponse429 | SignInEmailResponse500]:
    """  Sign in with email and password

    Args:
        body (SignInEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SignInEmailResponse200 | SignInEmailResponse400 | SignInEmailResponse401 | SignInEmailResponse403 | SignInEmailResponse404 | SignInEmailResponse429 | SignInEmailResponse500]
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
    client: AuthenticatedClient | Client,
    body: SignInEmailBody,

) -> SignInEmailResponse200 | SignInEmailResponse400 | SignInEmailResponse401 | SignInEmailResponse403 | SignInEmailResponse404 | SignInEmailResponse429 | SignInEmailResponse500 | None:
    """  Sign in with email and password

    Args:
        body (SignInEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SignInEmailResponse200 | SignInEmailResponse400 | SignInEmailResponse401 | SignInEmailResponse403 | SignInEmailResponse404 | SignInEmailResponse429 | SignInEmailResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SignInEmailBody,

) -> Response[SignInEmailResponse200 | SignInEmailResponse400 | SignInEmailResponse401 | SignInEmailResponse403 | SignInEmailResponse404 | SignInEmailResponse429 | SignInEmailResponse500]:
    """  Sign in with email and password

    Args:
        body (SignInEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SignInEmailResponse200 | SignInEmailResponse400 | SignInEmailResponse401 | SignInEmailResponse403 | SignInEmailResponse404 | SignInEmailResponse429 | SignInEmailResponse500]
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
    client: AuthenticatedClient | Client,
    body: SignInEmailBody,

) -> SignInEmailResponse200 | SignInEmailResponse400 | SignInEmailResponse401 | SignInEmailResponse403 | SignInEmailResponse404 | SignInEmailResponse429 | SignInEmailResponse500 | None:
    """  Sign in with email and password

    Args:
        body (SignInEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SignInEmailResponse200 | SignInEmailResponse400 | SignInEmailResponse401 | SignInEmailResponse403 | SignInEmailResponse404 | SignInEmailResponse429 | SignInEmailResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
