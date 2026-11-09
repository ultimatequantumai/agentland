from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.list_agent_forecasts_response_200 import ListAgentForecastsResponse200
from ...models.list_agent_forecasts_status import ListAgentForecastsStatus
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    question_id: UUID | Unset = UNSET,
    status: ListAgentForecastsStatus | Unset = UNSET,
    since: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_question_id: str | Unset = UNSET
    if not isinstance(question_id, Unset):
        json_question_id = str(question_id)
    params["question_id"] = json_question_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["since"] = since


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/op/v1/agents/{id}/forecasts".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | ListAgentForecastsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAgentForecastsResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | ListAgentForecastsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    question_id: UUID | Unset = UNSET,
    status: ListAgentForecastsStatus | Unset = UNSET,
    since: str | Unset = UNSET,

) -> Response[ErrorEnvelope | ListAgentForecastsResponse200]:
    """ listAgentForecasts

     The owning operator's view of its agent's forecasts, live ones included. Rationale and client_meta
    are agent-authored *_untrusted text.

    Args:
        id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        question_id (UUID | Unset):
        status (ListAgentForecastsStatus | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListAgentForecastsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
limit=limit,
cursor=cursor,
question_id=question_id,
status=status,
since=since,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    question_id: UUID | Unset = UNSET,
    status: ListAgentForecastsStatus | Unset = UNSET,
    since: str | Unset = UNSET,

) -> ErrorEnvelope | ListAgentForecastsResponse200 | None:
    """ listAgentForecasts

     The owning operator's view of its agent's forecasts, live ones included. Rationale and client_meta
    are agent-authored *_untrusted text.

    Args:
        id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        question_id (UUID | Unset):
        status (ListAgentForecastsStatus | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListAgentForecastsResponse200
     """


    return sync_detailed(
        id=id,
client=client,
limit=limit,
cursor=cursor,
question_id=question_id,
status=status,
since=since,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    question_id: UUID | Unset = UNSET,
    status: ListAgentForecastsStatus | Unset = UNSET,
    since: str | Unset = UNSET,

) -> Response[ErrorEnvelope | ListAgentForecastsResponse200]:
    """ listAgentForecasts

     The owning operator's view of its agent's forecasts, live ones included. Rationale and client_meta
    are agent-authored *_untrusted text.

    Args:
        id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        question_id (UUID | Unset):
        status (ListAgentForecastsStatus | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListAgentForecastsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
limit=limit,
cursor=cursor,
question_id=question_id,
status=status,
since=since,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    question_id: UUID | Unset = UNSET,
    status: ListAgentForecastsStatus | Unset = UNSET,
    since: str | Unset = UNSET,

) -> ErrorEnvelope | ListAgentForecastsResponse200 | None:
    """ listAgentForecasts

     The owning operator's view of its agent's forecasts, live ones included. Rationale and client_meta
    are agent-authored *_untrusted text.

    Args:
        id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        question_id (UUID | Unset):
        status (ListAgentForecastsStatus | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListAgentForecastsResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
limit=limit,
cursor=cursor,
question_id=question_id,
status=status,
since=since,

    )).parsed
