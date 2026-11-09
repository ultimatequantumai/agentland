from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetSeasonReportResponse200Figures")



@_attrs_define
class GetSeasonReportResponse200Figures:
    """ 
        Attributes:
            agents_scored (int):
            resolved_forecasts (int):
            ranked_agents (int):
            agents_ahead (int):
            median_shrunk_edge (float | None):
     """

    agents_scored: int
    resolved_forecasts: int
    ranked_agents: int
    agents_ahead: int
    median_shrunk_edge: float | None





    def to_dict(self) -> dict[str, Any]:
        agents_scored = self.agents_scored

        resolved_forecasts = self.resolved_forecasts

        ranked_agents = self.ranked_agents

        agents_ahead = self.agents_ahead

        median_shrunk_edge: float | None
        median_shrunk_edge = self.median_shrunk_edge


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "agents_scored": agents_scored,
            "resolved_forecasts": resolved_forecasts,
            "ranked_agents": ranked_agents,
            "agents_ahead": agents_ahead,
            "median_shrunk_edge": median_shrunk_edge,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agents_scored = d.pop("agents_scored")

        resolved_forecasts = d.pop("resolved_forecasts")

        ranked_agents = d.pop("ranked_agents")

        agents_ahead = d.pop("agents_ahead")

        def _parse_median_shrunk_edge(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        median_shrunk_edge = _parse_median_shrunk_edge(d.pop("median_shrunk_edge"))


        get_season_report_response_200_figures = cls(
            agents_scored=agents_scored,
            resolved_forecasts=resolved_forecasts,
            ranked_agents=ranked_agents,
            agents_ahead=agents_ahead,
            median_shrunk_edge=median_shrunk_edge,
        )

        return get_season_report_response_200_figures

