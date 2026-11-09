from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetMeResponse200Standing")



@_attrs_define
class GetMeResponse200Standing:
    """ 
        Attributes:
            n_resolved (int):
            shrunk_edge (float):
            rank_overall (int | None):
            rank_lift (int | None):
            trust (float | None):
     """

    n_resolved: int
    shrunk_edge: float
    rank_overall: int | None
    rank_lift: int | None
    trust: float | None





    def to_dict(self) -> dict[str, Any]:
        n_resolved = self.n_resolved

        shrunk_edge = self.shrunk_edge

        rank_overall: int | None
        rank_overall = self.rank_overall

        rank_lift: int | None
        rank_lift = self.rank_lift

        trust: float | None
        trust = self.trust


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "n_resolved": n_resolved,
            "shrunk_edge": shrunk_edge,
            "rank_overall": rank_overall,
            "rank_lift": rank_lift,
            "trust": trust,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        n_resolved = d.pop("n_resolved")

        shrunk_edge = d.pop("shrunk_edge")

        def _parse_rank_overall(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rank_overall = _parse_rank_overall(d.pop("rank_overall"))


        def _parse_rank_lift(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rank_lift = _parse_rank_lift(d.pop("rank_lift"))


        def _parse_trust(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        trust = _parse_trust(d.pop("trust"))


        get_me_response_200_standing = cls(
            n_resolved=n_resolved,
            shrunk_edge=shrunk_edge,
            rank_overall=rank_overall,
            rank_lift=rank_lift,
            trust=trust,
        )

        return get_me_response_200_standing

