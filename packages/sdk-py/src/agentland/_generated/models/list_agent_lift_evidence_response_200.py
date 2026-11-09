from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.list_agent_lift_evidence_response_200_data_item import ListAgentLiftEvidenceResponse200DataItem
  from ..models.list_agent_lift_evidence_response_200_season import ListAgentLiftEvidenceResponse200Season
  from ..models.list_agent_lift_evidence_response_200_seasons_item import ListAgentLiftEvidenceResponse200SeasonsItem
  from ..models.list_agent_lift_evidence_response_200_summary_type_0 import ListAgentLiftEvidenceResponse200SummaryType0





T = TypeVar("T", bound="ListAgentLiftEvidenceResponse200")



@_attrs_define
class ListAgentLiftEvidenceResponse200:
    """ 
        Attributes:
            season (ListAgentLiftEvidenceResponse200Season):
            summary (ListAgentLiftEvidenceResponse200SummaryType0 | None):
            seasons (list[ListAgentLiftEvidenceResponse200SeasonsItem]):
            data (list[ListAgentLiftEvidenceResponse200DataItem]):
            next_cursor (None | str):
     """

    season: ListAgentLiftEvidenceResponse200Season
    summary: ListAgentLiftEvidenceResponse200SummaryType0 | None
    seasons: list[ListAgentLiftEvidenceResponse200SeasonsItem]
    data: list[ListAgentLiftEvidenceResponse200DataItem]
    next_cursor: None | str





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_agent_lift_evidence_response_200_data_item import ListAgentLiftEvidenceResponse200DataItem # noqa: PLC0415
        from ..models.list_agent_lift_evidence_response_200_season import ListAgentLiftEvidenceResponse200Season # noqa: PLC0415
        from ..models.list_agent_lift_evidence_response_200_seasons_item import ListAgentLiftEvidenceResponse200SeasonsItem # noqa: PLC0415
        from ..models.list_agent_lift_evidence_response_200_summary_type_0 import ListAgentLiftEvidenceResponse200SummaryType0 # noqa: PLC0415
        season = self.season.to_dict()

        summary: dict[str, Any] | None
        if isinstance(self.summary, ListAgentLiftEvidenceResponse200SummaryType0):
            summary = self.summary.to_dict()
        else:
            summary = self.summary

        seasons = []
        for seasons_item_data in self.seasons:
            seasons_item = seasons_item_data.to_dict()
            seasons.append(seasons_item)



        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        next_cursor: None | str
        next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "season": season,
            "summary": summary,
            "seasons": seasons,
            "data": data,
            "next_cursor": next_cursor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_agent_lift_evidence_response_200_data_item import ListAgentLiftEvidenceResponse200DataItem # noqa: PLC0415
        from ..models.list_agent_lift_evidence_response_200_season import ListAgentLiftEvidenceResponse200Season # noqa: PLC0415
        from ..models.list_agent_lift_evidence_response_200_seasons_item import ListAgentLiftEvidenceResponse200SeasonsItem # noqa: PLC0415
        from ..models.list_agent_lift_evidence_response_200_summary_type_0 import ListAgentLiftEvidenceResponse200SummaryType0 # noqa: PLC0415
        d = dict(src_dict)
        season = ListAgentLiftEvidenceResponse200Season.from_dict(d.pop("season"))




        def _parse_summary(data: object) -> ListAgentLiftEvidenceResponse200SummaryType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                summary_type_0 = ListAgentLiftEvidenceResponse200SummaryType0.from_dict(data)



                return summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListAgentLiftEvidenceResponse200SummaryType0 | None, data)

        summary = _parse_summary(d.pop("summary"))


        seasons = []
        _seasons = d.pop("seasons")
        for seasons_item_data in (_seasons):
            seasons_item = ListAgentLiftEvidenceResponse200SeasonsItem.from_dict(seasons_item_data)



            seasons.append(seasons_item)


        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = ListAgentLiftEvidenceResponse200DataItem.from_dict(data_item_data)



            data.append(data_item)


        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))


        list_agent_lift_evidence_response_200 = cls(
            season=season,
            summary=summary,
            seasons=seasons,
            data=data,
            next_cursor=next_cursor,
        )

        return list_agent_lift_evidence_response_200

