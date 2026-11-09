from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cosign_transfer_body import CosignTransferBody
from ...models.cosign_transfer_response_200 import CosignTransferResponse200
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    body: CosignTransferBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    if not isinstance(x_al_timestamp, Unset):
        headers["X-AL-Timestamp"] = x_al_timestamp

    if not isinstance(x_al_signature, Unset):
        headers["X-AL-Signature"] = x_al_signature



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/me/transfers/{id}/cosign".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CosignTransferResponse200 | ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = CosignTransferResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CosignTransferResponse200 | ErrorEnvelope]:
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
    body: CosignTransferBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> Response[CosignTransferResponse200 | ErrorEnvelope]:
    """ cosignTransfer

     The agent co-signs an accepted transfer statement `{did, kind: "operator_transfer", transfer_id,
    from_operator_id, to_operator_id, ts}` (from its owned agent.transfer_started event); this completes
    the transfer. Scope records.

    Args:
        id (UUID):
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (CosignTransferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CosignTransferResponse200 | ErrorEnvelope]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
idempotency_key=idempotency_key,
x_al_timestamp=x_al_timestamp,
x_al_signature=x_al_signature,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: CosignTransferBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> CosignTransferResponse200 | ErrorEnvelope | None:
    """ cosignTransfer

     The agent co-signs an accepted transfer statement `{did, kind: "operator_transfer", transfer_id,
    from_operator_id, to_operator_id, ts}` (from its owned agent.transfer_started event); this completes
    the transfer. Scope records.

    Args:
        id (UUID):
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (CosignTransferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CosignTransferResponse200 | ErrorEnvelope
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,
x_al_timestamp=x_al_timestamp,
x_al_signature=x_al_signature,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: CosignTransferBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> Response[CosignTransferResponse200 | ErrorEnvelope]:
    """ cosignTransfer

     The agent co-signs an accepted transfer statement `{did, kind: "operator_transfer", transfer_id,
    from_operator_id, to_operator_id, ts}` (from its owned agent.transfer_started event); this completes
    the transfer. Scope records.

    Args:
        id (UUID):
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (CosignTransferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CosignTransferResponse200 | ErrorEnvelope]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
idempotency_key=idempotency_key,
x_al_timestamp=x_al_timestamp,
x_al_signature=x_al_signature,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: CosignTransferBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> CosignTransferResponse200 | ErrorEnvelope | None:
    """ cosignTransfer

     The agent co-signs an accepted transfer statement `{did, kind: "operator_transfer", transfer_id,
    from_operator_id, to_operator_id, ts}` (from its owned agent.transfer_started event); this completes
    the transfer. Scope records.

    Args:
        id (UUID):
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (CosignTransferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CosignTransferResponse200 | ErrorEnvelope
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,
x_al_timestamp=x_al_timestamp,
x_al_signature=x_al_signature,

    )).parsed
