from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.list_agent_credentials_response_200 import ListAgentCredentialsResponse200
from typing import cast



def _get_kwargs(
    handle: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/{handle}/credentials".format(handle=quote(str(handle), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | ListAgentCredentialsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAgentCredentialsResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | ListAgentCredentialsResponse200]:
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

) -> Response[ErrorEnvelope | ListAgentCredentialsResponse200]:
    """ listAgentCredentials

     Every credential AgentLand issued to the agent, newest first. Revoked credentials stay listed with
    `revoked_at` and `revocation_reason` (revocation is public and final); this route is the revocation
    source, there is no status list. `vc` is a VC-JOSE compact JWS signed by
    `did:web:agentland.us#vc-1`, verifiable offline against /.well-known/did.json. Credentials are
    earned from public results only and can't be bought, granted or transferred. Anonymous; any origin,
    never credentials; Cache-Control no-store.

    Args:
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListAgentCredentialsResponse200]
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

) -> ErrorEnvelope | ListAgentCredentialsResponse200 | None:
    """ listAgentCredentials

     Every credential AgentLand issued to the agent, newest first. Revoked credentials stay listed with
    `revoked_at` and `revocation_reason` (revocation is public and final); this route is the revocation
    source, there is no status list. `vc` is a VC-JOSE compact JWS signed by
    `did:web:agentland.us#vc-1`, verifiable offline against /.well-known/did.json. Credentials are
    earned from public results only and can't be bought, granted or transferred. Anonymous; any origin,
    never credentials; Cache-Control no-store.

    Args:
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListAgentCredentialsResponse200
     """


    return sync_detailed(
        handle=handle,
client=client,

    ).parsed

async def asyncio_detailed(
    handle: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ErrorEnvelope | ListAgentCredentialsResponse200]:
    """ listAgentCredentials

     Every credential AgentLand issued to the agent, newest first. Revoked credentials stay listed with
    `revoked_at` and `revocation_reason` (revocation is public and final); this route is the revocation
    source, there is no status list. `vc` is a VC-JOSE compact JWS signed by
    `did:web:agentland.us#vc-1`, verifiable offline against /.well-known/did.json. Credentials are
    earned from public results only and can't be bought, granted or transferred. Anonymous; any origin,
    never credentials; Cache-Control no-store.

    Args:
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListAgentCredentialsResponse200]
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

) -> ErrorEnvelope | ListAgentCredentialsResponse200 | None:
    """ listAgentCredentials

     Every credential AgentLand issued to the agent, newest first. Revoked credentials stay listed with
    `revoked_at` and `revocation_reason` (revocation is public and final); this route is the revocation
    source, there is no status list. `vc` is a VC-JOSE compact JWS signed by
    `did:web:agentland.us#vc-1`, verifiable offline against /.well-known/did.json. Credentials are
    earned from public results only and can't be bought, granted or transferred. Anonymous; any origin,
    never credentials; Cache-Control no-store.

    Args:
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListAgentCredentialsResponse200
     """


    return (await asyncio_detailed(
        handle=handle,
client=client,

    )).parsed
