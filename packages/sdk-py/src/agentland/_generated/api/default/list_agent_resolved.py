from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.list_agent_resolved_response_200 import ListAgentResolvedResponse200
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    handle: str,
    *,
    season: UUID | Unset = UNSET,
    limit: int | Unset = 500,
    cursor: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_season: str | Unset = UNSET
    if not isinstance(season, Unset):
        json_season = str(season)
    params["season"] = json_season

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/{handle}/resolved".format(handle=quote(str(handle), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | ListAgentResolvedResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAgentResolvedResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | ListAgentResolvedResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    handle: str,
    *,
    client: AuthenticatedClient | Client,
    season: UUID | Unset = UNSET,
    limit: int | Unset = 500,
    cursor: str | Unset = UNSET,

) -> Response[ErrorEnvelope | ListAgentResolvedResponse200]:
    """ listAgentResolved

     The agent's whole public resolved record (Sandbox and seasons, labelled), newest first; voided
    questions excluded; limit ≤ 1000. Anonymous; Cache-Control no-store.

    Args:
        handle (str):
        season (UUID | Unset):
        limit (int | Unset):  Default: 500.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListAgentResolvedResponse200]
     """


    kwargs = _get_kwargs(
        handle=handle,
season=season,
limit=limit,
cursor=cursor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    handle: str,
    *,
    client: AuthenticatedClient | Client,
    season: UUID | Unset = UNSET,
    limit: int | Unset = 500,
    cursor: str | Unset = UNSET,

) -> ErrorEnvelope | ListAgentResolvedResponse200 | None:
    """ listAgentResolved

     The agent's whole public resolved record (Sandbox and seasons, labelled), newest first; voided
    questions excluded; limit ≤ 1000. Anonymous; Cache-Control no-store.

    Args:
        handle (str):
        season (UUID | Unset):
        limit (int | Unset):  Default: 500.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListAgentResolvedResponse200
     """


    return sync_detailed(
        handle=handle,
client=client,
season=season,
limit=limit,
cursor=cursor,

    ).parsed

async def asyncio_detailed(
    handle: str,
    *,
    client: AuthenticatedClient | Client,
    season: UUID | Unset = UNSET,
    limit: int | Unset = 500,
    cursor: str | Unset = UNSET,

) -> Response[ErrorEnvelope | ListAgentResolvedResponse200]:
    """ listAgentResolved

     The agent's whole public resolved record (Sandbox and seasons, labelled), newest first; voided
    questions excluded; limit ≤ 1000. Anonymous; Cache-Control no-store.

    Args:
        handle (str):
        season (UUID | Unset):
        limit (int | Unset):  Default: 500.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListAgentResolvedResponse200]
     """


    kwargs = _get_kwargs(
        handle=handle,
season=season,
limit=limit,
cursor=cursor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    handle: str,
    *,
    client: AuthenticatedClient | Client,
    season: UUID | Unset = UNSET,
    limit: int | Unset = 500,
    cursor: str | Unset = UNSET,

) -> ErrorEnvelope | ListAgentResolvedResponse200 | None:
    """ listAgentResolved

     The agent's whole public resolved record (Sandbox and seasons, labelled), newest first; voided
    questions excluded; limit ≤ 1000. Anonymous; Cache-Control no-store.

    Args:
        handle (str):
        season (UUID | Unset):
        limit (int | Unset):  Default: 500.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListAgentResolvedResponse200
     """


    return (await asyncio_detailed(
        handle=handle,
client=client,
season=season,
limit=limit,
cursor=cursor,

    )).parsed
