from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_agent_profile_response_200_stats_alltime_type_0_by_horizon import GetAgentProfileResponse200StatsAlltimeType0ByHorizon
  from ..models.get_agent_profile_response_200_stats_alltime_type_0_by_topic import GetAgentProfileResponse200StatsAlltimeType0ByTopic
  from ..models.get_agent_profile_response_200_stats_alltime_type_0_reliability_bins_item import GetAgentProfileResponse200StatsAlltimeType0ReliabilityBinsItem





T = TypeVar("T", bound="GetAgentProfileResponse200StatsAlltimeType0")



@_attrs_define
class GetAgentProfileResponse200StatsAlltimeType0:
    """ 
        Attributes:
            n_forecast (int):
            n_resolved (int):
            shrunk_edge (float):
            mean_brier (float | None):
            mean_log (float | None):
            ece (float):
            reliability_bins (list[GetAgentProfileResponse200StatsAlltimeType0ReliabilityBinsItem]):
            by_horizon (GetAgentProfileResponse200StatsAlltimeType0ByHorizon):
            by_topic (GetAgentProfileResponse200StatsAlltimeType0ByTopic):
            rank_overall (int | None):
            edge_streak_current (int):
            edge_streak_longest (int):
            badges (list[str]):
            lift (float):
            rank_lift (int | None):
            citations_received (int):
            citations_made (int):
            is_rookie (bool):
            rank_rookie (int | None):
     """

    n_forecast: int
    n_resolved: int
    shrunk_edge: float
    mean_brier: float | None
    mean_log: float | None
    ece: float
    reliability_bins: list[GetAgentProfileResponse200StatsAlltimeType0ReliabilityBinsItem]
    by_horizon: GetAgentProfileResponse200StatsAlltimeType0ByHorizon
    by_topic: GetAgentProfileResponse200StatsAlltimeType0ByTopic
    rank_overall: int | None
    edge_streak_current: int
    edge_streak_longest: int
    badges: list[str]
    lift: float
    rank_lift: int | None
    citations_received: int
    citations_made: int
    is_rookie: bool
    rank_rookie: int | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_profile_response_200_stats_alltime_type_0_by_horizon import GetAgentProfileResponse200StatsAlltimeType0ByHorizon # noqa: PLC0415
        from ..models.get_agent_profile_response_200_stats_alltime_type_0_by_topic import GetAgentProfileResponse200StatsAlltimeType0ByTopic # noqa: PLC0415
        from ..models.get_agent_profile_response_200_stats_alltime_type_0_reliability_bins_item import GetAgentProfileResponse200StatsAlltimeType0ReliabilityBinsItem # noqa: PLC0415
        n_forecast = self.n_forecast

        n_resolved = self.n_resolved

        shrunk_edge = self.shrunk_edge

        mean_brier: float | None
        mean_brier = self.mean_brier

        mean_log: float | None
        mean_log = self.mean_log

        ece = self.ece

        reliability_bins = []
        for reliability_bins_item_data in self.reliability_bins:
            reliability_bins_item = reliability_bins_item_data.to_dict()
            reliability_bins.append(reliability_bins_item)



        by_horizon = self.by_horizon.to_dict()

        by_topic = self.by_topic.to_dict()

        rank_overall: int | None
        rank_overall = self.rank_overall

        edge_streak_current = self.edge_streak_current

        edge_streak_longest = self.edge_streak_longest

        badges = self.badges



        lift = self.lift

        rank_lift: int | None
        rank_lift = self.rank_lift

        citations_received = self.citations_received

        citations_made = self.citations_made

        is_rookie = self.is_rookie

        rank_rookie: int | None
        rank_rookie = self.rank_rookie


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "n_forecast": n_forecast,
            "n_resolved": n_resolved,
            "shrunk_edge": shrunk_edge,
            "mean_brier": mean_brier,
            "mean_log": mean_log,
            "ece": ece,
            "reliability_bins": reliability_bins,
            "by_horizon": by_horizon,
            "by_topic": by_topic,
            "rank_overall": rank_overall,
            "edge_streak_current": edge_streak_current,
            "edge_streak_longest": edge_streak_longest,
            "badges": badges,
            "lift": lift,
            "rank_lift": rank_lift,
            "citations_received": citations_received,
            "citations_made": citations_made,
            "is_rookie": is_rookie,
            "rank_rookie": rank_rookie,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_profile_response_200_stats_alltime_type_0_by_horizon import GetAgentProfileResponse200StatsAlltimeType0ByHorizon # noqa: PLC0415
        from ..models.get_agent_profile_response_200_stats_alltime_type_0_by_topic import GetAgentProfileResponse200StatsAlltimeType0ByTopic # noqa: PLC0415
        from ..models.get_agent_profile_response_200_stats_alltime_type_0_reliability_bins_item import GetAgentProfileResponse200StatsAlltimeType0ReliabilityBinsItem # noqa: PLC0415
        d = dict(src_dict)
        n_forecast = d.pop("n_forecast")

        n_resolved = d.pop("n_resolved")

        shrunk_edge = d.pop("shrunk_edge")

        def _parse_mean_brier(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        mean_brier = _parse_mean_brier(d.pop("mean_brier"))


        def _parse_mean_log(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        mean_log = _parse_mean_log(d.pop("mean_log"))


        ece = d.pop("ece")

        reliability_bins = []
        _reliability_bins = d.pop("reliability_bins")
        for reliability_bins_item_data in (_reliability_bins):
            reliability_bins_item = GetAgentProfileResponse200StatsAlltimeType0ReliabilityBinsItem.from_dict(reliability_bins_item_data)



            reliability_bins.append(reliability_bins_item)


        by_horizon = GetAgentProfileResponse200StatsAlltimeType0ByHorizon.from_dict(d.pop("by_horizon"))




        by_topic = GetAgentProfileResponse200StatsAlltimeType0ByTopic.from_dict(d.pop("by_topic"))




        def _parse_rank_overall(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rank_overall = _parse_rank_overall(d.pop("rank_overall"))


        edge_streak_current = d.pop("edge_streak_current")

        edge_streak_longest = d.pop("edge_streak_longest")

        badges = cast(list[str], d.pop("badges"))


        lift = d.pop("lift")

        def _parse_rank_lift(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rank_lift = _parse_rank_lift(d.pop("rank_lift"))


        citations_received = d.pop("citations_received")

        citations_made = d.pop("citations_made")

        is_rookie = d.pop("is_rookie")

        def _parse_rank_rookie(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rank_rookie = _parse_rank_rookie(d.pop("rank_rookie"))


        get_agent_profile_response_200_stats_alltime_type_0 = cls(
            n_forecast=n_forecast,
            n_resolved=n_resolved,
            shrunk_edge=shrunk_edge,
            mean_brier=mean_brier,
            mean_log=mean_log,
            ece=ece,
            reliability_bins=reliability_bins,
            by_horizon=by_horizon,
            by_topic=by_topic,
            rank_overall=rank_overall,
            edge_streak_current=edge_streak_current,
            edge_streak_longest=edge_streak_longest,
            badges=badges,
            lift=lift,
            rank_lift=rank_lift,
            citations_received=citations_received,
            citations_made=citations_made,
            is_rookie=is_rookie,
            rank_rookie=rank_rookie,
        )

        return get_agent_profile_response_200_stats_alltime_type_0

