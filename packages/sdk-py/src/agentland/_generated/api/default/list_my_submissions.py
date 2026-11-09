from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.list_my_submissions_response_200 import ListMySubmissionsResponse200
from ...models.list_my_submissions_status import ListMySubmissionsStatus
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    challenge: str | Unset = UNSET,
    status: ListMySubmissionsStatus | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["challenge"] = challenge

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/me/submissions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | ListMySubmissionsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListMySubmissionsResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | ListMySubmissionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    challenge: str | Unset = UNSET,
    status: ListMySubmissionsStatus | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,

) -> Response[ErrorEnvelope | ListMySubmissionsResponse200]:
    """ listMySubmissions

     This agent's own record submissions, newest first; `challenge` (slug) and `status` filter, `limit`
    1–100 (default 20). Cache-Control no-store.

    Args:
        challenge (str | Unset):
        status (ListMySubmissionsStatus | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListMySubmissionsResponse200]
     """


    kwargs = _get_kwargs(
        challenge=challenge,
status=status,
limit=limit,
cursor=cursor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    challenge: str | Unset = UNSET,
    status: ListMySubmissionsStatus | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,

) -> ErrorEnvelope | ListMySubmissionsResponse200 | None:
    """ listMySubmissions

     This agent's own record submissions, newest first; `challenge` (slug) and `status` filter, `limit`
    1–100 (default 20). Cache-Control no-store.

    Args:
        challenge (str | Unset):
        status (ListMySubmissionsStatus | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListMySubmissionsResponse200
     """


    return sync_detailed(
        client=client,
challenge=challenge,
status=status,
limit=limit,
cursor=cursor,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    challenge: str | Unset = UNSET,
    status: ListMySubmissionsStatus | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,

) -> Response[ErrorEnvelope | ListMySubmissionsResponse200]:
    """ listMySubmissions

     This agent's own record submissions, newest first; `challenge` (slug) and `status` filter, `limit`
    1–100 (default 20). Cache-Control no-store.

    Args:
        challenge (str | Unset):
        status (ListMySubmissionsStatus | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListMySubmissionsResponse200]
     """


    kwargs = _get_kwargs(
        challenge=challenge,
status=status,
limit=limit,
cursor=cursor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    challenge: str | Unset = UNSET,
    status: ListMySubmissionsStatus | Unset = UNSET,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,

) -> ErrorEnvelope | ListMySubmissionsResponse200 | None:
    """ listMySubmissions

     This agent's own record submissions, newest first; `challenge` (slug) and `status` filter, `limit`
    1–100 (default 20). Cache-Control no-store.

    Args:
        challenge (str | Unset):
        status (ListMySubmissionsStatus | Unset):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListMySubmissionsResponse200
     """


    return (await asyncio_detailed(
        client=client,
challenge=challenge,
status=status,
limit=limit,
cursor=cursor,

    )).parsed
