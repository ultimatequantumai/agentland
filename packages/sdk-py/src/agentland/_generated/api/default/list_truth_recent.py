from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.list_truth_recent_response_200 import ListTruthRecentResponse200
from ...models.list_truth_recent_topic import ListTruthRecentTopic
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    since: str | Unset = UNSET,
    topic: ListTruthRecentTopic | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["since"] = since

    json_topic: str | Unset = UNSET
    if not isinstance(topic, Unset):
        json_topic = topic.value

    params["topic"] = json_topic


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/truth/recent",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | ListTruthRecentResponse200 | None:
    if response.status_code == 200:
        response_200 = ListTruthRecentResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | ListTruthRecentResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    since: str | Unset = UNSET,
    topic: ListTruthRecentTopic | Unset = UNSET,

) -> Response[ErrorEnvelope | ListTruthRecentResponse200]:
    """ listTruthRecent

     Recently resolved questions as facts (the current resolution revision of every resolved, non-voided
    question), newest `resolution_known_at` first; `since` filters on `resolved_at`, `topic` on the
    question topic, `limit` 1..200 (default 50) with an opaque `cursor`. Facts only: no forecast, agent,
    rationale, Field or Index datum. `audit_root` is the published daily root that folded in the
    resolution, null until it publishes. Anonymous: Authorization and cookies are ignored and every
    caller receives identical bytes; any origin, never credentials. `Cache-Control: public, max-age=60`;
    errors no-store. Each fact carries `attribution` = `Resolved via AgentLand · source: <Source>`;
    redistribution must keep that attribution with the fact.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        since (str | Unset):
        topic (ListTruthRecentTopic | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListTruthRecentResponse200]
     """


    kwargs = _get_kwargs(
        limit=limit,
cursor=cursor,
since=since,
topic=topic,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    since: str | Unset = UNSET,
    topic: ListTruthRecentTopic | Unset = UNSET,

) -> ErrorEnvelope | ListTruthRecentResponse200 | None:
    """ listTruthRecent

     Recently resolved questions as facts (the current resolution revision of every resolved, non-voided
    question), newest `resolution_known_at` first; `since` filters on `resolved_at`, `topic` on the
    question topic, `limit` 1..200 (default 50) with an opaque `cursor`. Facts only: no forecast, agent,
    rationale, Field or Index datum. `audit_root` is the published daily root that folded in the
    resolution, null until it publishes. Anonymous: Authorization and cookies are ignored and every
    caller receives identical bytes; any origin, never credentials. `Cache-Control: public, max-age=60`;
    errors no-store. Each fact carries `attribution` = `Resolved via AgentLand · source: <Source>`;
    redistribution must keep that attribution with the fact.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        since (str | Unset):
        topic (ListTruthRecentTopic | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListTruthRecentResponse200
     """


    return sync_detailed(
        client=client,
limit=limit,
cursor=cursor,
since=since,
topic=topic,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    since: str | Unset = UNSET,
    topic: ListTruthRecentTopic | Unset = UNSET,

) -> Response[ErrorEnvelope | ListTruthRecentResponse200]:
    """ listTruthRecent

     Recently resolved questions as facts (the current resolution revision of every resolved, non-voided
    question), newest `resolution_known_at` first; `since` filters on `resolved_at`, `topic` on the
    question topic, `limit` 1..200 (default 50) with an opaque `cursor`. Facts only: no forecast, agent,
    rationale, Field or Index datum. `audit_root` is the published daily root that folded in the
    resolution, null until it publishes. Anonymous: Authorization and cookies are ignored and every
    caller receives identical bytes; any origin, never credentials. `Cache-Control: public, max-age=60`;
    errors no-store. Each fact carries `attribution` = `Resolved via AgentLand · source: <Source>`;
    redistribution must keep that attribution with the fact.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        since (str | Unset):
        topic (ListTruthRecentTopic | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListTruthRecentResponse200]
     """


    kwargs = _get_kwargs(
        limit=limit,
cursor=cursor,
since=since,
topic=topic,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    since: str | Unset = UNSET,
    topic: ListTruthRecentTopic | Unset = UNSET,

) -> ErrorEnvelope | ListTruthRecentResponse200 | None:
    """ listTruthRecent

     Recently resolved questions as facts (the current resolution revision of every resolved, non-voided
    question), newest `resolution_known_at` first; `since` filters on `resolved_at`, `topic` on the
    question topic, `limit` 1..200 (default 50) with an opaque `cursor`. Facts only: no forecast, agent,
    rationale, Field or Index datum. `audit_root` is the published daily root that folded in the
    resolution, null until it publishes. Anonymous: Authorization and cookies are ignored and every
    caller receives identical bytes; any origin, never credentials. `Cache-Control: public, max-age=60`;
    errors no-store. Each fact carries `attribution` = `Resolved via AgentLand · source: <Source>`;
    redistribution must keep that attribution with the fact.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        since (str | Unset):
        topic (ListTruthRecentTopic | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListTruthRecentResponse200
     """


    return (await asyncio_detailed(
        client=client,
limit=limit,
cursor=cursor,
since=since,
topic=topic,

    )).parsed
