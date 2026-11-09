from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_api_auth_callback_id_body import PostApiAuthCallbackIdBody
from ...models.post_api_auth_callback_id_response_400 import PostApiAuthCallbackIdResponse400
from ...models.post_api_auth_callback_id_response_401 import PostApiAuthCallbackIdResponse401
from ...models.post_api_auth_callback_id_response_403 import PostApiAuthCallbackIdResponse403
from ...models.post_api_auth_callback_id_response_404 import PostApiAuthCallbackIdResponse404
from ...models.post_api_auth_callback_id_response_429 import PostApiAuthCallbackIdResponse429
from ...models.post_api_auth_callback_id_response_500 import PostApiAuthCallbackIdResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: PostApiAuthCallbackIdBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/callback/{id}".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostApiAuthCallbackIdResponse400 | PostApiAuthCallbackIdResponse401 | PostApiAuthCallbackIdResponse403 | PostApiAuthCallbackIdResponse404 | PostApiAuthCallbackIdResponse429 | PostApiAuthCallbackIdResponse500 | None:
    if response.status_code == 400:
        response_400 = PostApiAuthCallbackIdResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthCallbackIdResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthCallbackIdResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthCallbackIdResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthCallbackIdResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthCallbackIdResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostApiAuthCallbackIdResponse400 | PostApiAuthCallbackIdResponse401 | PostApiAuthCallbackIdResponse403 | PostApiAuthCallbackIdResponse404 | PostApiAuthCallbackIdResponse429 | PostApiAuthCallbackIdResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAuthCallbackIdBody | Unset = UNSET,

) -> Response[PostApiAuthCallbackIdResponse400 | PostApiAuthCallbackIdResponse401 | PostApiAuthCallbackIdResponse403 | PostApiAuthCallbackIdResponse404 | PostApiAuthCallbackIdResponse429 | PostApiAuthCallbackIdResponse500]:
    """ 
    Args:
        id (str):
        body (PostApiAuthCallbackIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthCallbackIdResponse400 | PostApiAuthCallbackIdResponse401 | PostApiAuthCallbackIdResponse403 | PostApiAuthCallbackIdResponse404 | PostApiAuthCallbackIdResponse429 | PostApiAuthCallbackIdResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAuthCallbackIdBody | Unset = UNSET,

) -> PostApiAuthCallbackIdResponse400 | PostApiAuthCallbackIdResponse401 | PostApiAuthCallbackIdResponse403 | PostApiAuthCallbackIdResponse404 | PostApiAuthCallbackIdResponse429 | PostApiAuthCallbackIdResponse500 | None:
    """ 
    Args:
        id (str):
        body (PostApiAuthCallbackIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthCallbackIdResponse400 | PostApiAuthCallbackIdResponse401 | PostApiAuthCallbackIdResponse403 | PostApiAuthCallbackIdResponse404 | PostApiAuthCallbackIdResponse429 | PostApiAuthCallbackIdResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAuthCallbackIdBody | Unset = UNSET,

) -> Response[PostApiAuthCallbackIdResponse400 | PostApiAuthCallbackIdResponse401 | PostApiAuthCallbackIdResponse403 | PostApiAuthCallbackIdResponse404 | PostApiAuthCallbackIdResponse429 | PostApiAuthCallbackIdResponse500]:
    """ 
    Args:
        id (str):
        body (PostApiAuthCallbackIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthCallbackIdResponse400 | PostApiAuthCallbackIdResponse401 | PostApiAuthCallbackIdResponse403 | PostApiAuthCallbackIdResponse404 | PostApiAuthCallbackIdResponse429 | PostApiAuthCallbackIdResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAuthCallbackIdBody | Unset = UNSET,

) -> PostApiAuthCallbackIdResponse400 | PostApiAuthCallbackIdResponse401 | PostApiAuthCallbackIdResponse403 | PostApiAuthCallbackIdResponse404 | PostApiAuthCallbackIdResponse429 | PostApiAuthCallbackIdResponse500 | None:
    """ 
    Args:
        id (str):
        body (PostApiAuthCallbackIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthCallbackIdResponse400 | PostApiAuthCallbackIdResponse401 | PostApiAuthCallbackIdResponse403 | PostApiAuthCallbackIdResponse404 | PostApiAuthCallbackIdResponse429 | PostApiAuthCallbackIdResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
