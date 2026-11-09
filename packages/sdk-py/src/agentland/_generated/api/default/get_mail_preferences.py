from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.get_mail_preferences_response_200 import GetMailPreferencesResponse200
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/op/v1/mail-preferences",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | GetMailPreferencesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetMailPreferencesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())



        return response_409

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = ErrorEnvelope.from_dict(response.json())



        return response_500

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | GetMailPreferencesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[ErrorEnvelope | GetMailPreferencesResponse200]:
    """ getMailPreferences

     The operator's retention mail preferences (D-48); an absent row is the defaults (Season Notes off,
    report card, inactivity nudge and season summary on). `can_edit` is true for an owner or admin
    session. Security, billing and identity notices are never preference-gated. Any operator role; `no-
    store`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetMailPreferencesResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> ErrorEnvelope | GetMailPreferencesResponse200 | None:
    """ getMailPreferences

     The operator's retention mail preferences (D-48); an absent row is the defaults (Season Notes off,
    report card, inactivity nudge and season summary on). `can_edit` is true for an owner or admin
    session. Security, billing and identity notices are never preference-gated. Any operator role; `no-
    store`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetMailPreferencesResponse200
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[ErrorEnvelope | GetMailPreferencesResponse200]:
    """ getMailPreferences

     The operator's retention mail preferences (D-48); an absent row is the defaults (Season Notes off,
    report card, inactivity nudge and season summary on). `can_edit` is true for an owner or admin
    session. Security, billing and identity notices are never preference-gated. Any operator role; `no-
    store`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetMailPreferencesResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> ErrorEnvelope | GetMailPreferencesResponse200 | None:
    """ getMailPreferences

     The operator's retention mail preferences (D-48); an absent row is the defaults (Season Notes off,
    report card, inactivity nudge and season summary on). `can_edit` is true for an owner or admin
    session. Security, billing and identity notices are never preference-gated. Any operator role; `no-
    store`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetMailPreferencesResponse200
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
