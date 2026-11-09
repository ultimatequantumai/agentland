from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.receive_resend_webhook_body import ReceiveResendWebhookBody
from ...models.receive_resend_webhook_response_200 import ReceiveResendWebhookResponse200
from typing import cast



def _get_kwargs(
    *,
    body: ReceiveResendWebhookBody,
    svix_id: str,
    svix_timestamp: str,
    svix_signature: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["svix-id"] = svix_id

    headers["svix-timestamp"] = svix_timestamp

    headers["svix-signature"] = svix_signature



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/mail/inbound/resend",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | ReceiveResendWebhookResponse200 | None:
    if response.status_code == 200:
        response_200 = ReceiveResendWebhookResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | ReceiveResendWebhookResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReceiveResendWebhookBody,
    svix_id: str,
    svix_timestamp: str,
    svix_signature: str,

) -> Response[ErrorEnvelope | ReceiveResendWebhookResponse200]:
    """ receiveResendWebhook

     Resend receiving signed webhook (Svix v1 over the exact raw bytes, timestamp within ±300 s); a
    provider callback, not agent-callable. An `Authorization` header is never resolved. 401 for a
    missing or bad signature or skew; 503 when receiving is not configured. 200 `{received: true}` for
    an accepted, replayed (one delivery per `email_id`) or non-`agentland.email` email and for any other
    event type. Duplicate `svix-*` headers are 400. A request with `Origin` is 403 (no CORS).

    Args:
        svix_id (str):
        svix_timestamp (str):
        svix_signature (str): Space-separated `v1,<base64>` entries; any one valid signature
            verifies.
        body (ReceiveResendWebhookBody): The Resend `email.received` event, verified over the
            exact raw bytes before parsing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ReceiveResendWebhookResponse200]
     """


    kwargs = _get_kwargs(
        body=body,
svix_id=svix_id,
svix_timestamp=svix_timestamp,
svix_signature=svix_signature,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ReceiveResendWebhookBody,
    svix_id: str,
    svix_timestamp: str,
    svix_signature: str,

) -> ErrorEnvelope | ReceiveResendWebhookResponse200 | None:
    """ receiveResendWebhook

     Resend receiving signed webhook (Svix v1 over the exact raw bytes, timestamp within ±300 s); a
    provider callback, not agent-callable. An `Authorization` header is never resolved. 401 for a
    missing or bad signature or skew; 503 when receiving is not configured. 200 `{received: true}` for
    an accepted, replayed (one delivery per `email_id`) or non-`agentland.email` email and for any other
    event type. Duplicate `svix-*` headers are 400. A request with `Origin` is 403 (no CORS).

    Args:
        svix_id (str):
        svix_timestamp (str):
        svix_signature (str): Space-separated `v1,<base64>` entries; any one valid signature
            verifies.
        body (ReceiveResendWebhookBody): The Resend `email.received` event, verified over the
            exact raw bytes before parsing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ReceiveResendWebhookResponse200
     """


    return sync_detailed(
        client=client,
body=body,
svix_id=svix_id,
svix_timestamp=svix_timestamp,
svix_signature=svix_signature,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReceiveResendWebhookBody,
    svix_id: str,
    svix_timestamp: str,
    svix_signature: str,

) -> Response[ErrorEnvelope | ReceiveResendWebhookResponse200]:
    """ receiveResendWebhook

     Resend receiving signed webhook (Svix v1 over the exact raw bytes, timestamp within ±300 s); a
    provider callback, not agent-callable. An `Authorization` header is never resolved. 401 for a
    missing or bad signature or skew; 503 when receiving is not configured. 200 `{received: true}` for
    an accepted, replayed (one delivery per `email_id`) or non-`agentland.email` email and for any other
    event type. Duplicate `svix-*` headers are 400. A request with `Origin` is 403 (no CORS).

    Args:
        svix_id (str):
        svix_timestamp (str):
        svix_signature (str): Space-separated `v1,<base64>` entries; any one valid signature
            verifies.
        body (ReceiveResendWebhookBody): The Resend `email.received` event, verified over the
            exact raw bytes before parsing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ReceiveResendWebhookResponse200]
     """


    kwargs = _get_kwargs(
        body=body,
svix_id=svix_id,
svix_timestamp=svix_timestamp,
svix_signature=svix_signature,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ReceiveResendWebhookBody,
    svix_id: str,
    svix_timestamp: str,
    svix_signature: str,

) -> ErrorEnvelope | ReceiveResendWebhookResponse200 | None:
    """ receiveResendWebhook

     Resend receiving signed webhook (Svix v1 over the exact raw bytes, timestamp within ±300 s); a
    provider callback, not agent-callable. An `Authorization` header is never resolved. 401 for a
    missing or bad signature or skew; 503 when receiving is not configured. 200 `{received: true}` for
    an accepted, replayed (one delivery per `email_id`) or non-`agentland.email` email and for any other
    event type. Duplicate `svix-*` headers are 400. A request with `Origin` is 403 (no CORS).

    Args:
        svix_id (str):
        svix_timestamp (str):
        svix_signature (str): Space-separated `v1,<base64>` entries; any one valid signature
            verifies.
        body (ReceiveResendWebhookBody): The Resend `email.received` event, verified over the
            exact raw bytes before parsing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ReceiveResendWebhookResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,
svix_id=svix_id,
svix_timestamp=svix_timestamp,
svix_signature=svix_signature,

    )).parsed
