from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_season_report_response_200_by_horizon_item_horizon import GetSeasonReportResponse200ByHorizonItemHorizon
from typing import cast






T = TypeVar("T", bound="GetSeasonReportResponse200ByHorizonItem")



@_attrs_define
class GetSeasonReportResponse200ByHorizonItem:
    """ 
        Attributes:
            horizon (GetSeasonReportResponse200ByHorizonItemHorizon):
            forecasts (int):
            mean_edge (float | None):
            ranked_agents (int):
            agents_ahead (int):
     """

    horizon: GetSeasonReportResponse200ByHorizonItemHorizon
    forecasts: int
    mean_edge: float | None
    ranked_agents: int
    agents_ahead: int





    def to_dict(self) -> dict[str, Any]:
        horizon = self.horizon.value

        forecasts = self.forecasts

        mean_edge: float | None
        mean_edge = self.mean_edge

        ranked_agents = self.ranked_agents

        agents_ahead = self.agents_ahead


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "horizon": horizon,
            "forecasts": forecasts,
            "mean_edge": mean_edge,
            "ranked_agents": ranked_agents,
            "agents_ahead": agents_ahead,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        horizon = GetSeasonReportResponse200ByHorizonItemHorizon(d.pop("horizon"))




        forecasts = d.pop("forecasts")

        def _parse_mean_edge(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        mean_edge = _parse_mean_edge(d.pop("mean_edge"))


        ranked_agents = d.pop("ranked_agents")

        agents_ahead = d.pop("agents_ahead")

        get_season_report_response_200_by_horizon_item = cls(
            horizon=horizon,
            forecasts=forecasts,
            mean_edge=mean_edge,
            ranked_agents=ranked_agents,
            agents_ahead=agents_ahead,
        )

        return get_season_report_response_200_by_horizon_item

