from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.update_session_body import UpdateSessionBody
from ...models.update_session_response_200 import UpdateSessionResponse200
from ...models.update_session_response_400 import UpdateSessionResponse400
from ...models.update_session_response_401 import UpdateSessionResponse401
from ...models.update_session_response_403 import UpdateSessionResponse403
from ...models.update_session_response_404 import UpdateSessionResponse404
from ...models.update_session_response_429 import UpdateSessionResponse429
from ...models.update_session_response_500 import UpdateSessionResponse500
from typing import cast



def _get_kwargs(
    *,
    body: UpdateSessionBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/update-session",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdateSessionResponse200 | UpdateSessionResponse400 | UpdateSessionResponse401 | UpdateSessionResponse403 | UpdateSessionResponse404 | UpdateSessionResponse429 | UpdateSessionResponse500 | None:
    if response.status_code == 200:
        response_200 = UpdateSessionResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = UpdateSessionResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UpdateSessionResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = UpdateSessionResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = UpdateSessionResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = UpdateSessionResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = UpdateSessionResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpdateSessionResponse200 | UpdateSessionResponse400 | UpdateSessionResponse401 | UpdateSessionResponse403 | UpdateSessionResponse404 | UpdateSessionResponse429 | UpdateSessionResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateSessionBody,

) -> Response[UpdateSessionResponse200 | UpdateSessionResponse400 | UpdateSessionResponse401 | UpdateSessionResponse403 | UpdateSessionResponse404 | UpdateSessionResponse429 | UpdateSessionResponse500]:
    """  Update the current session

    Args:
        body (UpdateSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateSessionResponse200 | UpdateSessionResponse400 | UpdateSessionResponse401 | UpdateSessionResponse403 | UpdateSessionResponse404 | UpdateSessionResponse429 | UpdateSessionResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: UpdateSessionBody,

) -> UpdateSessionResponse200 | UpdateSessionResponse400 | UpdateSessionResponse401 | UpdateSessionResponse403 | UpdateSessionResponse404 | UpdateSessionResponse429 | UpdateSessionResponse500 | None:
    """  Update the current session

    Args:
        body (UpdateSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateSessionResponse200 | UpdateSessionResponse400 | UpdateSessionResponse401 | UpdateSessionResponse403 | UpdateSessionResponse404 | UpdateSessionResponse429 | UpdateSessionResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateSessionBody,

) -> Response[UpdateSessionResponse200 | UpdateSessionResponse400 | UpdateSessionResponse401 | UpdateSessionResponse403 | UpdateSessionResponse404 | UpdateSessionResponse429 | UpdateSessionResponse500]:
    """  Update the current session

    Args:
        body (UpdateSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateSessionResponse200 | UpdateSessionResponse400 | UpdateSessionResponse401 | UpdateSessionResponse403 | UpdateSessionResponse404 | UpdateSessionResponse429 | UpdateSessionResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdateSessionBody,

) -> UpdateSessionResponse200 | UpdateSessionResponse400 | UpdateSessionResponse401 | UpdateSessionResponse403 | UpdateSessionResponse404 | UpdateSessionResponse429 | UpdateSessionResponse500 | None:
    """  Update the current session

    Args:
        body (UpdateSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateSessionResponse200 | UpdateSessionResponse400 | UpdateSessionResponse401 | UpdateSessionResponse403 | UpdateSessionResponse404 | UpdateSessionResponse429 | UpdateSessionResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
