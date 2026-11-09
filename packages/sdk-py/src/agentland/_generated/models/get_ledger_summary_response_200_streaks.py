from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_ledger_summary_response_200_streaks_edge_streak import GetLedgerSummaryResponse200StreaksEdgeStreak





T = TypeVar("T", bound="GetLedgerSummaryResponse200Streaks")



@_attrs_define
class GetLedgerSummaryResponse200Streaks:
    """ 
        Attributes:
            edge_streak (GetLedgerSummaryResponse200StreaksEdgeStreak):
     """

    edge_streak: GetLedgerSummaryResponse200StreaksEdgeStreak





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_ledger_summary_response_200_streaks_edge_streak import GetLedgerSummaryResponse200StreaksEdgeStreak # noqa: PLC0415
        edge_streak = self.edge_streak.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "edge_streak": edge_streak,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_ledger_summary_response_200_streaks_edge_streak import GetLedgerSummaryResponse200StreaksEdgeStreak # noqa: PLC0415
        d = dict(src_dict)
        edge_streak = GetLedgerSummaryResponse200StreaksEdgeStreak.from_dict(d.pop("edge_streak"))




        get_ledger_summary_response_200_streaks = cls(
            edge_streak=edge_streak,
        )

        return get_ledger_summary_response_200_streaks

