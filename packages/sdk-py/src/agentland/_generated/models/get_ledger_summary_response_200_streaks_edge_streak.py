from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetLedgerSummaryResponse200StreaksEdgeStreak")



@_attrs_define
class GetLedgerSummaryResponse200StreaksEdgeStreak:
    """ 
        Attributes:
            current (int):
            longest (int):
     """

    current: int
    longest: int





    def to_dict(self) -> dict[str, Any]:
        current = self.current

        longest = self.longest


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "current": current,
            "longest": longest,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current = d.pop("current")

        longest = d.pop("longest")

        get_ledger_summary_response_200_streaks_edge_streak = cls(
            current=current,
            longest=longest,
        )

        return get_ledger_summary_response_200_streaks_edge_streak

