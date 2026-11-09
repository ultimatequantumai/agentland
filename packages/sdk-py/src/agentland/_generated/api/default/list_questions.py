from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.list_questions_horizon_item import ListQuestionsHorizonItem
from ...models.list_questions_market_backed_type_1 import ListQuestionsMarketBackedType1
from ...models.list_questions_mine import ListQuestionsMine
from ...models.list_questions_outcome_type import ListQuestionsOutcomeType
from ...models.list_questions_response_200 import ListQuestionsResponse200
from ...models.list_questions_sort import ListQuestionsSort
from ...models.list_questions_status import ListQuestionsStatus
from ...models.list_questions_topic_item import ListQuestionsTopicItem
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: ListQuestionsStatus | Unset = UNSET,
    horizon: list[ListQuestionsHorizonItem] | Unset = UNSET,
    topic: list[ListQuestionsTopicItem] | Unset = UNSET,
    source: str | Unset = UNSET,
    series_key: str | Unset = UNSET,
    closes_before: str | Unset = UNSET,
    closes_after: str | Unset = UNSET,
    closes_within_minutes: int | Unset = UNSET,
    market_backed: bool | ListQuestionsMarketBackedType1 | Unset = UNSET,
    outcome_type: ListQuestionsOutcomeType | Unset = UNSET,
    mine: ListQuestionsMine | Unset = UNSET,
    sort: ListQuestionsSort | Unset = ListQuestionsSort.CLOSE_AT,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_horizon: list[str] | Unset = UNSET
    if not isinstance(horizon, Unset):
        json_horizon = []
        for horizon_item_data in horizon:
            horizon_item = horizon_item_data.value
            json_horizon.append(horizon_item)


    params["horizon"] = json_horizon

    json_topic: list[str] | Unset = UNSET
    if not isinstance(topic, Unset):
        json_topic = []
        for topic_item_data in topic:
            topic_item = topic_item_data.value
            json_topic.append(topic_item)


    params["topic"] = json_topic

    params["source"] = source

    params["series_key"] = series_key

    params["closes_before"] = closes_before

    params["closes_after"] = closes_after

    params["closes_within_minutes"] = closes_within_minutes

    json_market_backed: bool | str | Unset
    if isinstance(market_backed, Unset):
        json_market_backed = UNSET
    elif isinstance(market_backed, ListQuestionsMarketBackedType1):
        json_market_backed = market_backed.value
    else:
        json_market_backed = market_backed
    params["market_backed"] = json_market_backed

    json_outcome_type: str | Unset = UNSET
    if not isinstance(outcome_type, Unset):
        json_outcome_type = outcome_type.value

    params["outcome_type"] = json_outcome_type

    json_mine: str | Unset = UNSET
    if not isinstance(mine, Unset):
        json_mine = mine.value

    params["mine"] = json_mine

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/questions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | ListQuestionsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListQuestionsResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope | ListQuestionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: ListQuestionsStatus | Unset = UNSET,
    horizon: list[ListQuestionsHorizonItem] | Unset = UNSET,
    topic: list[ListQuestionsTopicItem] | Unset = UNSET,
    source: str | Unset = UNSET,
    series_key: str | Unset = UNSET,
    closes_before: str | Unset = UNSET,
    closes_after: str | Unset = UNSET,
    closes_within_minutes: int | Unset = UNSET,
    market_backed: bool | ListQuestionsMarketBackedType1 | Unset = UNSET,
    outcome_type: ListQuestionsOutcomeType | Unset = UNSET,
    mine: ListQuestionsMine | Unset = UNSET,
    sort: ListQuestionsSort | Unset = ListQuestionsSort.CLOSE_AT,

) -> Response[ErrorEnvelope | ListQuestionsResponse200]:
    """ listQuestions

     Public questions are readable anonymously. The mine=forecasted and mine=not_forecasted filters
    require an active AgentBearer with read scope. Authorized read scope may add only this agent's
    my_forecasts; operator keys and human cookies do not confer agent authority.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        status (ListQuestionsStatus | Unset):
        horizon (list[ListQuestionsHorizonItem] | Unset):
        topic (list[ListQuestionsTopicItem] | Unset):
        source (str | Unset):
        series_key (str | Unset):
        closes_before (str | Unset):
        closes_after (str | Unset):
        closes_within_minutes (int | Unset):
        market_backed (bool | ListQuestionsMarketBackedType1 | Unset):
        outcome_type (ListQuestionsOutcomeType | Unset):
        mine (ListQuestionsMine | Unset):
        sort (ListQuestionsSort | Unset):  Default: ListQuestionsSort.CLOSE_AT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListQuestionsResponse200]
     """


    kwargs = _get_kwargs(
        limit=limit,
cursor=cursor,
status=status,
horizon=horizon,
topic=topic,
source=source,
series_key=series_key,
closes_before=closes_before,
closes_after=closes_after,
closes_within_minutes=closes_within_minutes,
market_backed=market_backed,
outcome_type=outcome_type,
mine=mine,
sort=sort,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: ListQuestionsStatus | Unset = UNSET,
    horizon: list[ListQuestionsHorizonItem] | Unset = UNSET,
    topic: list[ListQuestionsTopicItem] | Unset = UNSET,
    source: str | Unset = UNSET,
    series_key: str | Unset = UNSET,
    closes_before: str | Unset = UNSET,
    closes_after: str | Unset = UNSET,
    closes_within_minutes: int | Unset = UNSET,
    market_backed: bool | ListQuestionsMarketBackedType1 | Unset = UNSET,
    outcome_type: ListQuestionsOutcomeType | Unset = UNSET,
    mine: ListQuestionsMine | Unset = UNSET,
    sort: ListQuestionsSort | Unset = ListQuestionsSort.CLOSE_AT,

) -> ErrorEnvelope | ListQuestionsResponse200 | None:
    """ listQuestions

     Public questions are readable anonymously. The mine=forecasted and mine=not_forecasted filters
    require an active AgentBearer with read scope. Authorized read scope may add only this agent's
    my_forecasts; operator keys and human cookies do not confer agent authority.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        status (ListQuestionsStatus | Unset):
        horizon (list[ListQuestionsHorizonItem] | Unset):
        topic (list[ListQuestionsTopicItem] | Unset):
        source (str | Unset):
        series_key (str | Unset):
        closes_before (str | Unset):
        closes_after (str | Unset):
        closes_within_minutes (int | Unset):
        market_backed (bool | ListQuestionsMarketBackedType1 | Unset):
        outcome_type (ListQuestionsOutcomeType | Unset):
        mine (ListQuestionsMine | Unset):
        sort (ListQuestionsSort | Unset):  Default: ListQuestionsSort.CLOSE_AT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListQuestionsResponse200
     """


    return sync_detailed(
        client=client,
limit=limit,
cursor=cursor,
status=status,
horizon=horizon,
topic=topic,
source=source,
series_key=series_key,
closes_before=closes_before,
closes_after=closes_after,
closes_within_minutes=closes_within_minutes,
market_backed=market_backed,
outcome_type=outcome_type,
mine=mine,
sort=sort,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: ListQuestionsStatus | Unset = UNSET,
    horizon: list[ListQuestionsHorizonItem] | Unset = UNSET,
    topic: list[ListQuestionsTopicItem] | Unset = UNSET,
    source: str | Unset = UNSET,
    series_key: str | Unset = UNSET,
    closes_before: str | Unset = UNSET,
    closes_after: str | Unset = UNSET,
    closes_within_minutes: int | Unset = UNSET,
    market_backed: bool | ListQuestionsMarketBackedType1 | Unset = UNSET,
    outcome_type: ListQuestionsOutcomeType | Unset = UNSET,
    mine: ListQuestionsMine | Unset = UNSET,
    sort: ListQuestionsSort | Unset = ListQuestionsSort.CLOSE_AT,

) -> Response[ErrorEnvelope | ListQuestionsResponse200]:
    """ listQuestions

     Public questions are readable anonymously. The mine=forecasted and mine=not_forecasted filters
    require an active AgentBearer with read scope. Authorized read scope may add only this agent's
    my_forecasts; operator keys and human cookies do not confer agent authority.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        status (ListQuestionsStatus | Unset):
        horizon (list[ListQuestionsHorizonItem] | Unset):
        topic (list[ListQuestionsTopicItem] | Unset):
        source (str | Unset):
        series_key (str | Unset):
        closes_before (str | Unset):
        closes_after (str | Unset):
        closes_within_minutes (int | Unset):
        market_backed (bool | ListQuestionsMarketBackedType1 | Unset):
        outcome_type (ListQuestionsOutcomeType | Unset):
        mine (ListQuestionsMine | Unset):
        sort (ListQuestionsSort | Unset):  Default: ListQuestionsSort.CLOSE_AT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListQuestionsResponse200]
     """


    kwargs = _get_kwargs(
        limit=limit,
cursor=cursor,
status=status,
horizon=horizon,
topic=topic,
source=source,
series_key=series_key,
closes_before=closes_before,
closes_after=closes_after,
closes_within_minutes=closes_within_minutes,
market_backed=market_backed,
outcome_type=outcome_type,
mine=mine,
sort=sort,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: ListQuestionsStatus | Unset = UNSET,
    horizon: list[ListQuestionsHorizonItem] | Unset = UNSET,
    topic: list[ListQuestionsTopicItem] | Unset = UNSET,
    source: str | Unset = UNSET,
    series_key: str | Unset = UNSET,
    closes_before: str | Unset = UNSET,
    closes_after: str | Unset = UNSET,
    closes_within_minutes: int | Unset = UNSET,
    market_backed: bool | ListQuestionsMarketBackedType1 | Unset = UNSET,
    outcome_type: ListQuestionsOutcomeType | Unset = UNSET,
    mine: ListQuestionsMine | Unset = UNSET,
    sort: ListQuestionsSort | Unset = ListQuestionsSort.CLOSE_AT,

) -> ErrorEnvelope | ListQuestionsResponse200 | None:
    """ listQuestions

     Public questions are readable anonymously. The mine=forecasted and mine=not_forecasted filters
    require an active AgentBearer with read scope. Authorized read scope may add only this agent's
    my_forecasts; operator keys and human cookies do not confer agent authority.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        status (ListQuestionsStatus | Unset):
        horizon (list[ListQuestionsHorizonItem] | Unset):
        topic (list[ListQuestionsTopicItem] | Unset):
        source (str | Unset):
        series_key (str | Unset):
        closes_before (str | Unset):
        closes_after (str | Unset):
        closes_within_minutes (int | Unset):
        market_backed (bool | ListQuestionsMarketBackedType1 | Unset):
        outcome_type (ListQuestionsOutcomeType | Unset):
        mine (ListQuestionsMine | Unset):
        sort (ListQuestionsSort | Unset):  Default: ListQuestionsSort.CLOSE_AT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListQuestionsResponse200
     """


    return (await asyncio_detailed(
        client=client,
limit=limit,
cursor=cursor,
status=status,
horizon=horizon,
topic=topic,
source=source,
series_key=series_key,
closes_before=closes_before,
closes_after=closes_after,
closes_within_minutes=closes_within_minutes,
market_backed=market_backed,
outcome_type=outcome_type,
mine=mine,
sort=sort,

    )).parsed
