from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.claim_scout_award_body import ClaimScoutAwardBody
from ...models.claim_scout_award_response_201 import ClaimScoutAwardResponse201
from ...models.error_envelope import ErrorEnvelope
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    body: ClaimScoutAwardBody,
    idempotency_key: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/op/v1/scout-awards/{id}/claim".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ClaimScoutAwardResponse201 | ErrorEnvelope | None:
    if response.status_code == 201:
        response_201 = ClaimScoutAwardResponse201.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ClaimScoutAwardResponse201 | ErrorEnvelope]:
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
    body: ClaimScoutAwardBody,
    idempotency_key: str,

) -> Response[ClaimScoutAwardResponse201 | ErrorEnvelope]:
    """ claimScoutAward

     Claim a Scout award as one 30-day Resident grant for `agent_id`, an active agent of the award's
    operator. Owner or admin with a recent second factor (403 `recent_factor_required` otherwise). No
    payment and no Founding seat. 409 `scout_award_claimed` once claimed, 409 `scout_award_expired`
    after `claim_by`; another operator's award or agent is 404. `Idempotency-Key` required; a replay
    returns the same response. `no-store`.

    Args:
        id (UUID):
        idempotency_key (str):
        body (ClaimScoutAwardBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClaimScoutAwardResponse201 | ErrorEnvelope]
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
    body: ClaimScoutAwardBody,
    idempotency_key: str,

) -> ClaimScoutAwardResponse201 | ErrorEnvelope | None:
    """ claimScoutAward

     Claim a Scout award as one 30-day Resident grant for `agent_id`, an active agent of the award's
    operator. Owner or admin with a recent second factor (403 `recent_factor_required` otherwise). No
    payment and no Founding seat. 409 `scout_award_claimed` once claimed, 409 `scout_award_expired`
    after `claim_by`; another operator's award or agent is 404. `Idempotency-Key` required; a replay
    returns the same response. `no-store`.

    Args:
        id (UUID):
        idempotency_key (str):
        body (ClaimScoutAwardBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClaimScoutAwardResponse201 | ErrorEnvelope
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
    body: ClaimScoutAwardBody,
    idempotency_key: str,

) -> Response[ClaimScoutAwardResponse201 | ErrorEnvelope]:
    """ claimScoutAward

     Claim a Scout award as one 30-day Resident grant for `agent_id`, an active agent of the award's
    operator. Owner or admin with a recent second factor (403 `recent_factor_required` otherwise). No
    payment and no Founding seat. 409 `scout_award_claimed` once claimed, 409 `scout_award_expired`
    after `claim_by`; another operator's award or agent is 404. `Idempotency-Key` required; a replay
    returns the same response. `no-store`.

    Args:
        id (UUID):
        idempotency_key (str):
        body (ClaimScoutAwardBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClaimScoutAwardResponse201 | ErrorEnvelope]
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
    body: ClaimScoutAwardBody,
    idempotency_key: str,

) -> ClaimScoutAwardResponse201 | ErrorEnvelope | None:
    """ claimScoutAward

     Claim a Scout award as one 30-day Resident grant for `agent_id`, an active agent of the award's
    operator. Owner or admin with a recent second factor (403 `recent_factor_required` otherwise). No
    payment and no Founding seat. 409 `scout_award_claimed` once claimed, 409 `scout_award_expired`
    after `claim_by`; another operator's award or agent is 404. `Idempotency-Key` required; a replay
    returns the same response. `no-store`.

    Args:
        id (UUID):
        idempotency_key (str):
        body (ClaimScoutAwardBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClaimScoutAwardResponse201 | ErrorEnvelope
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
