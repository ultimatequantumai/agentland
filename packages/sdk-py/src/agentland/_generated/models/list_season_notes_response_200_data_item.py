from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ListSeasonNotesResponse200DataItem")



@_attrs_define
class ListSeasonNotesResponse200DataItem:
    """ 
        Attributes:
            week (str):
            starts_on (str):
            ends_on (str):
            published_at (str):
            rationale_count (int):
            edge_count (int):
     """

    week: str
    starts_on: str
    ends_on: str
    published_at: str
    rationale_count: int
    edge_count: int





    def to_dict(self) -> dict[str, Any]:
        week = self.week

        starts_on = self.starts_on

        ends_on = self.ends_on

        published_at = self.published_at

        rationale_count = self.rationale_count

        edge_count = self.edge_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "week": week,
            "starts_on": starts_on,
            "ends_on": ends_on,
            "published_at": published_at,
            "rationale_count": rationale_count,
            "edge_count": edge_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        week = d.pop("week")

        starts_on = d.pop("starts_on")

        ends_on = d.pop("ends_on")

        published_at = d.pop("published_at")

        rationale_count = d.pop("rationale_count")

        edge_count = d.pop("edge_count")

        list_season_notes_response_200_data_item = cls(
            week=week,
            starts_on=starts_on,
            ends_on=ends_on,
            published_at=published_at,
            rationale_count=rationale_count,
            edge_count=edge_count,
        )

        return list_season_notes_response_200_data_item

