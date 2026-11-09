from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.rotate_signing_key_body import RotateSigningKeyBody
from ...models.rotate_signing_key_response_201_type_0 import RotateSigningKeyResponse201Type0
from ...models.rotate_signing_key_response_201_type_1 import RotateSigningKeyResponse201Type1
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: RotateSigningKeyBody,
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
        "url": "/v1/me/keys/rotate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | RotateSigningKeyResponse201Type0 | RotateSigningKeyResponse201Type1 | None:
    if response.status_code == 201:
        def _parse_response_201(data: object) -> RotateSigningKeyResponse201Type0 | RotateSigningKeyResponse201Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0 = RotateSigningKeyResponse201Type0.from_dict(data)



                return response_201_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_201_type_1 = RotateSigningKeyResponse201Type1.from_dict(data)



            return response_201_type_1

        response_201 = _parse_response_201(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | RotateSigningKeyResponse201Type0 | RotateSigningKeyResponse201Type1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RotateSigningKeyBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> Response[ErrorEnvelope | RotateSigningKeyResponse201Type0 | RotateSigningKeyResponse201Type1]:
    """ rotateSigningKey

     Self custody: `sig_old` + `sig_new` rotate immediately; `sig_old` alone opens the 7-day compromise
    window (status `challenge_opened`); `sig_new` alone is 400. Platform custody: omit `sig_old` and
    supply `sig_new` to upgrade to self custody. Scope records.

    Args:
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (RotateSigningKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | RotateSigningKeyResponse201Type0 | RotateSigningKeyResponse201Type1]
     """


    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    body: RotateSigningKeyBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> ErrorEnvelope | RotateSigningKeyResponse201Type0 | RotateSigningKeyResponse201Type1 | None:
    """ rotateSigningKey

     Self custody: `sig_old` + `sig_new` rotate immediately; `sig_old` alone opens the 7-day compromise
    window (status `challenge_opened`); `sig_new` alone is 400. Platform custody: omit `sig_old` and
    supply `sig_new` to upgrade to self custody. Scope records.

    Args:
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (RotateSigningKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | RotateSigningKeyResponse201Type0 | RotateSigningKeyResponse201Type1
     """


    return sync_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,
x_al_timestamp=x_al_timestamp,
x_al_signature=x_al_signature,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RotateSigningKeyBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> Response[ErrorEnvelope | RotateSigningKeyResponse201Type0 | RotateSigningKeyResponse201Type1]:
    """ rotateSigningKey

     Self custody: `sig_old` + `sig_new` rotate immediately; `sig_old` alone opens the 7-day compromise
    window (status `challenge_opened`); `sig_new` alone is 400. Platform custody: omit `sig_old` and
    supply `sig_new` to upgrade to self custody. Scope records.

    Args:
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (RotateSigningKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | RotateSigningKeyResponse201Type0 | RotateSigningKeyResponse201Type1]
     """


    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    body: RotateSigningKeyBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> ErrorEnvelope | RotateSigningKeyResponse201Type0 | RotateSigningKeyResponse201Type1 | None:
    """ rotateSigningKey

     Self custody: `sig_old` + `sig_new` rotate immediately; `sig_old` alone opens the 7-day compromise
    window (status `challenge_opened`); `sig_new` alone is 400. Platform custody: omit `sig_old` and
    supply `sig_new` to upgrade to self custody. Scope records.

    Args:
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (RotateSigningKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | RotateSigningKeyResponse201Type0 | RotateSigningKeyResponse201Type1
     """


    return (await asyncio_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,
x_al_timestamp=x_al_timestamp,
x_al_signature=x_al_signature,

    )).parsed
