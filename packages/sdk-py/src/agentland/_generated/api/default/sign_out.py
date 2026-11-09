from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.sign_out_body import SignOutBody
from ...models.sign_out_response_200 import SignOutResponse200
from ...models.sign_out_response_400 import SignOutResponse400
from ...models.sign_out_response_401 import SignOutResponse401
from ...models.sign_out_response_403 import SignOutResponse403
from ...models.sign_out_response_404 import SignOutResponse404
from ...models.sign_out_response_429 import SignOutResponse429
from ...models.sign_out_response_500 import SignOutResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SignOutBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/sign-out",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SignOutResponse200 | SignOutResponse400 | SignOutResponse401 | SignOutResponse403 | SignOutResponse404 | SignOutResponse429 | SignOutResponse500 | None:
    if response.status_code == 200:
        response_200 = SignOutResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = SignOutResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = SignOutResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = SignOutResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = SignOutResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = SignOutResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = SignOutResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SignOutResponse200 | SignOutResponse400 | SignOutResponse401 | SignOutResponse403 | SignOutResponse404 | SignOutResponse429 | SignOutResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SignOutBody | Unset = UNSET,

) -> Response[SignOutResponse200 | SignOutResponse400 | SignOutResponse401 | SignOutResponse403 | SignOutResponse404 | SignOutResponse429 | SignOutResponse500]:
    """  Sign out the current user

    Args:
        body (SignOutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SignOutResponse200 | SignOutResponse400 | SignOutResponse401 | SignOutResponse403 | SignOutResponse404 | SignOutResponse429 | SignOutResponse500]
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
    body: SignOutBody | Unset = UNSET,

) -> SignOutResponse200 | SignOutResponse400 | SignOutResponse401 | SignOutResponse403 | SignOutResponse404 | SignOutResponse429 | SignOutResponse500 | None:
    """  Sign out the current user

    Args:
        body (SignOutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SignOutResponse200 | SignOutResponse400 | SignOutResponse401 | SignOutResponse403 | SignOutResponse404 | SignOutResponse429 | SignOutResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SignOutBody | Unset = UNSET,

) -> Response[SignOutResponse200 | SignOutResponse400 | SignOutResponse401 | SignOutResponse403 | SignOutResponse404 | SignOutResponse429 | SignOutResponse500]:
    """  Sign out the current user

    Args:
        body (SignOutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SignOutResponse200 | SignOutResponse400 | SignOutResponse401 | SignOutResponse403 | SignOutResponse404 | SignOutResponse429 | SignOutResponse500]
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
    body: SignOutBody | Unset = UNSET,

) -> SignOutResponse200 | SignOutResponse400 | SignOutResponse401 | SignOutResponse403 | SignOutResponse404 | SignOutResponse429 | SignOutResponse500 | None:
    """  Sign out the current user

    Args:
        body (SignOutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SignOutResponse200 | SignOutResponse400 | SignOutResponse401 | SignOutResponse403 | SignOutResponse404 | SignOutResponse429 | SignOutResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
