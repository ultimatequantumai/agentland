from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_ledger_summary_response_200_by_horizon_day import GetLedgerSummaryResponse200ByHorizonDay
  from ..models.get_ledger_summary_response_200_by_horizon_hour import GetLedgerSummaryResponse200ByHorizonHour
  from ..models.get_ledger_summary_response_200_by_horizon_long import GetLedgerSummaryResponse200ByHorizonLong
  from ..models.get_ledger_summary_response_200_by_horizon_month import GetLedgerSummaryResponse200ByHorizonMonth
  from ..models.get_ledger_summary_response_200_by_horizon_week import GetLedgerSummaryResponse200ByHorizonWeek





T = TypeVar("T", bound="GetLedgerSummaryResponse200ByHorizon")



@_attrs_define
class GetLedgerSummaryResponse200ByHorizon:
    """ 
        Attributes:
            hour (GetLedgerSummaryResponse200ByHorizonHour | Unset):
            day (GetLedgerSummaryResponse200ByHorizonDay | Unset):
            week (GetLedgerSummaryResponse200ByHorizonWeek | Unset):
            month (GetLedgerSummaryResponse200ByHorizonMonth | Unset):
            long (GetLedgerSummaryResponse200ByHorizonLong | Unset):
     """

    hour: GetLedgerSummaryResponse200ByHorizonHour | Unset = UNSET
    day: GetLedgerSummaryResponse200ByHorizonDay | Unset = UNSET
    week: GetLedgerSummaryResponse200ByHorizonWeek | Unset = UNSET
    month: GetLedgerSummaryResponse200ByHorizonMonth | Unset = UNSET
    long: GetLedgerSummaryResponse200ByHorizonLong | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_ledger_summary_response_200_by_horizon_day import GetLedgerSummaryResponse200ByHorizonDay # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_horizon_hour import GetLedgerSummaryResponse200ByHorizonHour # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_horizon_long import GetLedgerSummaryResponse200ByHorizonLong # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_horizon_month import GetLedgerSummaryResponse200ByHorizonMonth # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_horizon_week import GetLedgerSummaryResponse200ByHorizonWeek # noqa: PLC0415
        hour: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hour, Unset):
            hour = self.hour.to_dict()

        day: dict[str, Any] | Unset = UNSET
        if not isinstance(self.day, Unset):
            day = self.day.to_dict()

        week: dict[str, Any] | Unset = UNSET
        if not isinstance(self.week, Unset):
            week = self.week.to_dict()

        month: dict[str, Any] | Unset = UNSET
        if not isinstance(self.month, Unset):
            month = self.month.to_dict()

        long: dict[str, Any] | Unset = UNSET
        if not isinstance(self.long, Unset):
            long = self.long.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hour is not UNSET:
            field_dict["hour"] = hour
        if day is not UNSET:
            field_dict["day"] = day
        if week is not UNSET:
            field_dict["week"] = week
        if month is not UNSET:
            field_dict["month"] = month
        if long is not UNSET:
            field_dict["long"] = long

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_ledger_summary_response_200_by_horizon_day import GetLedgerSummaryResponse200ByHorizonDay # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_horizon_hour import GetLedgerSummaryResponse200ByHorizonHour # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_horizon_long import GetLedgerSummaryResponse200ByHorizonLong # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_horizon_month import GetLedgerSummaryResponse200ByHorizonMonth # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_horizon_week import GetLedgerSummaryResponse200ByHorizonWeek # noqa: PLC0415
        d = dict(src_dict)
        _hour = d.pop("hour", UNSET)
        hour: GetLedgerSummaryResponse200ByHorizonHour | Unset
        if isinstance(_hour,  Unset):
            hour = UNSET
        else:
            hour = GetLedgerSummaryResponse200ByHorizonHour.from_dict(_hour)




        _day = d.pop("day", UNSET)
        day: GetLedgerSummaryResponse200ByHorizonDay | Unset
        if isinstance(_day,  Unset):
            day = UNSET
        else:
            day = GetLedgerSummaryResponse200ByHorizonDay.from_dict(_day)




        _week = d.pop("week", UNSET)
        week: GetLedgerSummaryResponse200ByHorizonWeek | Unset
        if isinstance(_week,  Unset):
            week = UNSET
        else:
            week = GetLedgerSummaryResponse200ByHorizonWeek.from_dict(_week)




        _month = d.pop("month", UNSET)
        month: GetLedgerSummaryResponse200ByHorizonMonth | Unset
        if isinstance(_month,  Unset):
            month = UNSET
        else:
            month = GetLedgerSummaryResponse200ByHorizonMonth.from_dict(_month)




        _long = d.pop("long", UNSET)
        long: GetLedgerSummaryResponse200ByHorizonLong | Unset
        if isinstance(_long,  Unset):
            long = UNSET
        else:
            long = GetLedgerSummaryResponse200ByHorizonLong.from_dict(_long)




        get_ledger_summary_response_200_by_horizon = cls(
            hour=hour,
            day=day,
            week=week,
            month=month,
            long=long,
        )


        get_ledger_summary_response_200_by_horizon.additional_properties = d
        return get_ledger_summary_response_200_by_horizon

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
