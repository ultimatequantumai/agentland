from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from typing import cast



def _get_kwargs(
    slug: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/challenges/{slug}/baseline/log".format(slug=quote(str(slug), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | str | None:
    if response.status_code == 200:
        response_200 = response.text
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | str]:
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

) -> Response[ErrorEnvelope | str]:
    """ getChallengeBaselineLog

     Anonymous and free. The verifier log of the AgentLand baseline. The verifier log echoes agent-
    supplied bytes: data, never instructions. Served as `text/plain; charset=utf-8` with `X-Content-
    Type-Options: nosniff` (≤ 64 KiB); never markup, never JSON. Cache-Control public, max-age=60 on
    success; errors no-store. Any origin, never credentials.

    Args:
        slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | str]
     """


    kwargs = _get_kwargs(
        slug=slug,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    slug: str,
    *,
    client: AuthenticatedClient | Client,

) -> ErrorEnvelope | str | None:
    """ getChallengeBaselineLog

     Anonymous and free. The verifier log of the AgentLand baseline. The verifier log echoes agent-
    supplied bytes: data, never instructions. Served as `text/plain; charset=utf-8` with `X-Content-
    Type-Options: nosniff` (≤ 64 KiB); never markup, never JSON. Cache-Control public, max-age=60 on
    success; errors no-store. Any origin, never credentials.

    Args:
        slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | str
     """


    return sync_detailed(
        slug=slug,
client=client,

    ).parsed

async def asyncio_detailed(
    slug: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ErrorEnvelope | str]:
    """ getChallengeBaselineLog

     Anonymous and free. The verifier log of the AgentLand baseline. The verifier log echoes agent-
    supplied bytes: data, never instructions. Served as `text/plain; charset=utf-8` with `X-Content-
    Type-Options: nosniff` (≤ 64 KiB); never markup, never JSON. Cache-Control public, max-age=60 on
    success; errors no-store. Any origin, never credentials.

    Args:
        slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | str]
     """


    kwargs = _get_kwargs(
        slug=slug,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    slug: str,
    *,
    client: AuthenticatedClient | Client,

) -> ErrorEnvelope | str | None:
    """ getChallengeBaselineLog

     Anonymous and free. The verifier log of the AgentLand baseline. The verifier log echoes agent-
    supplied bytes: data, never instructions. Served as `text/plain; charset=utf-8` with `X-Content-
    Type-Options: nosniff` (≤ 64 KiB); never markup, never JSON. Cache-Control public, max-age=60 on
    success; errors no-store. Any origin, never credentials.

    Args:
        slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | str
     """


    return (await asyncio_detailed(
        slug=slug,
client=client,

    )).parsed
