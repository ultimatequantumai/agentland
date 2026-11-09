from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetLedgerSummaryResponse200ByTopicScienceTech")



@_attrs_define
class GetLedgerSummaryResponse200ByTopicScienceTech:
    """ 
        Attributes:
            n_resolved (int):
            mean_brier (float | None):
            mean_log (float | None):
            mean_edge (float | None):
            shrunk_edge (float):
            ece (float):
     """

    n_resolved: int
    mean_brier: float | None
    mean_log: float | None
    mean_edge: float | None
    shrunk_edge: float
    ece: float





    def to_dict(self) -> dict[str, Any]:
        n_resolved = self.n_resolved

        mean_brier: float | None
        mean_brier = self.mean_brier

        mean_log: float | None
        mean_log = self.mean_log

        mean_edge: float | None
        mean_edge = self.mean_edge

        shrunk_edge = self.shrunk_edge

        ece = self.ece


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "n_resolved": n_resolved,
            "mean_brier": mean_brier,
            "mean_log": mean_log,
            "mean_edge": mean_edge,
            "shrunk_edge": shrunk_edge,
            "ece": ece,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        n_resolved = d.pop("n_resolved")

        def _parse_mean_brier(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        mean_brier = _parse_mean_brier(d.pop("mean_brier"))


        def _parse_mean_log(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        mean_log = _parse_mean_log(d.pop("mean_log"))


        def _parse_mean_edge(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        mean_edge = _parse_mean_edge(d.pop("mean_edge"))


        shrunk_edge = d.pop("shrunk_edge")

        ece = d.pop("ece")

        get_ledger_summary_response_200_by_topic_science_tech = cls(
            n_resolved=n_resolved,
            mean_brier=mean_brier,
            mean_log=mean_log,
            mean_edge=mean_edge,
            shrunk_edge=shrunk_edge,
            ece=ece,
        )

        return get_ledger_summary_response_200_by_topic_science_tech

