from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_stats_response_200_current_seasons_item import GetStatsResponse200CurrentSeasonsItem
  from ..models.get_stats_response_200_open_questions_by_horizon import GetStatsResponse200OpenQuestionsByHorizon





T = TypeVar("T", bound="GetStatsResponse200")



@_attrs_define
class GetStatsResponse200:
    """ 
        Attributes:
            as_of (str):
            resolved_forecasts_7d (int):
            resolved_forecasts_total (int):
            agents_total (int):
            agents_active_7d (int):
            open_questions_by_horizon (GetStatsResponse200OpenQuestionsByHorizon):
            resolved_questions_total (int):
            citations_7d (int):
            current_seasons (list[GetStatsResponse200CurrentSeasonsItem]):
     """

    as_of: str
    resolved_forecasts_7d: int
    resolved_forecasts_total: int
    agents_total: int
    agents_active_7d: int
    open_questions_by_horizon: GetStatsResponse200OpenQuestionsByHorizon
    resolved_questions_total: int
    citations_7d: int
    current_seasons: list[GetStatsResponse200CurrentSeasonsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_stats_response_200_current_seasons_item import GetStatsResponse200CurrentSeasonsItem # noqa: PLC0415
        from ..models.get_stats_response_200_open_questions_by_horizon import GetStatsResponse200OpenQuestionsByHorizon # noqa: PLC0415
        as_of = self.as_of

        resolved_forecasts_7d = self.resolved_forecasts_7d

        resolved_forecasts_total = self.resolved_forecasts_total

        agents_total = self.agents_total

        agents_active_7d = self.agents_active_7d

        open_questions_by_horizon = self.open_questions_by_horizon.to_dict()

        resolved_questions_total = self.resolved_questions_total

        citations_7d = self.citations_7d

        current_seasons = []
        for current_seasons_item_data in self.current_seasons:
            current_seasons_item = current_seasons_item_data.to_dict()
            current_seasons.append(current_seasons_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "as_of": as_of,
            "resolved_forecasts_7d": resolved_forecasts_7d,
            "resolved_forecasts_total": resolved_forecasts_total,
            "agents_total": agents_total,
            "agents_active_7d": agents_active_7d,
            "open_questions_by_horizon": open_questions_by_horizon,
            "resolved_questions_total": resolved_questions_total,
            "citations_7d": citations_7d,
            "current_seasons": current_seasons,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_stats_response_200_current_seasons_item import GetStatsResponse200CurrentSeasonsItem # noqa: PLC0415
        from ..models.get_stats_response_200_open_questions_by_horizon import GetStatsResponse200OpenQuestionsByHorizon # noqa: PLC0415
        d = dict(src_dict)
        as_of = d.pop("as_of")

        resolved_forecasts_7d = d.pop("resolved_forecasts_7d")

        resolved_forecasts_total = d.pop("resolved_forecasts_total")

        agents_total = d.pop("agents_total")

        agents_active_7d = d.pop("agents_active_7d")

        open_questions_by_horizon = GetStatsResponse200OpenQuestionsByHorizon.from_dict(d.pop("open_questions_by_horizon"))




        resolved_questions_total = d.pop("resolved_questions_total")

        citations_7d = d.pop("citations_7d")

        current_seasons = []
        _current_seasons = d.pop("current_seasons")
        for current_seasons_item_data in (_current_seasons):
            current_seasons_item = GetStatsResponse200CurrentSeasonsItem.from_dict(current_seasons_item_data)



            current_seasons.append(current_seasons_item)


        get_stats_response_200 = cls(
            as_of=as_of,
            resolved_forecasts_7d=resolved_forecasts_7d,
            resolved_forecasts_total=resolved_forecasts_total,
            agents_total=agents_total,
            agents_active_7d=agents_active_7d,
            open_questions_by_horizon=open_questions_by_horizon,
            resolved_questions_total=resolved_questions_total,
            citations_7d=citations_7d,
            current_seasons=current_seasons,
        )

        return get_stats_response_200

