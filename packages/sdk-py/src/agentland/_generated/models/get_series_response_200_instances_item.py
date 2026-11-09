from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_series_response_200_instances_item_outcome_type_1 import GetSeriesResponse200InstancesItemOutcomeType1
from ..models.get_series_response_200_instances_item_outcome_type_2_type_1 import GetSeriesResponse200InstancesItemOutcomeType2Type1
from ..models.get_series_response_200_instances_item_outcome_type_3_type_1 import GetSeriesResponse200InstancesItemOutcomeType3Type1
from ..models.get_series_response_200_instances_item_status import GetSeriesResponse200InstancesItemStatus
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_series_response_200_instances_item_market_item import GetSeriesResponse200InstancesItemMarketItem





T = TypeVar("T", bound="GetSeriesResponse200InstancesItem")



@_attrs_define
class GetSeriesResponse200InstancesItem:
    """ 
        Attributes:
            id (UUID):
            slug (str):
            title (str):
            status (GetSeriesResponse200InstancesItemStatus):
            open_at (str):
            close_at (str):
            expected_resolve_at (str):
            resolution_source_url (str):
            market (list[GetSeriesResponse200InstancesItemMarketItem]):
            outcome (GetSeriesResponse200InstancesItemOutcomeType1 | GetSeriesResponse200InstancesItemOutcomeType2Type1 |
                GetSeriesResponse200InstancesItemOutcomeType3Type1 | None):
            resolved_at (None | str):
     """

    id: UUID
    slug: str
    title: str
    status: GetSeriesResponse200InstancesItemStatus
    open_at: str
    close_at: str
    expected_resolve_at: str
    resolution_source_url: str
    market: list[GetSeriesResponse200InstancesItemMarketItem]
    outcome: GetSeriesResponse200InstancesItemOutcomeType1 | GetSeriesResponse200InstancesItemOutcomeType2Type1 | GetSeriesResponse200InstancesItemOutcomeType3Type1 | None
    resolved_at: None | str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_series_response_200_instances_item_market_item import GetSeriesResponse200InstancesItemMarketItem # noqa: PLC0415
        id = str(self.id)

        slug = self.slug

        title = self.title

        status = self.status.value

        open_at = self.open_at

        close_at = self.close_at

        expected_resolve_at = self.expected_resolve_at

        resolution_source_url = self.resolution_source_url

        market = []
        for market_item_data in self.market:
            market_item = market_item_data.to_dict()
            market.append(market_item)



        outcome: None | str
        if isinstance(self.outcome, GetSeriesResponse200InstancesItemOutcomeType1):
            outcome = self.outcome.value
        elif isinstance(self.outcome, GetSeriesResponse200InstancesItemOutcomeType2Type1):
            outcome = self.outcome.value
        elif isinstance(self.outcome, GetSeriesResponse200InstancesItemOutcomeType3Type1):
            outcome = self.outcome.value
        else:
            outcome = self.outcome

        resolved_at: None | str
        resolved_at = self.resolved_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "slug": slug,
            "title": title,
            "status": status,
            "open_at": open_at,
            "close_at": close_at,
            "expected_resolve_at": expected_resolve_at,
            "resolution_source_url": resolution_source_url,
            "market": market,
            "outcome": outcome,
            "resolved_at": resolved_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_series_response_200_instances_item_market_item import GetSeriesResponse200InstancesItemMarketItem # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        slug = d.pop("slug")

        title = d.pop("title")

        status = GetSeriesResponse200InstancesItemStatus(d.pop("status"))




        open_at = d.pop("open_at")

        close_at = d.pop("close_at")

        expected_resolve_at = d.pop("expected_resolve_at")

        resolution_source_url = d.pop("resolution_source_url")

        market = []
        _market = d.pop("market")
        for market_item_data in (_market):
            market_item = GetSeriesResponse200InstancesItemMarketItem.from_dict(market_item_data)



            market.append(market_item)


        def _parse_outcome(data: object) -> GetSeriesResponse200InstancesItemOutcomeType1 | GetSeriesResponse200InstancesItemOutcomeType2Type1 | GetSeriesResponse200InstancesItemOutcomeType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_type_1 = GetSeriesResponse200InstancesItemOutcomeType1(data)



                return outcome_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_type_2_type_1 = GetSeriesResponse200InstancesItemOutcomeType2Type1(data)



                return outcome_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_type_3_type_1 = GetSeriesResponse200InstancesItemOutcomeType3Type1(data)



                return outcome_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSeriesResponse200InstancesItemOutcomeType1 | GetSeriesResponse200InstancesItemOutcomeType2Type1 | GetSeriesResponse200InstancesItemOutcomeType3Type1 | None, data)

        outcome = _parse_outcome(d.pop("outcome"))


        def _parse_resolved_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at"))


        get_series_response_200_instances_item = cls(
            id=id,
            slug=slug,
            title=title,
            status=status,
            open_at=open_at,
            close_at=close_at,
            expected_resolve_at=expected_resolve_at,
            resolution_source_url=resolution_source_url,
            market=market,
            outcome=outcome,
            resolved_at=resolved_at,
        )

        return get_series_response_200_instances_item

