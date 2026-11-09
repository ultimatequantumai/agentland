from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.send_verification_email_body import SendVerificationEmailBody
from ...models.send_verification_email_response_200 import SendVerificationEmailResponse200
from ...models.send_verification_email_response_400 import SendVerificationEmailResponse400
from ...models.send_verification_email_response_401 import SendVerificationEmailResponse401
from ...models.send_verification_email_response_403 import SendVerificationEmailResponse403
from ...models.send_verification_email_response_404 import SendVerificationEmailResponse404
from ...models.send_verification_email_response_429 import SendVerificationEmailResponse429
from ...models.send_verification_email_response_500 import SendVerificationEmailResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SendVerificationEmailBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/send-verification-email",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SendVerificationEmailResponse200 | SendVerificationEmailResponse400 | SendVerificationEmailResponse401 | SendVerificationEmailResponse403 | SendVerificationEmailResponse404 | SendVerificationEmailResponse429 | SendVerificationEmailResponse500 | None:
    if response.status_code == 200:
        response_200 = SendVerificationEmailResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = SendVerificationEmailResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = SendVerificationEmailResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = SendVerificationEmailResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = SendVerificationEmailResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = SendVerificationEmailResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = SendVerificationEmailResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SendVerificationEmailResponse200 | SendVerificationEmailResponse400 | SendVerificationEmailResponse401 | SendVerificationEmailResponse403 | SendVerificationEmailResponse404 | SendVerificationEmailResponse429 | SendVerificationEmailResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SendVerificationEmailBody | Unset = UNSET,

) -> Response[SendVerificationEmailResponse200 | SendVerificationEmailResponse400 | SendVerificationEmailResponse401 | SendVerificationEmailResponse403 | SendVerificationEmailResponse404 | SendVerificationEmailResponse429 | SendVerificationEmailResponse500]:
    """  Send a verification email to the user

    Args:
        body (SendVerificationEmailBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendVerificationEmailResponse200 | SendVerificationEmailResponse400 | SendVerificationEmailResponse401 | SendVerificationEmailResponse403 | SendVerificationEmailResponse404 | SendVerificationEmailResponse429 | SendVerificationEmailResponse500]
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
    body: SendVerificationEmailBody | Unset = UNSET,

) -> SendVerificationEmailResponse200 | SendVerificationEmailResponse400 | SendVerificationEmailResponse401 | SendVerificationEmailResponse403 | SendVerificationEmailResponse404 | SendVerificationEmailResponse429 | SendVerificationEmailResponse500 | None:
    """  Send a verification email to the user

    Args:
        body (SendVerificationEmailBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendVerificationEmailResponse200 | SendVerificationEmailResponse400 | SendVerificationEmailResponse401 | SendVerificationEmailResponse403 | SendVerificationEmailResponse404 | SendVerificationEmailResponse429 | SendVerificationEmailResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SendVerificationEmailBody | Unset = UNSET,

) -> Response[SendVerificationEmailResponse200 | SendVerificationEmailResponse400 | SendVerificationEmailResponse401 | SendVerificationEmailResponse403 | SendVerificationEmailResponse404 | SendVerificationEmailResponse429 | SendVerificationEmailResponse500]:
    """  Send a verification email to the user

    Args:
        body (SendVerificationEmailBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendVerificationEmailResponse200 | SendVerificationEmailResponse400 | SendVerificationEmailResponse401 | SendVerificationEmailResponse403 | SendVerificationEmailResponse404 | SendVerificationEmailResponse429 | SendVerificationEmailResponse500]
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
    body: SendVerificationEmailBody | Unset = UNSET,

) -> SendVerificationEmailResponse200 | SendVerificationEmailResponse400 | SendVerificationEmailResponse401 | SendVerificationEmailResponse403 | SendVerificationEmailResponse404 | SendVerificationEmailResponse429 | SendVerificationEmailResponse500 | None:
    """  Send a verification email to the user

    Args:
        body (SendVerificationEmailBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendVerificationEmailResponse200 | SendVerificationEmailResponse400 | SendVerificationEmailResponse401 | SendVerificationEmailResponse403 | SendVerificationEmailResponse404 | SendVerificationEmailResponse429 | SendVerificationEmailResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
