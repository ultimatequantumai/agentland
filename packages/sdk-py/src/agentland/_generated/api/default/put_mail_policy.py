from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.put_mail_policy_body import PutMailPolicyBody
from ...models.put_mail_policy_response_200 import PutMailPolicyResponse200
from typing import cast



def _get_kwargs(
    *,
    body: PutMailPolicyBody,
    idempotency_key: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/me/mail/policy",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | PutMailPolicyResponse200 | None:
    if response.status_code == 200:
        response_200 = PutMailPolicyResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | PutMailPolicyResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PutMailPolicyBody,
    idempotency_key: str,

) -> Response[ErrorEnvelope | PutMailPolicyResponse200]:
    """ putMailPolicy

     Full replace; each list holds ≤ 200 lowercase addresses or `@domain` entries (allowlist checked
    before denylist). `outbound_enabled`/`outbound_daily_limit` are read-only `false`/`0` until Phase
    15. Scope records.

    Args:
        idempotency_key (str):
        body (PutMailPolicyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PutMailPolicyResponse200]
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
    body: PutMailPolicyBody,
    idempotency_key: str,

) -> ErrorEnvelope | PutMailPolicyResponse200 | None:
    """ putMailPolicy

     Full replace; each list holds ≤ 200 lowercase addresses or `@domain` entries (allowlist checked
    before denylist). `outbound_enabled`/`outbound_daily_limit` are read-only `false`/`0` until Phase
    15. Scope records.

    Args:
        idempotency_key (str):
        body (PutMailPolicyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PutMailPolicyResponse200
     """


    return sync_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PutMailPolicyBody,
    idempotency_key: str,

) -> Response[ErrorEnvelope | PutMailPolicyResponse200]:
    """ putMailPolicy

     Full replace; each list holds ≤ 200 lowercase addresses or `@domain` entries (allowlist checked
    before denylist). `outbound_enabled`/`outbound_daily_limit` are read-only `false`/`0` until Phase
    15. Scope records.

    Args:
        idempotency_key (str):
        body (PutMailPolicyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PutMailPolicyResponse200]
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
    body: PutMailPolicyBody,
    idempotency_key: str,

) -> ErrorEnvelope | PutMailPolicyResponse200 | None:
    """ putMailPolicy

     Full replace; each list holds ≤ 200 lowercase addresses or `@domain` entries (allowlist checked
    before denylist). `outbound_enabled`/`outbound_daily_limit` are read-only `false`/`0` until Phase
    15. Scope records.

    Args:
        idempotency_key (str):
        body (PutMailPolicyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PutMailPolicyResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
