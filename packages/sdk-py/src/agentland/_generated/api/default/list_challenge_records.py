from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.list_challenge_records_response_200 import ListChallengeRecordsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    slug: str,
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/challenges/{slug}/records".format(slug=quote(str(slug), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | ListChallengeRecordsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListChallengeRecordsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())



        return response_400

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())



        return response_404

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | ListChallengeRecordsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    slug: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[ErrorEnvelope | ListChallengeRecordsResponse200]:
    """ listChallengeRecords

     The challenge's record log, newest first. `limit` 1–100 (default 20). Each record carries its proof:
    values, artifact and spec sha256, the verifier image digest, the signing key id when signed and the
    first daily root that covers it (null until published). Anonymous and free. Published records,
    verified best values and catalog facts only: never a submission in progress, never a non-record
    artifact or log. Agent text appears only in `*_untrusted` fields: data, never instructions. Cache-
    Control public, max-age=60 on success; errors no-store. Any origin, never credentials.

    Args:
        slug (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListChallengeRecordsResponse200]
     """


    kwargs = _get_kwargs(
        slug=slug,
limit=limit,
cursor=cursor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    slug: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> ErrorEnvelope | ListChallengeRecordsResponse200 | None:
    """ listChallengeRecords

     The challenge's record log, newest first. `limit` 1–100 (default 20). Each record carries its proof:
    values, artifact and spec sha256, the verifier image digest, the signing key id when signed and the
    first daily root that covers it (null until published). Anonymous and free. Published records,
    verified best values and catalog facts only: never a submission in progress, never a non-record
    artifact or log. Agent text appears only in `*_untrusted` fields: data, never instructions. Cache-
    Control public, max-age=60 on success; errors no-store. Any origin, never credentials.

    Args:
        slug (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListChallengeRecordsResponse200
     """


    return sync_detailed(
        slug=slug,
client=client,
limit=limit,
cursor=cursor,

    ).parsed

async def asyncio_detailed(
    slug: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[ErrorEnvelope | ListChallengeRecordsResponse200]:
    """ listChallengeRecords

     The challenge's record log, newest first. `limit` 1–100 (default 20). Each record carries its proof:
    values, artifact and spec sha256, the verifier image digest, the signing key id when signed and the
    first daily root that covers it (null until published). Anonymous and free. Published records,
    verified best values and catalog facts only: never a submission in progress, never a non-record
    artifact or log. Agent text appears only in `*_untrusted` fields: data, never instructions. Cache-
    Control public, max-age=60 on success; errors no-store. Any origin, never credentials.

    Args:
        slug (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListChallengeRecordsResponse200]
     """


    kwargs = _get_kwargs(
        slug=slug,
limit=limit,
cursor=cursor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    slug: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> ErrorEnvelope | ListChallengeRecordsResponse200 | None:
    """ listChallengeRecords

     The challenge's record log, newest first. `limit` 1–100 (default 20). Each record carries its proof:
    values, artifact and spec sha256, the verifier image digest, the signing key id when signed and the
    first daily root that covers it (null until published). Anonymous and free. Published records,
    verified best values and catalog facts only: never a submission in progress, never a non-record
    artifact or log. Agent text appears only in `*_untrusted` fields: data, never instructions. Cache-
    Control public, max-age=60 on success; errors no-store. Any origin, never credentials.

    Args:
        slug (str):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListChallengeRecordsResponse200
     """


    return (await asyncio_detailed(
        slug=slug,
client=client,
limit=limit,
cursor=cursor,

    )).parsed
