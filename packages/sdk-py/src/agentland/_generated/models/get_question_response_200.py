from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_question_response_200_horizon import GetQuestionResponse200Horizon
from ..models.get_question_response_200_outcome_type import GetQuestionResponse200OutcomeType
from ..models.get_question_response_200_status import GetQuestionResponse200Status
from ..models.get_question_response_200_topic import GetQuestionResponse200Topic
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_question_response_200_market_type_0 import GetQuestionResponse200MarketType0
  from ..models.get_question_response_200_market_type_1 import GetQuestionResponse200MarketType1
  from ..models.get_question_response_200_my_forecasts_item import GetQuestionResponse200MyForecastsItem
  from ..models.get_question_response_200_numeric_type_0 import GetQuestionResponse200NumericType0
  from ..models.get_question_response_200_resolution_type_0 import GetQuestionResponse200ResolutionType0





T = TypeVar("T", bound="GetQuestionResponse200")



@_attrs_define
class GetQuestionResponse200:
    """ 
        Attributes:
            id (UUID):
            slug (str):
            title (str):
            description (str):
            resolution_criteria (str):
            resolution_source_url (str):
            topic (GetQuestionResponse200Topic):
            tags (list[str]):
            horizon (GetQuestionResponse200Horizon):
            source (str):
            source_ref (str):
            series_key (None | str):
            source_market_url (None | str):
            outcome_type (GetQuestionResponse200OutcomeType):
            numeric (GetQuestionResponse200NumericType0 | None):
            outcomes (list[Any]):
            open_at (str):
            close_at (str):
            expected_resolve_at (str):
            market_backed (bool):
            market (GetQuestionResponse200MarketType0 | GetQuestionResponse200MarketType1 | None):
            forecast_count (int):
            resolution (GetQuestionResponse200ResolutionType0 | None):
            status (GetQuestionResponse200Status):
            my_forecasts (list[GetQuestionResponse200MyForecastsItem] | Unset):
     """

    id: UUID
    slug: str
    title: str
    description: str
    resolution_criteria: str
    resolution_source_url: str
    topic: GetQuestionResponse200Topic
    tags: list[str]
    horizon: GetQuestionResponse200Horizon
    source: str
    source_ref: str
    series_key: None | str
    source_market_url: None | str
    outcome_type: GetQuestionResponse200OutcomeType
    numeric: GetQuestionResponse200NumericType0 | None
    outcomes: list[Any]
    open_at: str
    close_at: str
    expected_resolve_at: str
    market_backed: bool
    market: GetQuestionResponse200MarketType0 | GetQuestionResponse200MarketType1 | None
    forecast_count: int
    resolution: GetQuestionResponse200ResolutionType0 | None
    status: GetQuestionResponse200Status
    my_forecasts: list[GetQuestionResponse200MyForecastsItem] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_question_response_200_market_type_0 import GetQuestionResponse200MarketType0 # noqa: PLC0415
        from ..models.get_question_response_200_market_type_1 import GetQuestionResponse200MarketType1 # noqa: PLC0415
        from ..models.get_question_response_200_my_forecasts_item import GetQuestionResponse200MyForecastsItem # noqa: PLC0415
        from ..models.get_question_response_200_numeric_type_0 import GetQuestionResponse200NumericType0 # noqa: PLC0415
        from ..models.get_question_response_200_resolution_type_0 import GetQuestionResponse200ResolutionType0 # noqa: PLC0415
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
        if isinstance(self.numeric, GetQuestionResponse200NumericType0):
            numeric = self.numeric.to_dict()
        else:
            numeric = self.numeric

        outcomes = self.outcomes



        open_at = self.open_at

        close_at = self.close_at

        expected_resolve_at = self.expected_resolve_at

        market_backed = self.market_backed

        market: dict[str, Any] | None
        if isinstance(self.market, GetQuestionResponse200MarketType0):
            market = self.market.to_dict()
        elif isinstance(self.market, GetQuestionResponse200MarketType1):
            market = self.market.to_dict()
        else:
            market = self.market

        forecast_count = self.forecast_count

        resolution: dict[str, Any] | None
        if isinstance(self.resolution, GetQuestionResponse200ResolutionType0):
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
        from ..models.get_question_response_200_market_type_0 import GetQuestionResponse200MarketType0 # noqa: PLC0415
        from ..models.get_question_response_200_market_type_1 import GetQuestionResponse200MarketType1 # noqa: PLC0415
        from ..models.get_question_response_200_my_forecasts_item import GetQuestionResponse200MyForecastsItem # noqa: PLC0415
        from ..models.get_question_response_200_numeric_type_0 import GetQuestionResponse200NumericType0 # noqa: PLC0415
        from ..models.get_question_response_200_resolution_type_0 import GetQuestionResponse200ResolutionType0 # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        slug = d.pop("slug")

        title = d.pop("title")

        description = d.pop("description")

        resolution_criteria = d.pop("resolution_criteria")

        resolution_source_url = d.pop("resolution_source_url")

        topic = GetQuestionResponse200Topic(d.pop("topic"))




        tags = cast(list[str], d.pop("tags"))


        horizon = GetQuestionResponse200Horizon(d.pop("horizon"))




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


        outcome_type = GetQuestionResponse200OutcomeType(d.pop("outcome_type"))




        def _parse_numeric(data: object) -> GetQuestionResponse200NumericType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                numeric_type_0 = GetQuestionResponse200NumericType0.from_dict(data)



                return numeric_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetQuestionResponse200NumericType0 | None, data)

        numeric = _parse_numeric(d.pop("numeric"))


        outcomes = cast(list[Any], d.pop("outcomes"))


        open_at = d.pop("open_at")

        close_at = d.pop("close_at")

        expected_resolve_at = d.pop("expected_resolve_at")

        market_backed = d.pop("market_backed")

        def _parse_market(data: object) -> GetQuestionResponse200MarketType0 | GetQuestionResponse200MarketType1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                market_type_0 = GetQuestionResponse200MarketType0.from_dict(data)



                return market_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                market_type_1 = GetQuestionResponse200MarketType1.from_dict(data)



                return market_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetQuestionResponse200MarketType0 | GetQuestionResponse200MarketType1 | None, data)

        market = _parse_market(d.pop("market"))


        forecast_count = d.pop("forecast_count")

        def _parse_resolution(data: object) -> GetQuestionResponse200ResolutionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resolution_type_0 = GetQuestionResponse200ResolutionType0.from_dict(data)



                return resolution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetQuestionResponse200ResolutionType0 | None, data)

        resolution = _parse_resolution(d.pop("resolution"))


        status = GetQuestionResponse200Status(d.pop("status"))




        _my_forecasts = d.pop("my_forecasts", UNSET)
        my_forecasts: list[GetQuestionResponse200MyForecastsItem] | Unset = UNSET
        if _my_forecasts is not UNSET:
            my_forecasts = []
            for my_forecasts_item_data in _my_forecasts:
                my_forecasts_item = GetQuestionResponse200MyForecastsItem.from_dict(my_forecasts_item_data)



                my_forecasts.append(my_forecasts_item)


        get_question_response_200 = cls(
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

        return get_question_response_200

