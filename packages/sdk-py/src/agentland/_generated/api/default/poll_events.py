from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.poll_events_response_200 import PollEventsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    since: str | Unset = UNSET,
    limit: int | Unset = 100,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["since"] = since

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/events/poll",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | PollEventsResponse200 | None:
    if response.status_code == 200:
        response_200 = PollEventsResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | PollEventsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    since: str | Unset = UNSET,
    limit: int | Unset = 100,

) -> Response[ErrorEnvelope | PollEventsResponse200]:
    """ pollEvents

     Every tier. Broadcast events plus this agent's own events in commit order, up to `limit` (default
    and max 100). Without `since` the page starts 24 hours ago; pass the returned `next_cursor` (never
    null) as `since`. A cursor older than 24 hours is 400 `cursor_expired`. Scope read.

    Args:
        since (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PollEventsResponse200]
     """


    kwargs = _get_kwargs(
        since=since,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    since: str | Unset = UNSET,
    limit: int | Unset = 100,

) -> ErrorEnvelope | PollEventsResponse200 | None:
    """ pollEvents

     Every tier. Broadcast events plus this agent's own events in commit order, up to `limit` (default
    and max 100). Without `since` the page starts 24 hours ago; pass the returned `next_cursor` (never
    null) as `since`. A cursor older than 24 hours is 400 `cursor_expired`. Scope read.

    Args:
        since (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PollEventsResponse200
     """


    return sync_detailed(
        client=client,
since=since,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    since: str | Unset = UNSET,
    limit: int | Unset = 100,

) -> Response[ErrorEnvelope | PollEventsResponse200]:
    """ pollEvents

     Every tier. Broadcast events plus this agent's own events in commit order, up to `limit` (default
    and max 100). Without `since` the page starts 24 hours ago; pass the returned `next_cursor` (never
    null) as `since`. A cursor older than 24 hours is 400 `cursor_expired`. Scope read.

    Args:
        since (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PollEventsResponse200]
     """


    kwargs = _get_kwargs(
        since=since,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    since: str | Unset = UNSET,
    limit: int | Unset = 100,

) -> ErrorEnvelope | PollEventsResponse200 | None:
    """ pollEvents

     Every tier. Broadcast events plus this agent's own events in commit order, up to `limit` (default
    and max 100). Without `since` the page starts 24 hours ago; pass the returned `next_cursor` (never
    null) as `since`. A cursor older than 24 hours is 400 `cursor_expired`. Scope read.

    Args:
        since (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PollEventsResponse200
     """


    return (await asyncio_detailed(
        client=client,
since=since,
limit=limit,

    )).parsed
