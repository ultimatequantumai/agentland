from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_questions_response_200_data_item_horizon import ListQuestionsResponse200DataItemHorizon
from ..models.list_questions_response_200_data_item_outcome_type import ListQuestionsResponse200DataItemOutcomeType
from ..models.list_questions_response_200_data_item_status import ListQuestionsResponse200DataItemStatus
from ..models.list_questions_response_200_data_item_topic import ListQuestionsResponse200DataItemTopic
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.list_questions_response_200_data_item_market_type_0 import ListQuestionsResponse200DataItemMarketType0
  from ..models.list_questions_response_200_data_item_market_type_1 import ListQuestionsResponse200DataItemMarketType1
  from ..models.list_questions_response_200_data_item_my_forecasts_item import ListQuestionsResponse200DataItemMyForecastsItem
  from ..models.list_questions_response_200_data_item_numeric_type_0 import ListQuestionsResponse200DataItemNumericType0
  from ..models.list_questions_response_200_data_item_resolution_type_0 import ListQuestionsResponse200DataItemResolutionType0





T = TypeVar("T", bound="ListQuestionsResponse200DataItem")



@_attrs_define
class ListQuestionsResponse200DataItem:
    """ 
        Attributes:
            id (UUID):
            slug (str):
            title (str):
            description (str):
            resolution_criteria (str):
            resolution_source_url (str):
            topic (ListQuestionsResponse200DataItemTopic):
            tags (list[str]):
            horizon (ListQuestionsResponse200DataItemHorizon):
            source (str):
            source_ref (str):
            series_key (None | str):
            source_market_url (None | str):
            outcome_type (ListQuestionsResponse200DataItemOutcomeType):
            numeric (ListQuestionsResponse200DataItemNumericType0 | None):
            outcomes (list[Any]):
            open_at (str):
            close_at (str):
            expected_resolve_at (str):
            market_backed (bool):
            market (ListQuestionsResponse200DataItemMarketType0 | ListQuestionsResponse200DataItemMarketType1 | None):
            forecast_count (int):
            resolution (ListQuestionsResponse200DataItemResolutionType0 | None):
            status (ListQuestionsResponse200DataItemStatus):
            my_forecasts (list[ListQuestionsResponse200DataItemMyForecastsItem] | Unset):
     """

    id: UUID
    slug: str
    title: str
    description: str
    resolution_criteria: str
    resolution_source_url: str
    topic: ListQuestionsResponse200DataItemTopic
    tags: list[str]
    horizon: ListQuestionsResponse200DataItemHorizon
    source: str
    source_ref: str
    series_key: None | str
    source_market_url: None | str
    outcome_type: ListQuestionsResponse200DataItemOutcomeType
    numeric: ListQuestionsResponse200DataItemNumericType0 | None
    outcomes: list[Any]
    open_at: str
    close_at: str
    expected_resolve_at: str
    market_backed: bool
    market: ListQuestionsResponse200DataItemMarketType0 | ListQuestionsResponse200DataItemMarketType1 | None
    forecast_count: int
    resolution: ListQuestionsResponse200DataItemResolutionType0 | None
    status: ListQuestionsResponse200DataItemStatus
    my_forecasts: list[ListQuestionsResponse200DataItemMyForecastsItem] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_questions_response_200_data_item_market_type_0 import ListQuestionsResponse200DataItemMarketType0 # noqa: PLC0415
        from ..models.list_questions_response_200_data_item_market_type_1 import ListQuestionsResponse200DataItemMarketType1 # noqa: PLC0415
        from ..models.list_questions_response_200_data_item_my_forecasts_item import ListQuestionsResponse200DataItemMyForecastsItem # noqa: PLC0415
        from ..models.list_questions_response_200_data_item_numeric_type_0 import ListQuestionsResponse200DataItemNumericType0 # noqa: PLC0415
        from ..models.list_questions_response_200_data_item_resolution_type_0 import ListQuestionsResponse200DataItemResolutionType0 # noqa: PLC0415
        id = str(self.id)

        slug = self.slug

        title = self.title

        description = self.description

        resolution_criteria = self.resolution_criteria

        resolution_source_url = self.resolution_source_url

        topic = self.topic.value

        tags = self.tags



        horizon = self.horizon.value

        source = self.source

        source_ref = self.source_ref

        series_key: None | str
        series_key = self.series_key

        source_market_url: None | str
        source_market_url = self.source_market_url

        outcome_type = self.outcome_type.value

        numeric: dict[str, Any] | None
        if isinstance(self.numeric, ListQuestionsResponse200DataItemNumericType0):
            numeric = self.numeric.to_dict()
        else:
            numeric = self.numeric

        outcomes = self.outcomes



        open_at = self.open_at

        close_at = self.close_at

        expected_resolve_at = self.expected_resolve_at

        market_backed = self.market_backed

        market: dict[str, Any] | None
        if isinstance(self.market, ListQuestionsResponse200DataItemMarketType0):
            market = self.market.to_dict()
        elif isinstance(self.market, ListQuestionsResponse200DataItemMarketType1):
            market = self.market.to_dict()
        else:
            market = self.market

        forecast_count = self.forecast_count

        resolution: dict[str, Any] | None
        if isinstance(self.resolution, ListQuestionsResponse200DataItemResolutionType0):
            resolution = self.resolution.to_dict()
        else:
            resolution = self.resolution

        status = self.status.value

        my_forecasts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.my_forecasts, Unset):
            my_forecasts = []
            for my_forecasts_item_data in self.my_forecasts:
                my_forecasts_item = my_forecasts_item_data.to_dict()
                my_forecasts.append(my_forecasts_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "slug": slug,
            "title": title,
            "description": description,
            "resolution_criteria": resolution_criteria,
            "resolution_source_url": resolution_source_url,
            "topic": topic,
            "tags": tags,
            "horizon": horizon,
            "source": source,
            "source_ref": source_ref,
            "series_key": series_key,
            "source_market_url": source_market_url,
            "outcome_type": outcome_type,
            "numeric": numeric,
            "outcomes": outcomes,
            "open_at": open_at,
            "close_at": close_at,
            "expected_resolve_at": expected_resolve_at,
            "market_backed": market_backed,
            "market": market,
            "forecast_count": forecast_count,
            "resolution": resolution,
            "status": status,
        })
        if my_forecasts is not UNSET:
            field_dict["my_forecasts"] = my_forecasts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_questions_response_200_data_item_market_type_0 import ListQuestionsResponse200DataItemMarketType0 # noqa: PLC0415
        from ..models.list_questions_response_200_data_item_market_type_1 import ListQuestionsResponse200DataItemMarketType1 # noqa: PLC0415
        from ..models.list_questions_response_200_data_item_my_forecasts_item import ListQuestionsResponse200DataItemMyForecastsItem # noqa: PLC0415
        from ..models.list_questions_response_200_data_item_numeric_type_0 import ListQuestionsResponse200DataItemNumericType0 # noqa: PLC0415
        from ..models.list_questions_response_200_data_item_resolution_type_0 import ListQuestionsResponse200DataItemResolutionType0 # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        slug = d.pop("slug")

        title = d.pop("title")

        description = d.pop("description")

        resolution_criteria = d.pop("resolution_criteria")

        resolution_source_url = d.pop("resolution_source_url")

        topic = ListQuestionsResponse200DataItemTopic(d.pop("topic"))




        tags = cast(list[str], d.pop("tags"))


        horizon = ListQuestionsResponse200DataItemHorizon(d.pop("horizon"))




        source = d.pop("source")

        source_ref = d.pop("source_ref")

        def _parse_series_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        series_key = _parse_series_key(d.pop("series_key"))


        def _parse_source_market_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_market_url = _parse_source_market_url(d.pop("source_market_url"))


        outcome_type = ListQuestionsResponse200DataItemOutcomeType(d.pop("outcome_type"))




        def _parse_numeric(data: object) -> ListQuestionsResponse200DataItemNumericType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                numeric_type_0 = ListQuestionsResponse200DataItemNumericType0.from_dict(data)



                return numeric_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListQuestionsResponse200DataItemNumericType0 | None, data)

        numeric = _parse_numeric(d.pop("numeric"))


        outcomes = cast(list[Any], d.pop("outcomes"))


        open_at = d.pop("open_at")

        close_at = d.pop("close_at")

        expected_resolve_at = d.pop("expected_resolve_at")

        market_backed = d.pop("market_backed")

        def _parse_market(data: object) -> ListQuestionsResponse200DataItemMarketType0 | ListQuestionsResponse200DataItemMarketType1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                market_type_0 = ListQuestionsResponse200DataItemMarketType0.from_dict(data)



                return market_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                market_type_1 = ListQuestionsResponse200DataItemMarketType1.from_dict(data)



                return market_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListQuestionsResponse200DataItemMarketType0 | ListQuestionsResponse200DataItemMarketType1 | None, data)

        market = _parse_market(d.pop("market"))


        forecast_count = d.pop("forecast_count")

        def _parse_resolution(data: object) -> ListQuestionsResponse200DataItemResolutionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resolution_type_0 = ListQuestionsResponse200DataItemResolutionType0.from_dict(data)



                return resolution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListQuestionsResponse200DataItemResolutionType0 | None, data)

        resolution = _parse_resolution(d.pop("resolution"))


        status = ListQuestionsResponse200DataItemStatus(d.pop("status"))




        _my_forecasts = d.pop("my_forecasts", UNSET)
        my_forecasts: list[ListQuestionsResponse200DataItemMyForecastsItem] | Unset = UNSET
        if _my_forecasts is not UNSET:
            my_forecasts = []
            for my_forecasts_item_data in _my_forecasts:
                my_forecasts_item = ListQuestionsResponse200DataItemMyForecastsItem.from_dict(my_forecasts_item_data)



                my_forecasts.append(my_forecasts_item)


        list_questions_response_200_data_item = cls(
            id=id,
            slug=slug,
            title=title,
            description=description,
            resolution_criteria=resolution_criteria,
            resolution_source_url=resolution_source_url,
            topic=topic,
            tags=tags,
            horizon=horizon,
            source=source,
            source_ref=source_ref,
            series_key=series_key,
            source_market_url=source_market_url,
            outcome_type=outcome_type,
            numeric=numeric,
            outcomes=outcomes,
            open_at=open_at,
            close_at=close_at,
            expected_resolve_at=expected_resolve_at,
            market_backed=market_backed,
            market=market,
            forecast_count=forecast_count,
            resolution=resolution,
            status=status,
            my_forecasts=my_forecasts,
        )

        return list_questions_response_200_data_item

