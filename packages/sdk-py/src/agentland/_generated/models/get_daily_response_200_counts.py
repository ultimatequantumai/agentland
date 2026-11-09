from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetDailyResponse200Counts")



@_attrs_define
class GetDailyResponse200Counts:
    """ 
        Attributes:
            resolved (int):
            voided (int):
            scored_forecasts (int):
     """

    resolved: int
    voided: int
    scored_forecasts: int





    def to_dict(self) -> dict[str, Any]:
        resolved = self.resolved

        voided = self.voided

        scored_forecasts = self.scored_forecasts


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "resolved": resolved,
            "voided": voided,
            "scored_forecasts": scored_forecasts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resolved = d.pop("resolved")

        voided = d.pop("voided")

        scored_forecasts = d.pop("scored_forecasts")

        get_daily_response_200_counts = cls(
            resolved=resolved,
            voided=voided,
            scored_forecasts=scored_forecasts,
        )

        return get_daily_response_200_counts

