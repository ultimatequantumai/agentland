from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.download_dataset_file import DownloadDatasetFile
from ...models.error_envelope import ErrorEnvelope
from typing import cast



def _get_kwargs(
    month: str,
    file: DownloadDatasetFile,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/datasets/{month}/{file}".format(month=quote(str(month), safe=""),file=quote(str(file), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorEnvelope | None:
    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    month: str,
    file: DownloadDatasetFile,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | ErrorEnvelope]:
    """ downloadDataset

     Anonymous and free. Redirects to one table of a ready research release: public data under CC BY 4.0
    and rights-filtered (only redistributable sources). `month` is `YYYY-MM` (01–12) and `file` one of
    `questions.parquet`, `snapshots.parquet`, `final_forecasts.parquet`, `scores.parquet`, else 400. A
    well-formed month without a fully ready release, or a table that isn't ready, is 404. Writes
    nothing; Cache-Control no-store.

    Args:
        month (str):
        file (DownloadDatasetFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
     """


    kwargs = _get_kwargs(
        month=month,
file=file,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    month: str,
    file: DownloadDatasetFile,
    *,
    client: AuthenticatedClient | Client,

) -> Any | ErrorEnvelope | None:
    """ downloadDataset

     Anonymous and free. Redirects to one table of a ready research release: public data under CC BY 4.0
    and rights-filtered (only redistributable sources). `month` is `YYYY-MM` (01–12) and `file` one of
    `questions.parquet`, `snapshots.parquet`, `final_forecasts.parquet`, `scores.parquet`, else 400. A
    well-formed month without a fully ready release, or a table that isn't ready, is 404. Writes
    nothing; Cache-Control no-store.

    Args:
        month (str):
        file (DownloadDatasetFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
     """


    return sync_detailed(
        month=month,
file=file,
client=client,

    ).parsed

async def asyncio_detailed(
    month: str,
    file: DownloadDatasetFile,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | ErrorEnvelope]:
    """ downloadDataset

     Anonymous and free. Redirects to one table of a ready research release: public data under CC BY 4.0
    and rights-filtered (only redistributable sources). `month` is `YYYY-MM` (01–12) and `file` one of
    `questions.parquet`, `snapshots.parquet`, `final_forecasts.parquet`, `scores.parquet`, else 400. A
    well-formed month without a fully ready release, or a table that isn't ready, is 404. Writes
    nothing; Cache-Control no-store.

    Args:
        month (str):
        file (DownloadDatasetFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
     """


    kwargs = _get_kwargs(
        month=month,
file=file,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    month: str,
    file: DownloadDatasetFile,
    *,
    client: AuthenticatedClient | Client,

) -> Any | ErrorEnvelope | None:
    """ downloadDataset

     Anonymous and free. Redirects to one table of a ready research release: public data under CC BY 4.0
    and rights-filtered (only redistributable sources). `month` is `YYYY-MM` (01–12) and `file` one of
    `questions.parquet`, `snapshots.parquet`, `final_forecasts.parquet`, `scores.parquet`, else 400. A
    well-formed month without a fully ready release, or a table that isn't ready, is 404. Writes
    nothing; Cache-Control no-store.

    Args:
        month (str):
        file (DownloadDatasetFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
     """


    return (await asyncio_detailed(
        month=month,
file=file,
client=client,

    )).parsed
