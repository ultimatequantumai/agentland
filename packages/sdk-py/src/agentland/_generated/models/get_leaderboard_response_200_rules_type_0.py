from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetLeaderboardResponse200RulesType0")



@_attrs_define
class GetLeaderboardResponse200RulesType0:
    """ 
        Attributes:
            share (float):
            shrink_k (int):
            min_resolved_for_rank (int):
     """

    share: float
    shrink_k: int
    min_resolved_for_rank: int





    def to_dict(self) -> dict[str, Any]:
        share = self.share

        shrink_k = self.shrink_k

        min_resolved_for_rank = self.min_resolved_for_rank


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "share": share,
            "shrink_k": shrink_k,
            "min_resolved_for_rank": min_resolved_for_rank,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        share = d.pop("share")

        shrink_k = d.pop("shrink_k")

        min_resolved_for_rank = d.pop("min_resolved_for_rank")

        get_leaderboard_response_200_rules_type_0 = cls(
            share=share,
            shrink_k=shrink_k,
            min_resolved_for_rank=min_resolved_for_rank,
        )

        return get_leaderboard_response_200_rules_type_0

