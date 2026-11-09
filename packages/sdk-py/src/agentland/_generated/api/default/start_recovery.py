from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.start_recovery_body import StartRecoveryBody
from ...models.start_recovery_response_201 import StartRecoveryResponse201
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    body: StartRecoveryBody,
    idempotency_key: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/op/v1/agents/{id}/recoveries".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | StartRecoveryResponse201 | None:
    if response.status_code == 201:
        response_201 = StartRecoveryResponse201.from_dict(response.json())



        return response_201

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | StartRecoveryResponse201]:
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
    body: StartRecoveryBody,
    idempotency_key: str,

) -> Response[ErrorEnvelope | StartRecoveryResponse201]:
    """ startRecovery

     Starts a 72-hour key recovery with a proof of possession of the new key; the pending recovery is a
    public notice on the DID history until it completes or the agent or operator cancels it.

    Args:
        id (UUID):
        idempotency_key (str):
        body (StartRecoveryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | StartRecoveryResponse201]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: StartRecoveryBody,
    idempotency_key: str,

) -> ErrorEnvelope | StartRecoveryResponse201 | None:
    """ startRecovery

     Starts a 72-hour key recovery with a proof of possession of the new key; the pending recovery is a
    public notice on the DID history until it completes or the agent or operator cancels it.

    Args:
        id (UUID):
        idempotency_key (str):
        body (StartRecoveryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | StartRecoveryResponse201
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: StartRecoveryBody,
    idempotency_key: str,

) -> Response[ErrorEnvelope | StartRecoveryResponse201]:
    """ startRecovery

     Starts a 72-hour key recovery with a proof of possession of the new key; the pending recovery is a
    public notice on the DID history until it completes or the agent or operator cancels it.

    Args:
        id (UUID):
        idempotency_key (str):
        body (StartRecoveryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | StartRecoveryResponse201]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: StartRecoveryBody,
    idempotency_key: str,

) -> ErrorEnvelope | StartRecoveryResponse201 | None:
    """ startRecovery

     Starts a 72-hour key recovery with a proof of possession of the new key; the pending recovery is a
    public notice on the DID history until it completes or the agent or operator cancels it.

    Args:
        id (UUID):
        idempotency_key (str):
        body (StartRecoveryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | StartRecoveryResponse201
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
