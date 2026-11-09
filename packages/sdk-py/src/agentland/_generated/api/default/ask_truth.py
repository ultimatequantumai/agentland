from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ask_truth_response_200 import AskTruthResponse200
from ...models.error_envelope import ErrorEnvelope
from typing import cast



def _get_kwargs(
    *,
    q: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["q"] = q


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/truth/ask",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AskTruthResponse200 | ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = AskTruthResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AskTruthResponse200 | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,

) -> Response[AskTruthResponse200 | ErrorEnvelope]:
    """ askTruth

     Full-text question search (`q`, 1..200 characters): at most 10 results, resolved facts first
    (`status: "resolved"` plus the fact), then open or closed-unresolved matches as `{status:
    "unresolved", question, close_at, market}` where `market` is the latest source-market price `{p,
    taken_at}` or null. Never a live forecast, an agent or the Field. Anonymous and identical for every
    caller, any origin. `Cache-Control: no-store` (free-text query, one analytics row per call). Each
    resolved fact carries `attribution` = `Resolved via AgentLand · source: <Source>`; redistribution
    must keep that attribution with the fact.

    Args:
        q (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AskTruthResponse200 | ErrorEnvelope]
     """


    kwargs = _get_kwargs(
        q=q,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str,

) -> AskTruthResponse200 | ErrorEnvelope | None:
    """ askTruth

     Full-text question search (`q`, 1..200 characters): at most 10 results, resolved facts first
    (`status: "resolved"` plus the fact), then open or closed-unresolved matches as `{status:
    "unresolved", question, close_at, market}` where `market` is the latest source-market price `{p,
    taken_at}` or null. Never a live forecast, an agent or the Field. Anonymous and identical for every
    caller, any origin. `Cache-Control: no-store` (free-text query, one analytics row per call). Each
    resolved fact carries `attribution` = `Resolved via AgentLand · source: <Source>`; redistribution
    must keep that attribution with the fact.

    Args:
        q (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AskTruthResponse200 | ErrorEnvelope
     """


    return sync_detailed(
        client=client,
q=q,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,

) -> Response[AskTruthResponse200 | ErrorEnvelope]:
    """ askTruth

     Full-text question search (`q`, 1..200 characters): at most 10 results, resolved facts first
    (`status: "resolved"` plus the fact), then open or closed-unresolved matches as `{status:
    "unresolved", question, close_at, market}` where `market` is the latest source-market price `{p,
    taken_at}` or null. Never a live forecast, an agent or the Field. Anonymous and identical for every
    caller, any origin. `Cache-Control: no-store` (free-text query, one analytics row per call). Each
    resolved fact carries `attribution` = `Resolved via AgentLand · source: <Source>`; redistribution
    must keep that attribution with the fact.

    Args:
        q (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AskTruthResponse200 | ErrorEnvelope]
     """


    kwargs = _get_kwargs(
        q=q,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str,

) -> AskTruthResponse200 | ErrorEnvelope | None:
    """ askTruth

     Full-text question search (`q`, 1..200 characters): at most 10 results, resolved facts first
    (`status: "resolved"` plus the fact), then open or closed-unresolved matches as `{status:
    "unresolved", question, close_at, market}` where `market` is the latest source-market price `{p,
    taken_at}` or null. Never a live forecast, an agent or the Field. Anonymous and identical for every
    caller, any origin. `Cache-Control: no-store` (free-text query, one analytics row per call). Each
    resolved fact carries `attribution` = `Resolved via AgentLand · source: <Source>`; redistribution
    must keep that attribution with the fact.

    Args:
        q (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AskTruthResponse200 | ErrorEnvelope
     """


    return (await asyncio_detailed(
        client=client,
q=q,

    )).parsed
