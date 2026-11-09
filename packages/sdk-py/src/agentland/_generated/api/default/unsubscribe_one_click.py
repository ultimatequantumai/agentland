from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.unsubscribe_one_click_data_body import UnsubscribeOneClickDataBody
from ...models.unsubscribe_one_click_files_body import UnsubscribeOneClickFilesBody
from ...models.unsubscribe_one_click_response_200 import UnsubscribeOneClickResponse200
from typing import cast



def _get_kwargs(
    token: str,
    *,
    body:    UnsubscribeOneClickDataBody  |     UnsubscribeOneClickFilesBody  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/mail/unsubscribe/{token}".format(token=quote(str(token), safe=""),),
    }

    if isinstance(body, UnsubscribeOneClickDataBody):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UnsubscribeOneClickFilesBody):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | UnsubscribeOneClickResponse200 | None:
    if response.status_code == 200:
        response_200 = UnsubscribeOneClickResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = ErrorEnvelope.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | UnsubscribeOneClickResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    token: str,
    *,
    client: AuthenticatedClient | Client,
    body:    UnsubscribeOneClickDataBody  |     UnsubscribeOneClickFilesBody  | Unset = UNSET,

) -> Response[ErrorEnvelope | UnsubscribeOneClickResponse200]:
    """ unsubscribeOneClick

     RFC 8058 one-click unsubscribe, the `List-Unsubscribe` target of every retention email. Anonymous:
    an `Authorization` header is never resolved (never 401) and the request uses the anonymous IP rate
    bucket. Accepts `application/x-www-form-urlencoded` and `multipart/form-data` bodies of `List-
    Unsubscribe=One-Click`. Always 200 `no-store` JSON, never a redirect: a valid token turns off
    exactly its category and answers `{category}`; a forged, malformed or expired-secret token, or any
    other body, answers `{category: null}` and changes nothing. `Idempotency-Key` is honoured if sent
    but never required (mail clients send none); replay-safe.

    Args:
        token (str):
        body (UnsubscribeOneClickDataBody): RFC 8058 one-click body `List-Unsubscribe=One-Click`.
        body (UnsubscribeOneClickFilesBody): RFC 8058 one-click body `List-Unsubscribe=One-Click`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | UnsubscribeOneClickResponse200]
     """


    kwargs = _get_kwargs(
        token=token,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    token: str,
    *,
    client: AuthenticatedClient | Client,
    body:    UnsubscribeOneClickDataBody  |     UnsubscribeOneClickFilesBody  | Unset = UNSET,

) -> ErrorEnvelope | UnsubscribeOneClickResponse200 | None:
    """ unsubscribeOneClick

     RFC 8058 one-click unsubscribe, the `List-Unsubscribe` target of every retention email. Anonymous:
    an `Authorization` header is never resolved (never 401) and the request uses the anonymous IP rate
    bucket. Accepts `application/x-www-form-urlencoded` and `multipart/form-data` bodies of `List-
    Unsubscribe=One-Click`. Always 200 `no-store` JSON, never a redirect: a valid token turns off
    exactly its category and answers `{category}`; a forged, malformed or expired-secret token, or any
    other body, answers `{category: null}` and changes nothing. `Idempotency-Key` is honoured if sent
    but never required (mail clients send none); replay-safe.

    Args:
        token (str):
        body (UnsubscribeOneClickDataBody): RFC 8058 one-click body `List-Unsubscribe=One-Click`.
        body (UnsubscribeOneClickFilesBody): RFC 8058 one-click body `List-Unsubscribe=One-Click`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | UnsubscribeOneClickResponse200
     """


    return sync_detailed(
        token=token,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    token: str,
    *,
    client: AuthenticatedClient | Client,
    body:    UnsubscribeOneClickDataBody  |     UnsubscribeOneClickFilesBody  | Unset = UNSET,

) -> Response[ErrorEnvelope | UnsubscribeOneClickResponse200]:
    """ unsubscribeOneClick

     RFC 8058 one-click unsubscribe, the `List-Unsubscribe` target of every retention email. Anonymous:
    an `Authorization` header is never resolved (never 401) and the request uses the anonymous IP rate
    bucket. Accepts `application/x-www-form-urlencoded` and `multipart/form-data` bodies of `List-
    Unsubscribe=One-Click`. Always 200 `no-store` JSON, never a redirect: a valid token turns off
    exactly its category and answers `{category}`; a forged, malformed or expired-secret token, or any
    other body, answers `{category: null}` and changes nothing. `Idempotency-Key` is honoured if sent
    but never required (mail clients send none); replay-safe.

    Args:
        token (str):
        body (UnsubscribeOneClickDataBody): RFC 8058 one-click body `List-Unsubscribe=One-Click`.
        body (UnsubscribeOneClickFilesBody): RFC 8058 one-click body `List-Unsubscribe=One-Click`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | UnsubscribeOneClickResponse200]
     """


    kwargs = _get_kwargs(
        token=token,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    token: str,
    *,
    client: AuthenticatedClient | Client,
    body:    UnsubscribeOneClickDataBody  |     UnsubscribeOneClickFilesBody  | Unset = UNSET,

) -> ErrorEnvelope | UnsubscribeOneClickResponse200 | None:
    """ unsubscribeOneClick

     RFC 8058 one-click unsubscribe, the `List-Unsubscribe` target of every retention email. Anonymous:
    an `Authorization` header is never resolved (never 401) and the request uses the anonymous IP rate
    bucket. Accepts `application/x-www-form-urlencoded` and `multipart/form-data` bodies of `List-
    Unsubscribe=One-Click`. Always 200 `no-store` JSON, never a redirect: a valid token turns off
    exactly its category and answers `{category}`; a forged, malformed or expired-secret token, or any
    other body, answers `{category: null}` and changes nothing. `Idempotency-Key` is honoured if sent
    but never required (mail clients send none); replay-safe.

    Args:
        token (str):
        body (UnsubscribeOneClickDataBody): RFC 8058 one-click body `List-Unsubscribe=One-Click`.
        body (UnsubscribeOneClickFilesBody): RFC 8058 one-click body `List-Unsubscribe=One-Click`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | UnsubscribeOneClickResponse200
     """


    return (await asyncio_detailed(
        token=token,
client=client,
body=body,

    )).parsed
