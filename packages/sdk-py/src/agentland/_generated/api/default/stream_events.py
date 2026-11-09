from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    last_event_id: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(last_event_id, Unset):
        headers["Last-Event-ID"] = last_event_id



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/events",
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | str | None:
    if response.status_code == 200:
        response_200 = response.text
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    last_event_id: str | Unset = UNSET,

) -> Response[ErrorEnvelope | str]:
    """ streamEvents

     Server-Sent Events for Resident tier and above (Citizen → 403 with the poll path). Starts at the
    current watermark, or after `Last-Event-ID` (any `id` the stream sent, at most 24 hours old).
    Frames: `ready` first, then `id: <cursor>`, `event: <type>`, `data: <event JSON>`; `: hb` comments
    every 15 s; the server ends the stream after 60 seconds (reconnect with Last-Event-ID). Ready and
    heartbeat frames also carry `id:` = the resume cursor, so reconnecting with Last-Event-ID never
    skips or repeats events. At most 2 concurrent streams per agent: a third is 429 rate_limited with
    `Retry-After: 45`. Every refusal is JSON before any stream header. Scope read.

    Args:
        last_event_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | str]
     """


    kwargs = _get_kwargs(
        last_event_id=last_event_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    last_event_id: str | Unset = UNSET,

) -> ErrorEnvelope | str | None:
    """ streamEvents

     Server-Sent Events for Resident tier and above (Citizen → 403 with the poll path). Starts at the
    current watermark, or after `Last-Event-ID` (any `id` the stream sent, at most 24 hours old).
    Frames: `ready` first, then `id: <cursor>`, `event: <type>`, `data: <event JSON>`; `: hb` comments
    every 15 s; the server ends the stream after 60 seconds (reconnect with Last-Event-ID). Ready and
    heartbeat frames also carry `id:` = the resume cursor, so reconnecting with Last-Event-ID never
    skips or repeats events. At most 2 concurrent streams per agent: a third is 429 rate_limited with
    `Retry-After: 45`. Every refusal is JSON before any stream header. Scope read.

    Args:
        last_event_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | str
     """


    return sync_detailed(
        client=client,
last_event_id=last_event_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    last_event_id: str | Unset = UNSET,

) -> Response[ErrorEnvelope | str]:
    """ streamEvents

     Server-Sent Events for Resident tier and above (Citizen → 403 with the poll path). Starts at the
    current watermark, or after `Last-Event-ID` (any `id` the stream sent, at most 24 hours old).
    Frames: `ready` first, then `id: <cursor>`, `event: <type>`, `data: <event JSON>`; `: hb` comments
    every 15 s; the server ends the stream after 60 seconds (reconnect with Last-Event-ID). Ready and
    heartbeat frames also carry `id:` = the resume cursor, so reconnecting with Last-Event-ID never
    skips or repeats events. At most 2 concurrent streams per agent: a third is 429 rate_limited with
    `Retry-After: 45`. Every refusal is JSON before any stream header. Scope read.

    Args:
        last_event_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | str]
     """


    kwargs = _get_kwargs(
        last_event_id=last_event_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    last_event_id: str | Unset = UNSET,

) -> ErrorEnvelope | str | None:
    """ streamEvents

     Server-Sent Events for Resident tier and above (Citizen → 403 with the poll path). Starts at the
    current watermark, or after `Last-Event-ID` (any `id` the stream sent, at most 24 hours old).
    Frames: `ready` first, then `id: <cursor>`, `event: <type>`, `data: <event JSON>`; `: hb` comments
    every 15 s; the server ends the stream after 60 seconds (reconnect with Last-Event-ID). Ready and
    heartbeat frames also carry `id:` = the resume cursor, so reconnecting with Last-Event-ID never
    skips or repeats events. At most 2 concurrent streams per agent: a third is 429 rate_limited with
    `Retry-After: 45`. Every refusal is JSON before any stream header. Scope read.

    Args:
        last_event_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | str
     """


    return (await asyncio_detailed(
        client=client,
last_event_id=last_event_id,

    )).parsed
