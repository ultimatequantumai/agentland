from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.generate_passkey_registration_options_authenticator_attachment import GeneratePasskeyRegistrationOptionsAuthenticatorAttachment
from ...models.generate_passkey_registration_options_response_200 import GeneratePasskeyRegistrationOptionsResponse200
from ...models.generate_passkey_registration_options_response_400 import GeneratePasskeyRegistrationOptionsResponse400
from ...models.generate_passkey_registration_options_response_401 import GeneratePasskeyRegistrationOptionsResponse401
from ...models.generate_passkey_registration_options_response_403 import GeneratePasskeyRegistrationOptionsResponse403
from ...models.generate_passkey_registration_options_response_404 import GeneratePasskeyRegistrationOptionsResponse404
from ...models.generate_passkey_registration_options_response_429 import GeneratePasskeyRegistrationOptionsResponse429
from ...models.generate_passkey_registration_options_response_500 import GeneratePasskeyRegistrationOptionsResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    authenticator_attachment: GeneratePasskeyRegistrationOptionsAuthenticatorAttachment | Unset = UNSET,
    name: str | Unset = UNSET,
    context: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_authenticator_attachment: str | Unset = UNSET
    if not isinstance(authenticator_attachment, Unset):
        json_authenticator_attachment = authenticator_attachment.value

    params["authenticatorAttachment"] = json_authenticator_attachment

    params["name"] = name

    params["context"] = context


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/passkey/generate-register-options",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GeneratePasskeyRegistrationOptionsResponse200 | GeneratePasskeyRegistrationOptionsResponse400 | GeneratePasskeyRegistrationOptionsResponse401 | GeneratePasskeyRegistrationOptionsResponse403 | GeneratePasskeyRegistrationOptionsResponse404 | GeneratePasskeyRegistrationOptionsResponse429 | GeneratePasskeyRegistrationOptionsResponse500 | None:
    if response.status_code == 200:
        response_200 = GeneratePasskeyRegistrationOptionsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GeneratePasskeyRegistrationOptionsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GeneratePasskeyRegistrationOptionsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GeneratePasskeyRegistrationOptionsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GeneratePasskeyRegistrationOptionsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GeneratePasskeyRegistrationOptionsResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GeneratePasskeyRegistrationOptionsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GeneratePasskeyRegistrationOptionsResponse200 | GeneratePasskeyRegistrationOptionsResponse400 | GeneratePasskeyRegistrationOptionsResponse401 | GeneratePasskeyRegistrationOptionsResponse403 | GeneratePasskeyRegistrationOptionsResponse404 | GeneratePasskeyRegistrationOptionsResponse429 | GeneratePasskeyRegistrationOptionsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    authenticator_attachment: GeneratePasskeyRegistrationOptionsAuthenticatorAttachment | Unset = UNSET,
    name: str | Unset = UNSET,
    context: str | Unset = UNSET,

) -> Response[GeneratePasskeyRegistrationOptionsResponse200 | GeneratePasskeyRegistrationOptionsResponse400 | GeneratePasskeyRegistrationOptionsResponse401 | GeneratePasskeyRegistrationOptionsResponse403 | GeneratePasskeyRegistrationOptionsResponse404 | GeneratePasskeyRegistrationOptionsResponse429 | GeneratePasskeyRegistrationOptionsResponse500]:
    """  Generate registration options for a new passkey

    Args:
        authenticator_attachment (GeneratePasskeyRegistrationOptionsAuthenticatorAttachment |
            Unset):
        name (str | Unset):
        context (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GeneratePasskeyRegistrationOptionsResponse200 | GeneratePasskeyRegistrationOptionsResponse400 | GeneratePasskeyRegistrationOptionsResponse401 | GeneratePasskeyRegistrationOptionsResponse403 | GeneratePasskeyRegistrationOptionsResponse404 | GeneratePasskeyRegistrationOptionsResponse429 | GeneratePasskeyRegistrationOptionsResponse500]
     """


    kwargs = _get_kwargs(
        authenticator_attachment=authenticator_attachment,
name=name,
context=context,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    authenticator_attachment: GeneratePasskeyRegistrationOptionsAuthenticatorAttachment | Unset = UNSET,
    name: str | Unset = UNSET,
    context: str | Unset = UNSET,

) -> GeneratePasskeyRegistrationOptionsResponse200 | GeneratePasskeyRegistrationOptionsResponse400 | GeneratePasskeyRegistrationOptionsResponse401 | GeneratePasskeyRegistrationOptionsResponse403 | GeneratePasskeyRegistrationOptionsResponse404 | GeneratePasskeyRegistrationOptionsResponse429 | GeneratePasskeyRegistrationOptionsResponse500 | None:
    """  Generate registration options for a new passkey

    Args:
        authenticator_attachment (GeneratePasskeyRegistrationOptionsAuthenticatorAttachment |
            Unset):
        name (str | Unset):
        context (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GeneratePasskeyRegistrationOptionsResponse200 | GeneratePasskeyRegistrationOptionsResponse400 | GeneratePasskeyRegistrationOptionsResponse401 | GeneratePasskeyRegistrationOptionsResponse403 | GeneratePasskeyRegistrationOptionsResponse404 | GeneratePasskeyRegistrationOptionsResponse429 | GeneratePasskeyRegistrationOptionsResponse500
     """


    return sync_detailed(
        client=client,
authenticator_attachment=authenticator_attachment,
name=name,
context=context,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    authenticator_attachment: GeneratePasskeyRegistrationOptionsAuthenticatorAttachment | Unset = UNSET,
    name: str | Unset = UNSET,
    context: str | Unset = UNSET,

) -> Response[GeneratePasskeyRegistrationOptionsResponse200 | GeneratePasskeyRegistrationOptionsResponse400 | GeneratePasskeyRegistrationOptionsResponse401 | GeneratePasskeyRegistrationOptionsResponse403 | GeneratePasskeyRegistrationOptionsResponse404 | GeneratePasskeyRegistrationOptionsResponse429 | GeneratePasskeyRegistrationOptionsResponse500]:
    """  Generate registration options for a new passkey

    Args:
        authenticator_attachment (GeneratePasskeyRegistrationOptionsAuthenticatorAttachment |
            Unset):
        name (str | Unset):
        context (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GeneratePasskeyRegistrationOptionsResponse200 | GeneratePasskeyRegistrationOptionsResponse400 | GeneratePasskeyRegistrationOptionsResponse401 | GeneratePasskeyRegistrationOptionsResponse403 | GeneratePasskeyRegistrationOptionsResponse404 | GeneratePasskeyRegistrationOptionsResponse429 | GeneratePasskeyRegistrationOptionsResponse500]
     """


    kwargs = _get_kwargs(
        authenticator_attachment=authenticator_attachment,
name=name,
context=context,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    authenticator_attachment: GeneratePasskeyRegistrationOptionsAuthenticatorAttachment | Unset = UNSET,
    name: str | Unset = UNSET,
    context: str | Unset = UNSET,

) -> GeneratePasskeyRegistrationOptionsResponse200 | GeneratePasskeyRegistrationOptionsResponse400 | GeneratePasskeyRegistrationOptionsResponse401 | GeneratePasskeyRegistrationOptionsResponse403 | GeneratePasskeyRegistrationOptionsResponse404 | GeneratePasskeyRegistrationOptionsResponse429 | GeneratePasskeyRegistrationOptionsResponse500 | None:
    """  Generate registration options for a new passkey

    Args:
        authenticator_attachment (GeneratePasskeyRegistrationOptionsAuthenticatorAttachment |
            Unset):
        name (str | Unset):
        context (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GeneratePasskeyRegistrationOptionsResponse200 | GeneratePasskeyRegistrationOptionsResponse400 | GeneratePasskeyRegistrationOptionsResponse401 | GeneratePasskeyRegistrationOptionsResponse403 | GeneratePasskeyRegistrationOptionsResponse404 | GeneratePasskeyRegistrationOptionsResponse429 | GeneratePasskeyRegistrationOptionsResponse500
     """


    return (await asyncio_detailed(
        client=client,
authenticator_attachment=authenticator_attachment,
name=name,
context=context,

    )).parsed
