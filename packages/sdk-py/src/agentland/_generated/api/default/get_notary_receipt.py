from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.get_notary_receipt_response_200 import GetNotaryReceiptResponse200
from typing import cast
from uuid import UUID



def _get_kwargs(
    receipt_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/notary/{receipt_id}".format(receipt_id=quote(str(receipt_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | GetNotaryReceiptResponse200 | None:
    if response.status_code == 200:
        response_200 = GetNotaryReceiptResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | GetNotaryReceiptResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    receipt_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ErrorEnvelope | GetNotaryReceiptResponse200]:
    """ getNotaryReceipt

    Args:
        receipt_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetNotaryReceiptResponse200]
     """


    kwargs = _get_kwargs(
        receipt_id=receipt_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    receipt_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> ErrorEnvelope | GetNotaryReceiptResponse200 | None:
    """ getNotaryReceipt

    Args:
        receipt_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetNotaryReceiptResponse200
     """


    return sync_detailed(
        receipt_id=receipt_id,
client=client,

    ).parsed

async def asyncio_detailed(
    receipt_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ErrorEnvelope | GetNotaryReceiptResponse200]:
    """ getNotaryReceipt

    Args:
        receipt_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetNotaryReceiptResponse200]
     """


    kwargs = _get_kwargs(
        receipt_id=receipt_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    receipt_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> ErrorEnvelope | GetNotaryReceiptResponse200 | None:
    """ getNotaryReceipt

    Args:
        receipt_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetNotaryReceiptResponse200
     """


    return (await asyncio_detailed(
        receipt_id=receipt_id,
client=client,

    )).parsed
