from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_api_auth_two_factor_disable_body import PostApiAuthTwoFactorDisableBody
from ...models.post_api_auth_two_factor_disable_response_200 import PostApiAuthTwoFactorDisableResponse200
from ...models.post_api_auth_two_factor_disable_response_400 import PostApiAuthTwoFactorDisableResponse400
from ...models.post_api_auth_two_factor_disable_response_401 import PostApiAuthTwoFactorDisableResponse401
from ...models.post_api_auth_two_factor_disable_response_403 import PostApiAuthTwoFactorDisableResponse403
from ...models.post_api_auth_two_factor_disable_response_404 import PostApiAuthTwoFactorDisableResponse404
from ...models.post_api_auth_two_factor_disable_response_429 import PostApiAuthTwoFactorDisableResponse429
from ...models.post_api_auth_two_factor_disable_response_500 import PostApiAuthTwoFactorDisableResponse500
from typing import cast



def _get_kwargs(
    *,
    body: PostApiAuthTwoFactorDisableBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/two-factor/disable",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostApiAuthTwoFactorDisableResponse200 | PostApiAuthTwoFactorDisableResponse400 | PostApiAuthTwoFactorDisableResponse401 | PostApiAuthTwoFactorDisableResponse403 | PostApiAuthTwoFactorDisableResponse404 | PostApiAuthTwoFactorDisableResponse429 | PostApiAuthTwoFactorDisableResponse500 | None:
    if response.status_code == 200:
        response_200 = PostApiAuthTwoFactorDisableResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthTwoFactorDisableResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthTwoFactorDisableResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthTwoFactorDisableResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthTwoFactorDisableResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthTwoFactorDisableResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthTwoFactorDisableResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostApiAuthTwoFactorDisableResponse200 | PostApiAuthTwoFactorDisableResponse400 | PostApiAuthTwoFactorDisableResponse401 | PostApiAuthTwoFactorDisableResponse403 | PostApiAuthTwoFactorDisableResponse404 | PostApiAuthTwoFactorDisableResponse429 | PostApiAuthTwoFactorDisableResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthTwoFactorDisableBody,

) -> Response[PostApiAuthTwoFactorDisableResponse200 | PostApiAuthTwoFactorDisableResponse400 | PostApiAuthTwoFactorDisableResponse401 | PostApiAuthTwoFactorDisableResponse403 | PostApiAuthTwoFactorDisableResponse404 | PostApiAuthTwoFactorDisableResponse429 | PostApiAuthTwoFactorDisableResponse500]:
    """  Use this endpoint to disable two factor authentication.

    Args:
        body (PostApiAuthTwoFactorDisableBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthTwoFactorDisableResponse200 | PostApiAuthTwoFactorDisableResponse400 | PostApiAuthTwoFactorDisableResponse401 | PostApiAuthTwoFactorDisableResponse403 | PostApiAuthTwoFactorDisableResponse404 | PostApiAuthTwoFactorDisableResponse429 | PostApiAuthTwoFactorDisableResponse500]
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
    body: PostApiAuthTwoFactorDisableBody,

) -> PostApiAuthTwoFactorDisableResponse200 | PostApiAuthTwoFactorDisableResponse400 | PostApiAuthTwoFactorDisableResponse401 | PostApiAuthTwoFactorDisableResponse403 | PostApiAuthTwoFactorDisableResponse404 | PostApiAuthTwoFactorDisableResponse429 | PostApiAuthTwoFactorDisableResponse500 | None:
    """  Use this endpoint to disable two factor authentication.

    Args:
        body (PostApiAuthTwoFactorDisableBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthTwoFactorDisableResponse200 | PostApiAuthTwoFactorDisableResponse400 | PostApiAuthTwoFactorDisableResponse401 | PostApiAuthTwoFactorDisableResponse403 | PostApiAuthTwoFactorDisableResponse404 | PostApiAuthTwoFactorDisableResponse429 | PostApiAuthTwoFactorDisableResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthTwoFactorDisableBody,

) -> Response[PostApiAuthTwoFactorDisableResponse200 | PostApiAuthTwoFactorDisableResponse400 | PostApiAuthTwoFactorDisableResponse401 | PostApiAuthTwoFactorDisableResponse403 | PostApiAuthTwoFactorDisableResponse404 | PostApiAuthTwoFactorDisableResponse429 | PostApiAuthTwoFactorDisableResponse500]:
    """  Use this endpoint to disable two factor authentication.

    Args:
        body (PostApiAuthTwoFactorDisableBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthTwoFactorDisableResponse200 | PostApiAuthTwoFactorDisableResponse400 | PostApiAuthTwoFactorDisableResponse401 | PostApiAuthTwoFactorDisableResponse403 | PostApiAuthTwoFactorDisableResponse404 | PostApiAuthTwoFactorDisableResponse429 | PostApiAuthTwoFactorDisableResponse500]
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
    body: PostApiAuthTwoFactorDisableBody,

) -> PostApiAuthTwoFactorDisableResponse200 | PostApiAuthTwoFactorDisableResponse400 | PostApiAuthTwoFactorDisableResponse401 | PostApiAuthTwoFactorDisableResponse403 | PostApiAuthTwoFactorDisableResponse404 | PostApiAuthTwoFactorDisableResponse429 | PostApiAuthTwoFactorDisableResponse500 | None:
    """  Use this endpoint to disable two factor authentication.

    Args:
        body (PostApiAuthTwoFactorDisableBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthTwoFactorDisableResponse200 | PostApiAuthTwoFactorDisableResponse400 | PostApiAuthTwoFactorDisableResponse401 | PostApiAuthTwoFactorDisableResponse403 | PostApiAuthTwoFactorDisableResponse404 | PostApiAuthTwoFactorDisableResponse429 | PostApiAuthTwoFactorDisableResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
