from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.put_memory_body import PutMemoryBody
from ...models.put_memory_response_201 import PutMemoryResponse201
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    key: str,
    *,
    body: PutMemoryBody,
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
        "method": "put",
        "url": "/v1/me/memory/{key}".format(key=quote(str(key), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | PutMemoryResponse201 | None:
    if response.status_code == 201:
        response_201 = PutMemoryResponse201.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | PutMemoryResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key: str,
    *,
    client: AuthenticatedClient,
    body: PutMemoryBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> Response[ErrorEnvelope | PutMemoryResponse201]:
    """ putMemory

     Appends a signed put to the vault chain. Self custody: body `signature` over the canonical intent
    and the request signature over the encoded target. Stale `if_seq` → 409 conflict (never rebased);
    exhausted budget → 429 quota_exceeded; sealed/ → 400.

    Args:
        key (str): Vault key sent as ONE percent-encoded path segment (`vault/notes` →
            `vault%2Fnotes`), decoded exactly once; a raw `/` or a double-encoded `%252F` never names
            the key.
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (PutMemoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PutMemoryResponse201]
     """


    kwargs = _get_kwargs(
        key=key,
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
    key: str,
    *,
    client: AuthenticatedClient,
    body: PutMemoryBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> ErrorEnvelope | PutMemoryResponse201 | None:
    """ putMemory

     Appends a signed put to the vault chain. Self custody: body `signature` over the canonical intent
    and the request signature over the encoded target. Stale `if_seq` → 409 conflict (never rebased);
    exhausted budget → 429 quota_exceeded; sealed/ → 400.

    Args:
        key (str): Vault key sent as ONE percent-encoded path segment (`vault/notes` →
            `vault%2Fnotes`), decoded exactly once; a raw `/` or a double-encoded `%252F` never names
            the key.
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (PutMemoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PutMemoryResponse201
     """


    return sync_detailed(
        key=key,
client=client,
body=body,
idempotency_key=idempotency_key,
x_al_timestamp=x_al_timestamp,
x_al_signature=x_al_signature,

    ).parsed

async def asyncio_detailed(
    key: str,
    *,
    client: AuthenticatedClient,
    body: PutMemoryBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> Response[ErrorEnvelope | PutMemoryResponse201]:
    """ putMemory

     Appends a signed put to the vault chain. Self custody: body `signature` over the canonical intent
    and the request signature over the encoded target. Stale `if_seq` → 409 conflict (never rebased);
    exhausted budget → 429 quota_exceeded; sealed/ → 400.

    Args:
        key (str): Vault key sent as ONE percent-encoded path segment (`vault/notes` →
            `vault%2Fnotes`), decoded exactly once; a raw `/` or a double-encoded `%252F` never names
            the key.
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (PutMemoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PutMemoryResponse201]
     """


    kwargs = _get_kwargs(
        key=key,
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
    key: str,
    *,
    client: AuthenticatedClient,
    body: PutMemoryBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> ErrorEnvelope | PutMemoryResponse201 | None:
    """ putMemory

     Appends a signed put to the vault chain. Self custody: body `signature` over the canonical intent
    and the request signature over the encoded target. Stale `if_seq` → 409 conflict (never rebased);
    exhausted budget → 429 quota_exceeded; sealed/ → 400.

    Args:
        key (str): Vault key sent as ONE percent-encoded path segment (`vault/notes` →
            `vault%2Fnotes`), decoded exactly once; a raw `/` or a double-encoded `%252F` never names
            the key.
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (PutMemoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PutMemoryResponse201
     """


    return (await asyncio_detailed(
        key=key,
client=client,
body=body,
idempotency_key=idempotency_key,
x_al_timestamp=x_al_timestamp,
x_al_signature=x_al_signature,

    )).parsed
