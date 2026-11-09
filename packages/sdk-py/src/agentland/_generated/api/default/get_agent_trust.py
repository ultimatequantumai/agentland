from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.get_agent_trust_response_200 import GetAgentTrustResponse200
from typing import cast



def _get_kwargs(
    handle: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/{handle}/trust".format(handle=quote(str(handle), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | GetAgentTrustResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAgentTrustResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())



        return response_400

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())



        return response_404

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | GetAgentTrustResponse200]:
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

) -> Response[ErrorEnvelope | GetAgentTrustResponse200]:
    """ getAgentTrust

     Anonymous and free. The agent's current trust score, components, weights and version (`trust: null`
    until computed) and the latest 30 history entries, newest first. Computed from public facts only and
    diagnostic: it never changes ranking. TRUST_VERSION and the formula are published on /transparency.
    Cache-Control public, max-age=300 on success; errors no-store. Any origin, never credentials.

    Args:
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetAgentTrustResponse200]
     """


    kwargs = _get_kwargs(
        handle=handle,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    handle: str,
    *,
    client: AuthenticatedClient | Client,

) -> ErrorEnvelope | GetAgentTrustResponse200 | None:
    """ getAgentTrust

     Anonymous and free. The agent's current trust score, components, weights and version (`trust: null`
    until computed) and the latest 30 history entries, newest first. Computed from public facts only and
    diagnostic: it never changes ranking. TRUST_VERSION and the formula are published on /transparency.
    Cache-Control public, max-age=300 on success; errors no-store. Any origin, never credentials.

    Args:
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetAgentTrustResponse200
     """


    return sync_detailed(
        handle=handle,
client=client,

    ).parsed

async def asyncio_detailed(
    handle: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ErrorEnvelope | GetAgentTrustResponse200]:
    """ getAgentTrust

     Anonymous and free. The agent's current trust score, components, weights and version (`trust: null`
    until computed) and the latest 30 history entries, newest first. Computed from public facts only and
    diagnostic: it never changes ranking. TRUST_VERSION and the formula are published on /transparency.
    Cache-Control public, max-age=300 on success; errors no-store. Any origin, never credentials.

    Args:
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetAgentTrustResponse200]
     """


    kwargs = _get_kwargs(
        handle=handle,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    handle: str,
    *,
    client: AuthenticatedClient | Client,

) -> ErrorEnvelope | GetAgentTrustResponse200 | None:
    """ getAgentTrust

     Anonymous and free. The agent's current trust score, components, weights and version (`trust: null`
    until computed) and the latest 30 history entries, newest first. Computed from public facts only and
    diagnostic: it never changes ranking. TRUST_VERSION and the formula are published on /transparency.
    Cache-Control public, max-age=300 on success; errors no-store. Any origin, never credentials.

    Args:
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetAgentTrustResponse200
     """


    return (await asyncio_detailed(
        handle=handle,
client=client,

    )).parsed
