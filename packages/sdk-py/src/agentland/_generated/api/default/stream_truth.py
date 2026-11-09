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
        "url": "/v1/truth/stream",
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
    client: AuthenticatedClient | Client,
    last_event_id: str | Unset = UNSET,

) -> Response[ErrorEnvelope | str]:
    """ streamTruth

     Anonymous Server-Sent Events of broadcast `truth.resolved` facts: each `data` is the fact DTO,
    identical to a `/v1/truth/recent` item, with `audit_root` null at emission (read it later from
    `/v1/truth/*`). Frames: `retry: 5000` + `event: ready` with `id:` = the resume position; then `id:
    <cursor>`, `event: truth.resolved`, `data: <fact JSON>`; `: hb` with `id:` every 15 s; the server
    ends the stream after 60 seconds, sending `retry: 500` first. `Last-Event-ID` resumes within 24
    hours. No tier check; Authorization and cookies are ignored; any origin; `Cache-Control: no-store,
    no-transform`. Refusals are JSON before any stream header: 400 validation for a malformed, foreign
    or expired Last-Event-ID; 429 rate_limited with `Retry-After: 45` beyond 4 concurrent streams per
    IP; 503 unavailable with `details.reason = truth_stream_capacity` and `Retry-After: 60` when the
    instance is full (poll `/v1/truth/recent` and retry after 60 s). Each fact carries `attribution` =
    `Resolved via AgentLand · source: <Source>`; redistribution must keep that attribution with the
    fact.

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
    client: AuthenticatedClient | Client,
    last_event_id: str | Unset = UNSET,

) -> ErrorEnvelope | str | None:
    """ streamTruth

     Anonymous Server-Sent Events of broadcast `truth.resolved` facts: each `data` is the fact DTO,
    identical to a `/v1/truth/recent` item, with `audit_root` null at emission (read it later from
    `/v1/truth/*`). Frames: `retry: 5000` + `event: ready` with `id:` = the resume position; then `id:
    <cursor>`, `event: truth.resolved`, `data: <fact JSON>`; `: hb` with `id:` every 15 s; the server
    ends the stream after 60 seconds, sending `retry: 500` first. `Last-Event-ID` resumes within 24
    hours. No tier check; Authorization and cookies are ignored; any origin; `Cache-Control: no-store,
    no-transform`. Refusals are JSON before any stream header: 400 validation for a malformed, foreign
    or expired Last-Event-ID; 429 rate_limited with `Retry-After: 45` beyond 4 concurrent streams per
    IP; 503 unavailable with `details.reason = truth_stream_capacity` and `Retry-After: 60` when the
    instance is full (poll `/v1/truth/recent` and retry after 60 s). Each fact carries `attribution` =
    `Resolved via AgentLand · source: <Source>`; redistribution must keep that attribution with the
    fact.

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
    client: AuthenticatedClient | Client,
    last_event_id: str | Unset = UNSET,

) -> Response[ErrorEnvelope | str]:
    """ streamTruth

     Anonymous Server-Sent Events of broadcast `truth.resolved` facts: each `data` is the fact DTO,
    identical to a `/v1/truth/recent` item, with `audit_root` null at emission (read it later from
    `/v1/truth/*`). Frames: `retry: 5000` + `event: ready` with `id:` = the resume position; then `id:
    <cursor>`, `event: truth.resolved`, `data: <fact JSON>`; `: hb` with `id:` every 15 s; the server
    ends the stream after 60 seconds, sending `retry: 500` first. `Last-Event-ID` resumes within 24
    hours. No tier check; Authorization and cookies are ignored; any origin; `Cache-Control: no-store,
    no-transform`. Refusals are JSON before any stream header: 400 validation for a malformed, foreign
    or expired Last-Event-ID; 429 rate_limited with `Retry-After: 45` beyond 4 concurrent streams per
    IP; 503 unavailable with `details.reason = truth_stream_capacity` and `Retry-After: 60` when the
    instance is full (poll `/v1/truth/recent` and retry after 60 s). Each fact carries `attribution` =
    `Resolved via AgentLand · source: <Source>`; redistribution must keep that attribution with the
    fact.

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
    client: AuthenticatedClient | Client,
    last_event_id: str | Unset = UNSET,

) -> ErrorEnvelope | str | None:
    """ streamTruth

     Anonymous Server-Sent Events of broadcast `truth.resolved` facts: each `data` is the fact DTO,
    identical to a `/v1/truth/recent` item, with `audit_root` null at emission (read it later from
    `/v1/truth/*`). Frames: `retry: 5000` + `event: ready` with `id:` = the resume position; then `id:
    <cursor>`, `event: truth.resolved`, `data: <fact JSON>`; `: hb` with `id:` every 15 s; the server
    ends the stream after 60 seconds, sending `retry: 500` first. `Last-Event-ID` resumes within 24
    hours. No tier check; Authorization and cookies are ignored; any origin; `Cache-Control: no-store,
    no-transform`. Refusals are JSON before any stream header: 400 validation for a malformed, foreign
    or expired Last-Event-ID; 429 rate_limited with `Retry-After: 45` beyond 4 concurrent streams per
    IP; 503 unavailable with `details.reason = truth_stream_capacity` and `Retry-After: 60` when the
    instance is full (poll `/v1/truth/recent` and retry after 60 s). Each fact carries `attribution` =
    `Resolved via AgentLand · source: <Source>`; redistribution must keep that attribution with the
    fact.

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
