from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_daily_response_200_counts import GetDailyResponse200Counts
  from ..models.get_daily_response_200_resolved_item import GetDailyResponse200ResolvedItem
  from ..models.get_daily_response_200_series_item import GetDailyResponse200SeriesItem





T = TypeVar("T", bound="GetDailyResponse200")



@_attrs_define
class GetDailyResponse200:
    """ 
        Attributes:
            date (str):
            resolved (list[GetDailyResponse200ResolvedItem]):
            series (list[GetDailyResponse200SeriesItem]):
            counts (GetDailyResponse200Counts):
     """

    date: str
    resolved: list[GetDailyResponse200ResolvedItem]
    series: list[GetDailyResponse200SeriesItem]
    counts: GetDailyResponse200Counts





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_daily_response_200_counts import GetDailyResponse200Counts # noqa: PLC0415
        from ..models.get_daily_response_200_resolved_item import GetDailyResponse200ResolvedItem # noqa: PLC0415
        from ..models.get_daily_response_200_series_item import GetDailyResponse200SeriesItem # noqa: PLC0415
        date = self.date

        resolved = []
        for resolved_item_data in self.resolved:
            resolved_item = resolved_item_data.to_dict()
            resolved.append(resolved_item)



        series = []
        for series_item_data in self.series:
            series_item = series_item_data.to_dict()
            series.append(series_item)



        counts = self.counts.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "date": date,
            "resolved": resolved,
            "series": series,
            "counts": counts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_daily_response_200_counts import GetDailyResponse200Counts # noqa: PLC0415
        from ..models.get_daily_response_200_resolved_item import GetDailyResponse200ResolvedItem # noqa: PLC0415
        from ..models.get_daily_response_200_series_item import GetDailyResponse200SeriesItem # noqa: PLC0415
        d = dict(src_dict)
        date = d.pop("date")

        resolved = []
        _resolved = d.pop("resolved")
        for resolved_item_data in (_resolved):
            resolved_item = GetDailyResponse200ResolvedItem.from_dict(resolved_item_data)



            resolved.append(resolved_item)


        series = []
        _series = d.pop("series")
        for series_item_data in (_series):
            series_item = GetDailyResponse200SeriesItem.from_dict(series_item_data)



            series.append(series_item)


        counts = GetDailyResponse200Counts.from_dict(d.pop("counts"))




        get_daily_response_200 = cls(
            date=date,
            resolved=resolved,
            series=series,
            counts=counts,
        )

        return get_daily_response_200

