from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AppendLineageResponse201StatsBeforeType0")



@_attrs_define
class AppendLineageResponse201StatsBeforeType0:
    """ 
        Attributes:
            n (int):
            ece (float | None):
            mean_edge (float | None):
     """

    n: int
    ece: float | None
    mean_edge: float | None





    def to_dict(self) -> dict[str, Any]:
        n = self.n

        ece: float | None
        ece = self.ece

        mean_edge: float | None
        mean_edge = self.mean_edge


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "n": n,
            "ece": ece,
            "mean_edge": mean_edge,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        n = d.pop("n")

        def _parse_ece(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        ece = _parse_ece(d.pop("ece"))


        def _parse_mean_edge(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        mean_edge = _parse_mean_edge(d.pop("mean_edge"))


        append_lineage_response_201_stats_before_type_0 = cls(
            n=n,
            ece=ece,
            mean_edge=mean_edge,
        )

        return append_lineage_response_201_stats_before_type_0

