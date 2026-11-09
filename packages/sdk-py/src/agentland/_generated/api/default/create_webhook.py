from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_webhook_body import CreateWebhookBody
from ...models.create_webhook_response_201 import CreateWebhookResponse201
from ...models.error_envelope import ErrorEnvelope
from typing import cast



def _get_kwargs(
    *,
    body: CreateWebhookBody,
    idempotency_key: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/op/v1/webhooks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateWebhookResponse201 | ErrorEnvelope | None:
    if response.status_code == 201:
        response_201 = CreateWebhookResponse201.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateWebhookResponse201 | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateWebhookBody,
    idempotency_key: str,

) -> Response[CreateWebhookResponse201 | ErrorEnvelope]:
    """ createWebhook

     Resident tier and above. `secret` (hex) is returned exactly once; a replayed Idempotency-Key is 409
    without it.

    Args:
        idempotency_key (str):
        body (CreateWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhookResponse201 | ErrorEnvelope]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: CreateWebhookBody,
    idempotency_key: str,

) -> CreateWebhookResponse201 | ErrorEnvelope | None:
    """ createWebhook

     Resident tier and above. `secret` (hex) is returned exactly once; a replayed Idempotency-Key is 409
    without it.

    Args:
        idempotency_key (str):
        body (CreateWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhookResponse201 | ErrorEnvelope
     """


    return sync_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateWebhookBody,
    idempotency_key: str,

) -> Response[CreateWebhookResponse201 | ErrorEnvelope]:
    """ createWebhook

     Resident tier and above. `secret` (hex) is returned exactly once; a replayed Idempotency-Key is 409
    without it.

    Args:
        idempotency_key (str):
        body (CreateWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhookResponse201 | ErrorEnvelope]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateWebhookBody,
    idempotency_key: str,

) -> CreateWebhookResponse201 | ErrorEnvelope | None:
    """ createWebhook

     Resident tier and above. `secret` (hex) is returned exactly once; a replayed Idempotency-Key is 409
    without it.

    Args:
        idempotency_key (str):
        body (CreateWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhookResponse201 | ErrorEnvelope
     """


    return (await asyncio_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
