from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.get_field_replay_response_200 import GetFieldReplayResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    hours: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["hours"] = hours


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/field/replay",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | GetFieldReplayResponse200 | None:
    if response.status_code == 200:
        response_200 = GetFieldReplayResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | GetFieldReplayResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    hours: int | Unset = UNSET,

) -> Response[ErrorEnvelope | GetFieldReplayResponse200]:
    """ getFieldReplay

     One keyframe-partitioned hour of the 24 h ring: rows from the first key in the hour up to the first
    key of a later hour, so every non-empty page starts with a key. Exactly one of `cursor` (hour slot,
    a multiple of 360 inside the ring) or `hours` (1..24, default 24); both are 400. An out-of-ring
    cursor is 400 with `details.reason = cursor_out_of_ring` and the ring's
    `first_cursor`/`last_cursor`. An hour without a key returns `frames: []`. Anonymous and identical
    for every caller, any origin. `Cache-Control: public, max-age=60`; errors no-store; an empty ring is
    503.

    Args:
        cursor (str | Unset): Hour slot (decimal, a multiple of 360) inside the ring
        hours (int | Unset): Start this many hours before the newest row (default 24)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetFieldReplayResponse200]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
hours=hours,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    hours: int | Unset = UNSET,

) -> ErrorEnvelope | GetFieldReplayResponse200 | None:
    """ getFieldReplay

     One keyframe-partitioned hour of the 24 h ring: rows from the first key in the hour up to the first
    key of a later hour, so every non-empty page starts with a key. Exactly one of `cursor` (hour slot,
    a multiple of 360 inside the ring) or `hours` (1..24, default 24); both are 400. An out-of-ring
    cursor is 400 with `details.reason = cursor_out_of_ring` and the ring's
    `first_cursor`/`last_cursor`. An hour without a key returns `frames: []`. Anonymous and identical
    for every caller, any origin. `Cache-Control: public, max-age=60`; errors no-store; an empty ring is
    503.

    Args:
        cursor (str | Unset): Hour slot (decimal, a multiple of 360) inside the ring
        hours (int | Unset): Start this many hours before the newest row (default 24)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetFieldReplayResponse200
     """


    return sync_detailed(
        client=client,
cursor=cursor,
hours=hours,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    hours: int | Unset = UNSET,

) -> Response[ErrorEnvelope | GetFieldReplayResponse200]:
    """ getFieldReplay

     One keyframe-partitioned hour of the 24 h ring: rows from the first key in the hour up to the first
    key of a later hour, so every non-empty page starts with a key. Exactly one of `cursor` (hour slot,
    a multiple of 360 inside the ring) or `hours` (1..24, default 24); both are 400. An out-of-ring
    cursor is 400 with `details.reason = cursor_out_of_ring` and the ring's
    `first_cursor`/`last_cursor`. An hour without a key returns `frames: []`. Anonymous and identical
    for every caller, any origin. `Cache-Control: public, max-age=60`; errors no-store; an empty ring is
    503.

    Args:
        cursor (str | Unset): Hour slot (decimal, a multiple of 360) inside the ring
        hours (int | Unset): Start this many hours before the newest row (default 24)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetFieldReplayResponse200]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
hours=hours,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    hours: int | Unset = UNSET,

) -> ErrorEnvelope | GetFieldReplayResponse200 | None:
    """ getFieldReplay

     One keyframe-partitioned hour of the 24 h ring: rows from the first key in the hour up to the first
    key of a later hour, so every non-empty page starts with a key. Exactly one of `cursor` (hour slot,
    a multiple of 360 inside the ring) or `hours` (1..24, default 24); both are 400. An out-of-ring
    cursor is 400 with `details.reason = cursor_out_of_ring` and the ring's
    `first_cursor`/`last_cursor`. An hour without a key returns `frames: []`. Anonymous and identical
    for every caller, any origin. `Cache-Control: public, max-age=60`; errors no-store; an empty ring is
    503.

    Args:
        cursor (str | Unset): Hour slot (decimal, a multiple of 360) inside the ring
        hours (int | Unset): Start this many hours before the newest row (default 24)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetFieldReplayResponse200
     """


    return (await asyncio_detailed(
        client=client,
cursor=cursor,
hours=hours,

    )).parsed
