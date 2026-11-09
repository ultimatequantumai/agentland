from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_season_notes_response_200_edges_item import GetSeasonNotesResponse200EdgesItem
  from ..models.get_season_notes_response_200_rationales_item import GetSeasonNotesResponse200RationalesItem
  from ..models.get_season_notes_response_200_records_item import GetSeasonNotesResponse200RecordsItem





T = TypeVar("T", bound="GetSeasonNotesResponse200")



@_attrs_define
class GetSeasonNotesResponse200:
    """ 
        Attributes:
            week (str):
            starts_on (str):
            ends_on (str):
            published_at (str):
            prev (None | str):
            next_ (None | str):
            rationales (list[GetSeasonNotesResponse200RationalesItem]):
            edges (list[GetSeasonNotesResponse200EdgesItem]):
            records (list[GetSeasonNotesResponse200RecordsItem]):
     """

    week: str
    starts_on: str
    ends_on: str
    published_at: str
    prev: None | str
    next_: None | str
    rationales: list[GetSeasonNotesResponse200RationalesItem]
    edges: list[GetSeasonNotesResponse200EdgesItem]
    records: list[GetSeasonNotesResponse200RecordsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_season_notes_response_200_edges_item import GetSeasonNotesResponse200EdgesItem # noqa: PLC0415
        from ..models.get_season_notes_response_200_rationales_item import GetSeasonNotesResponse200RationalesItem # noqa: PLC0415
        from ..models.get_season_notes_response_200_records_item import GetSeasonNotesResponse200RecordsItem # noqa: PLC0415
        week = self.week

        starts_on = self.starts_on

        ends_on = self.ends_on

        published_at = self.published_at

        prev: None | str
        prev = self.prev

        next_: None | str
        next_ = self.next_

        rationales = []
        for rationales_item_data in self.rationales:
            rationales_item = rationales_item_data.to_dict()
            rationales.append(rationales_item)



        edges = []
        for edges_item_data in self.edges:
            edges_item = edges_item_data.to_dict()
            edges.append(edges_item)



        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "week": week,
            "starts_on": starts_on,
            "ends_on": ends_on,
            "published_at": published_at,
            "prev": prev,
            "next": next_,
            "rationales": rationales,
            "edges": edges,
            "records": records,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_season_notes_response_200_edges_item import GetSeasonNotesResponse200EdgesItem # noqa: PLC0415
        from ..models.get_season_notes_response_200_rationales_item import GetSeasonNotesResponse200RationalesItem # noqa: PLC0415
        from ..models.get_season_notes_response_200_records_item import GetSeasonNotesResponse200RecordsItem # noqa: PLC0415
        d = dict(src_dict)
        week = d.pop("week")

        starts_on = d.pop("starts_on")

        ends_on = d.pop("ends_on")

        published_at = d.pop("published_at")

        def _parse_prev(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        prev = _parse_prev(d.pop("prev"))


        def _parse_next_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_ = _parse_next_(d.pop("next"))


        rationales = []
        _rationales = d.pop("rationales")
        for rationales_item_data in (_rationales):
            rationales_item = GetSeasonNotesResponse200RationalesItem.from_dict(rationales_item_data)



            rationales.append(rationales_item)


        edges = []
        _edges = d.pop("edges")
        for edges_item_data in (_edges):
            edges_item = GetSeasonNotesResponse200EdgesItem.from_dict(edges_item_data)



            edges.append(edges_item)


        records = []
        _records = d.pop("records")
        for records_item_data in (_records):
            records_item = GetSeasonNotesResponse200RecordsItem.from_dict(records_item_data)



            records.append(records_item)


        get_season_notes_response_200 = cls(
            week=week,
            starts_on=starts_on,
            ends_on=ends_on,
            published_at=published_at,
            prev=prev,
            next_=next_,
            rationales=rationales,
            edges=edges,
            records=records,
        )

        return get_season_notes_response_200

