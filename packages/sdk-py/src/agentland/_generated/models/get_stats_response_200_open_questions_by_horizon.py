from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetStatsResponse200OpenQuestionsByHorizon")



@_attrs_define
class GetStatsResponse200OpenQuestionsByHorizon:
    """ 
        Attributes:
            hour (int):
            day (int):
            week (int):
            month (int):
            long (int):
     """

    hour: int
    day: int
    week: int
    month: int
    long: int





    def to_dict(self) -> dict[str, Any]:
        hour = self.hour

        day = self.day

        week = self.week

        month = self.month

        long = self.long


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "hour": hour,
            "day": day,
            "week": week,
            "month": month,
            "long": long,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hour = d.pop("hour")

        day = d.pop("day")

        week = d.pop("week")

        month = d.pop("month")

        long = d.pop("long")

        get_stats_response_200_open_questions_by_horizon = cls(
            hour=hour,
            day=day,
            week=week,
            month=month,
            long=long,
        )

        return get_stats_response_200_open_questions_by_horizon

