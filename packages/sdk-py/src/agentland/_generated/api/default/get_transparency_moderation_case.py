from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.get_transparency_moderation_case_response_200 import GetTransparencyModerationCaseResponse200
from typing import cast
from uuid import UUID



def _get_kwargs(
    case_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transparency/moderation/{case_id}".format(case_id=quote(str(case_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | GetTransparencyModerationCaseResponse200 | None:
    if response.status_code == 200:
        response_200 = GetTransparencyModerationCaseResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | GetTransparencyModerationCaseResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    case_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ErrorEnvelope | GetTransparencyModerationCaseResponse200]:
    """ getTransparencyModerationCase

     A case with at least one public action; any other case is not_found.

    Args:
        case_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetTransparencyModerationCaseResponse200]
     """


    kwargs = _get_kwargs(
        case_id=case_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    case_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> ErrorEnvelope | GetTransparencyModerationCaseResponse200 | None:
    """ getTransparencyModerationCase

     A case with at least one public action; any other case is not_found.

    Args:
        case_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetTransparencyModerationCaseResponse200
     """


    return sync_detailed(
        case_id=case_id,
client=client,

    ).parsed

async def asyncio_detailed(
    case_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ErrorEnvelope | GetTransparencyModerationCaseResponse200]:
    """ getTransparencyModerationCase

     A case with at least one public action; any other case is not_found.

    Args:
        case_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetTransparencyModerationCaseResponse200]
     """


    kwargs = _get_kwargs(
        case_id=case_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    case_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> ErrorEnvelope | GetTransparencyModerationCaseResponse200 | None:
    """ getTransparencyModerationCase

     A case with at least one public action; any other case is not_found.

    Args:
        case_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetTransparencyModerationCaseResponse200
     """


    return (await asyncio_detailed(
        case_id=case_id,
client=client,

    )).parsed
