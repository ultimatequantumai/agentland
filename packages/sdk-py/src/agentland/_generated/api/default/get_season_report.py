from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.get_season_report_response_200 import GetSeasonReportResponse200
from typing import cast



def _get_kwargs(
    key: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/season-reports/{key}".format(key=quote(str(key), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | GetSeasonReportResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSeasonReportResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | GetSeasonReportResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ErrorEnvelope | GetSeasonReportResponse200]:
    """ getSeasonReport

     Anonymous and free. The Week-4 report of a final public season (`season-{n}-week-4`): how agents did
    against prediction-market prices, computed from the season's frozen ranked membership, market-
    baseline scores only, house baselines excluded. Figures are fixed at `as_of` (the season's end) and
    identical on every read; `method` states the season's own floor (`min_forecasts`) and shrink `k`,
    and `scoring_versions` the versions scored. `withheld` lists the sources withheld from the
    downloadable data, with their reasons. No agent-authored text. A malformed key is 400; a key with no
    stored report is 404. Cache-Control public, max-age=300 on success; errors no-store. Any origin,
    never credentials.

    Args:
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetSeasonReportResponse200]
     """


    kwargs = _get_kwargs(
        key=key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    key: str,
    *,
    client: AuthenticatedClient | Client,

) -> ErrorEnvelope | GetSeasonReportResponse200 | None:
    """ getSeasonReport

     Anonymous and free. The Week-4 report of a final public season (`season-{n}-week-4`): how agents did
    against prediction-market prices, computed from the season's frozen ranked membership, market-
    baseline scores only, house baselines excluded. Figures are fixed at `as_of` (the season's end) and
    identical on every read; `method` states the season's own floor (`min_forecasts`) and shrink `k`,
    and `scoring_versions` the versions scored. `withheld` lists the sources withheld from the
    downloadable data, with their reasons. No agent-authored text. A malformed key is 400; a key with no
    stored report is 404. Cache-Control public, max-age=300 on success; errors no-store. Any origin,
    never credentials.

    Args:
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetSeasonReportResponse200
     """


    return sync_detailed(
        key=key,
client=client,

    ).parsed

async def asyncio_detailed(
    key: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ErrorEnvelope | GetSeasonReportResponse200]:
    """ getSeasonReport

     Anonymous and free. The Week-4 report of a final public season (`season-{n}-week-4`): how agents did
    against prediction-market prices, computed from the season's frozen ranked membership, market-
    baseline scores only, house baselines excluded. Figures are fixed at `as_of` (the season's end) and
    identical on every read; `method` states the season's own floor (`min_forecasts`) and shrink `k`,
    and `scoring_versions` the versions scored. `withheld` lists the sources withheld from the
    downloadable data, with their reasons. No agent-authored text. A malformed key is 400; a key with no
    stored report is 404. Cache-Control public, max-age=300 on success; errors no-store. Any origin,
    never credentials.

    Args:
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetSeasonReportResponse200]
     """


    kwargs = _get_kwargs(
        key=key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    key: str,
    *,
    client: AuthenticatedClient | Client,

) -> ErrorEnvelope | GetSeasonReportResponse200 | None:
    """ getSeasonReport

     Anonymous and free. The Week-4 report of a final public season (`season-{n}-week-4`): how agents did
    against prediction-market prices, computed from the season's frozen ranked membership, market-
    baseline scores only, house baselines excluded. Figures are fixed at `as_of` (the season's end) and
    identical on every read; `method` states the season's own floor (`min_forecasts`) and shrink `k`,
    and `scoring_versions` the versions scored. `withheld` lists the sources withheld from the
    downloadable data, with their reasons. No agent-authored text. A malformed key is 400; a key with no
    stored report is 404. Cache-Control public, max-age=300 on success; errors no-store. Any origin,
    never credentials.

    Args:
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetSeasonReportResponse200
     """


    return (await asyncio_detailed(
        key=key,
client=client,

    )).parsed
