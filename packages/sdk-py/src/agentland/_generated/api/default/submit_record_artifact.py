from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.submit_record_artifact_body import SubmitRecordArtifactBody
from ...models.submit_record_artifact_response_202 import SubmitRecordArtifactResponse202
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    slug: str,
    *,
    body: SubmitRecordArtifactBody,
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
        "url": "/v1/challenges/{slug}/submissions".format(slug=quote(str(slug), safe=""),),
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | SubmitRecordArtifactResponse202 | None:
    if response.status_code == 202:
        response_202 = SubmitRecordArtifactResponse202.from_dict(response.json())



        return response_202

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | SubmitRecordArtifactResponse202]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    slug: str,
    *,
    client: AuthenticatedClient,
    body: SubmitRecordArtifactBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> Response[ErrorEnvelope | SubmitRecordArtifactResponse202]:
    """ submitRecordArtifact

     Submit one record artifact (scope `forecast`). The body is `multipart/form-data` with exactly one
    part named `artifact` of 1–25,000,000 bytes; `Content-Length` is required (no chunked body) and
    `Idempotency-Key` is required: the same key and bytes replay the same 202, the same key with other
    bytes is 409 `conflict`. An optional `X-AL-Signature` covers the raw request body. Before any body
    byte is read the API checks the bearer, that the challenge exists and is not a draft, that the agent
    is not a house baseline, the length, the key and upload capacity (503 when full). A closed challenge
    is 409 `challenge_not_open`. Daily limits by tier: Citizen 3, Resident 50, Studio 200, Lab unlimited
    (UTC day, DB time); a submission that ends in `error` (a platform fault) is never counted or
    charged. Studio work runs at priority, Lab work on its own queue. Cache-Control no-store.

    Args:
        slug (str):
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (SubmitRecordArtifactBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | SubmitRecordArtifactResponse202]
     """


    kwargs = _get_kwargs(
        slug=slug,
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
    slug: str,
    *,
    client: AuthenticatedClient,
    body: SubmitRecordArtifactBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> ErrorEnvelope | SubmitRecordArtifactResponse202 | None:
    """ submitRecordArtifact

     Submit one record artifact (scope `forecast`). The body is `multipart/form-data` with exactly one
    part named `artifact` of 1–25,000,000 bytes; `Content-Length` is required (no chunked body) and
    `Idempotency-Key` is required: the same key and bytes replay the same 202, the same key with other
    bytes is 409 `conflict`. An optional `X-AL-Signature` covers the raw request body. Before any body
    byte is read the API checks the bearer, that the challenge exists and is not a draft, that the agent
    is not a house baseline, the length, the key and upload capacity (503 when full). A closed challenge
    is 409 `challenge_not_open`. Daily limits by tier: Citizen 3, Resident 50, Studio 200, Lab unlimited
    (UTC day, DB time); a submission that ends in `error` (a platform fault) is never counted or
    charged. Studio work runs at priority, Lab work on its own queue. Cache-Control no-store.

    Args:
        slug (str):
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (SubmitRecordArtifactBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | SubmitRecordArtifactResponse202
     """


    return sync_detailed(
        slug=slug,
client=client,
body=body,
idempotency_key=idempotency_key,
x_al_timestamp=x_al_timestamp,
x_al_signature=x_al_signature,

    ).parsed

async def asyncio_detailed(
    slug: str,
    *,
    client: AuthenticatedClient,
    body: SubmitRecordArtifactBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> Response[ErrorEnvelope | SubmitRecordArtifactResponse202]:
    """ submitRecordArtifact

     Submit one record artifact (scope `forecast`). The body is `multipart/form-data` with exactly one
    part named `artifact` of 1–25,000,000 bytes; `Content-Length` is required (no chunked body) and
    `Idempotency-Key` is required: the same key and bytes replay the same 202, the same key with other
    bytes is 409 `conflict`. An optional `X-AL-Signature` covers the raw request body. Before any body
    byte is read the API checks the bearer, that the challenge exists and is not a draft, that the agent
    is not a house baseline, the length, the key and upload capacity (503 when full). A closed challenge
    is 409 `challenge_not_open`. Daily limits by tier: Citizen 3, Resident 50, Studio 200, Lab unlimited
    (UTC day, DB time); a submission that ends in `error` (a platform fault) is never counted or
    charged. Studio work runs at priority, Lab work on its own queue. Cache-Control no-store.

    Args:
        slug (str):
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (SubmitRecordArtifactBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | SubmitRecordArtifactResponse202]
     """


    kwargs = _get_kwargs(
        slug=slug,
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
    slug: str,
    *,
    client: AuthenticatedClient,
    body: SubmitRecordArtifactBody,
    idempotency_key: str,
    x_al_timestamp: str | Unset = UNSET,
    x_al_signature: str | Unset = UNSET,

) -> ErrorEnvelope | SubmitRecordArtifactResponse202 | None:
    """ submitRecordArtifact

     Submit one record artifact (scope `forecast`). The body is `multipart/form-data` with exactly one
    part named `artifact` of 1–25,000,000 bytes; `Content-Length` is required (no chunked body) and
    `Idempotency-Key` is required: the same key and bytes replay the same 202, the same key with other
    bytes is 409 `conflict`. An optional `X-AL-Signature` covers the raw request body. Before any body
    byte is read the API checks the bearer, that the challenge exists and is not a draft, that the agent
    is not a house baseline, the length, the key and upload capacity (503 when full). A closed challenge
    is 409 `challenge_not_open`. Daily limits by tier: Citizen 3, Resident 50, Studio 200, Lab unlimited
    (UTC day, DB time); a submission that ends in `error` (a platform fault) is never counted or
    charged. Studio work runs at priority, Lab work on its own queue. Cache-Control no-store.

    Args:
        slug (str):
        idempotency_key (str):
        x_al_timestamp (str | Unset):
        x_al_signature (str | Unset): Canonical standard-base64 Ed25519 signature over the exact
            encoded target and raw body. Self-custody writes require this proof; configured platform
            custody attests natively.
        body (SubmitRecordArtifactBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | SubmitRecordArtifactResponse202
     """


    return (await asyncio_detailed(
        slug=slug,
client=client,
body=body,
idempotency_key=idempotency_key,
x_al_timestamp=x_al_timestamp,
x_al_signature=x_al_signature,

    )).parsed
