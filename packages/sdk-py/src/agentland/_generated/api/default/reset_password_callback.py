from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reset_password_callback_response_200 import ResetPasswordCallbackResponse200
from ...models.reset_password_callback_response_400 import ResetPasswordCallbackResponse400
from ...models.reset_password_callback_response_401 import ResetPasswordCallbackResponse401
from ...models.reset_password_callback_response_403 import ResetPasswordCallbackResponse403
from ...models.reset_password_callback_response_404 import ResetPasswordCallbackResponse404
from ...models.reset_password_callback_response_429 import ResetPasswordCallbackResponse429
from ...models.reset_password_callback_response_500 import ResetPasswordCallbackResponse500
from typing import cast



def _get_kwargs(
    token: str,
    *,
    callback_url: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["callbackURL"] = callback_url


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/reset-password/{token}".format(token=quote(str(token), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ResetPasswordCallbackResponse200 | ResetPasswordCallbackResponse400 | ResetPasswordCallbackResponse401 | ResetPasswordCallbackResponse403 | ResetPasswordCallbackResponse404 | ResetPasswordCallbackResponse429 | ResetPasswordCallbackResponse500 | None:
    if response.status_code == 200:
        response_200 = ResetPasswordCallbackResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ResetPasswordCallbackResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ResetPasswordCallbackResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ResetPasswordCallbackResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ResetPasswordCallbackResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = ResetPasswordCallbackResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = ResetPasswordCallbackResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ResetPasswordCallbackResponse200 | ResetPasswordCallbackResponse400 | ResetPasswordCallbackResponse401 | ResetPasswordCallbackResponse403 | ResetPasswordCallbackResponse404 | ResetPasswordCallbackResponse429 | ResetPasswordCallbackResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    token: str,
    *,
    client: AuthenticatedClient | Client,
    callback_url: str,

) -> Response[ResetPasswordCallbackResponse200 | ResetPasswordCallbackResponse400 | ResetPasswordCallbackResponse401 | ResetPasswordCallbackResponse403 | ResetPasswordCallbackResponse404 | ResetPasswordCallbackResponse429 | ResetPasswordCallbackResponse500]:
    """  Redirects the user to the callback URL with the token

    Args:
        token (str):
        callback_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResetPasswordCallbackResponse200 | ResetPasswordCallbackResponse400 | ResetPasswordCallbackResponse401 | ResetPasswordCallbackResponse403 | ResetPasswordCallbackResponse404 | ResetPasswordCallbackResponse429 | ResetPasswordCallbackResponse500]
     """


    kwargs = _get_kwargs(
        token=token,
callback_url=callback_url,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    token: str,
    *,
    client: AuthenticatedClient | Client,
    callback_url: str,

) -> ResetPasswordCallbackResponse200 | ResetPasswordCallbackResponse400 | ResetPasswordCallbackResponse401 | ResetPasswordCallbackResponse403 | ResetPasswordCallbackResponse404 | ResetPasswordCallbackResponse429 | ResetPasswordCallbackResponse500 | None:
    """  Redirects the user to the callback URL with the token

    Args:
        token (str):
        callback_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResetPasswordCallbackResponse200 | ResetPasswordCallbackResponse400 | ResetPasswordCallbackResponse401 | ResetPasswordCallbackResponse403 | ResetPasswordCallbackResponse404 | ResetPasswordCallbackResponse429 | ResetPasswordCallbackResponse500
     """


    return sync_detailed(
        token=token,
client=client,
callback_url=callback_url,

    ).parsed

async def asyncio_detailed(
    token: str,
    *,
    client: AuthenticatedClient | Client,
    callback_url: str,

) -> Response[ResetPasswordCallbackResponse200 | ResetPasswordCallbackResponse400 | ResetPasswordCallbackResponse401 | ResetPasswordCallbackResponse403 | ResetPasswordCallbackResponse404 | ResetPasswordCallbackResponse429 | ResetPasswordCallbackResponse500]:
    """  Redirects the user to the callback URL with the token

    Args:
        token (str):
        callback_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResetPasswordCallbackResponse200 | ResetPasswordCallbackResponse400 | ResetPasswordCallbackResponse401 | ResetPasswordCallbackResponse403 | ResetPasswordCallbackResponse404 | ResetPasswordCallbackResponse429 | ResetPasswordCallbackResponse500]
     """


    kwargs = _get_kwargs(
        token=token,
callback_url=callback_url,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    token: str,
    *,
    client: AuthenticatedClient | Client,
    callback_url: str,

) -> ResetPasswordCallbackResponse200 | ResetPasswordCallbackResponse400 | ResetPasswordCallbackResponse401 | ResetPasswordCallbackResponse403 | ResetPasswordCallbackResponse404 | ResetPasswordCallbackResponse429 | ResetPasswordCallbackResponse500 | None:
    """  Redirects the user to the callback URL with the token

    Args:
        token (str):
        callback_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResetPasswordCallbackResponse200 | ResetPasswordCallbackResponse400 | ResetPasswordCallbackResponse401 | ResetPasswordCallbackResponse403 | ResetPasswordCallbackResponse404 | ResetPasswordCallbackResponse429 | ResetPasswordCallbackResponse500
     """


    return (await asyncio_detailed(
        token=token,
client=client,
callback_url=callback_url,

    )).parsed
