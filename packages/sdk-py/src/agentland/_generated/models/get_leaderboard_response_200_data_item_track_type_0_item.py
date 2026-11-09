from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetLeaderboardResponse200DataItemTrackType0Item")



@_attrs_define
class GetLeaderboardResponse200DataItemTrackType0Item:
    """ 
        Attributes:
            t (str):
            score (float):
     """

    t: str
    score: float





    def to_dict(self) -> dict[str, Any]:
        t = self.t

        score = self.score


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "t": t,
            "score": score,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        t = d.pop("t")

        score = d.pop("score")

        get_leaderboard_response_200_data_item_track_type_0_item = cls(
            t=t,
            score=score,
        )

        return get_leaderboard_response_200_data_item_track_type_0_item

