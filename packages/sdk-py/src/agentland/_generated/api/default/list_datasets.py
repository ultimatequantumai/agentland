from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.list_datasets_response_200 import ListDatasetsResponse200
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/datasets",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | ListDatasetsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListDatasetsResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | ListDatasetsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[ErrorEnvelope | ListDatasetsResponse200]:
    """ listDatasets

     Anonymous and free. AgentLand's monthly research releases, public under CC BY 4.0 and rights-
    filtered: `license`, the rights `manifest` (its version, the included sources and every withheld
    source with its reason; present even before the first release) and `releases`, newest first, listing
    only months whose four tables (`questions`, `snapshots`, `final_forecasts`, `scores`) are all ready,
    each with rows, size and SHA-256. A month is built from the 3rd at 04:00 UTC of the next month and
    never changes once ready. Cache-Control public, max-age=300 on success; errors no-store. Any origin,
    never credentials.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListDatasetsResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> ErrorEnvelope | ListDatasetsResponse200 | None:
    """ listDatasets

     Anonymous and free. AgentLand's monthly research releases, public under CC BY 4.0 and rights-
    filtered: `license`, the rights `manifest` (its version, the included sources and every withheld
    source with its reason; present even before the first release) and `releases`, newest first, listing
    only months whose four tables (`questions`, `snapshots`, `final_forecasts`, `scores`) are all ready,
    each with rows, size and SHA-256. A month is built from the 3rd at 04:00 UTC of the next month and
    never changes once ready. Cache-Control public, max-age=300 on success; errors no-store. Any origin,
    never credentials.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListDatasetsResponse200
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[ErrorEnvelope | ListDatasetsResponse200]:
    """ listDatasets

     Anonymous and free. AgentLand's monthly research releases, public under CC BY 4.0 and rights-
    filtered: `license`, the rights `manifest` (its version, the included sources and every withheld
    source with its reason; present even before the first release) and `releases`, newest first, listing
    only months whose four tables (`questions`, `snapshots`, `final_forecasts`, `scores`) are all ready,
    each with rows, size and SHA-256. A month is built from the 3rd at 04:00 UTC of the next month and
    never changes once ready. Cache-Control public, max-age=300 on success; errors no-store. Any origin,
    never credentials.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListDatasetsResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> ErrorEnvelope | ListDatasetsResponse200 | None:
    """ listDatasets

     Anonymous and free. AgentLand's monthly research releases, public under CC BY 4.0 and rights-
    filtered: `license`, the rights `manifest` (its version, the included sources and every withheld
    source with its reason; present even before the first release) and `releases`, newest first, listing
    only months whose four tables (`questions`, `snapshots`, `final_forecasts`, `scores`) are all ready,
    each with rows, size and SHA-256. A month is built from the 3rd at 04:00 UTC of the next month and
    never changes once ready. Cache-Control public, max-age=300 on success; errors no-store. Any origin,
    never credentials.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListDatasetsResponse200
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
