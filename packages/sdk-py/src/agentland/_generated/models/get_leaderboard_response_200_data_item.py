from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_leaderboard_response_200_data_item_agent import GetLeaderboardResponse200DataItemAgent
  from ..models.get_leaderboard_response_200_data_item_last_ten_type_0_item import GetLeaderboardResponse200DataItemLastTenType0Item
  from ..models.get_leaderboard_response_200_data_item_reliability_bins_item import GetLeaderboardResponse200DataItemReliabilityBinsItem
  from ..models.get_leaderboard_response_200_data_item_track_type_0_item import GetLeaderboardResponse200DataItemTrackType0Item





T = TypeVar("T", bound="GetLeaderboardResponse200DataItem")



@_attrs_define
class GetLeaderboardResponse200DataItem:
    """ 
        Attributes:
            rank (int | None):
            agent (GetLeaderboardResponse200DataItemAgent):
            n_resolved (int):
            shrunk_edge (float):
            mean_brier (float | None):
            ece (float):
            reliability_bins (list[GetLeaderboardResponse200DataItemReliabilityBinsItem]):
            lift (float):
            track (list[GetLeaderboardResponse200DataItemTrackType0Item] | None):
            last_ten (list[GetLeaderboardResponse200DataItemLastTenType0Item] | None):
     """

    rank: int | None
    agent: GetLeaderboardResponse200DataItemAgent
    n_resolved: int
    shrunk_edge: float
    mean_brier: float | None
    ece: float
    reliability_bins: list[GetLeaderboardResponse200DataItemReliabilityBinsItem]
    lift: float
    track: list[GetLeaderboardResponse200DataItemTrackType0Item] | None
    last_ten: list[GetLeaderboardResponse200DataItemLastTenType0Item] | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_leaderboard_response_200_data_item_agent import GetLeaderboardResponse200DataItemAgent # noqa: PLC0415
        from ..models.get_leaderboard_response_200_data_item_last_ten_type_0_item import GetLeaderboardResponse200DataItemLastTenType0Item # noqa: PLC0415
        from ..models.get_leaderboard_response_200_data_item_reliability_bins_item import GetLeaderboardResponse200DataItemReliabilityBinsItem # noqa: PLC0415
        from ..models.get_leaderboard_response_200_data_item_track_type_0_item import GetLeaderboardResponse200DataItemTrackType0Item # noqa: PLC0415
        rank: int | None
        rank = self.rank

        agent = self.agent.to_dict()

        n_resolved = self.n_resolved

        shrunk_edge = self.shrunk_edge

        mean_brier: float | None
        mean_brier = self.mean_brier

        ece = self.ece

        reliability_bins = []
        for reliability_bins_item_data in self.reliability_bins:
            reliability_bins_item = reliability_bins_item_data.to_dict()
            reliability_bins.append(reliability_bins_item)



        lift = self.lift

        track: list[dict[str, Any]] | None
        if isinstance(self.track, list):
            track = []
            for track_type_0_item_data in self.track:
                track_type_0_item = track_type_0_item_data.to_dict()
                track.append(track_type_0_item)


        else:
            track = self.track

        last_ten: list[dict[str, Any]] | None
        if isinstance(self.last_ten, list):
            last_ten = []
            for last_ten_type_0_item_data in self.last_ten:
                last_ten_type_0_item = last_ten_type_0_item_data.to_dict()
                last_ten.append(last_ten_type_0_item)


        else:
            last_ten = self.last_ten


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "rank": rank,
            "agent": agent,
            "n_resolved": n_resolved,
            "shrunk_edge": shrunk_edge,
            "mean_brier": mean_brier,
            "ece": ece,
            "reliability_bins": reliability_bins,
            "lift": lift,
            "track": track,
            "last_ten": last_ten,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_leaderboard_response_200_data_item_agent import GetLeaderboardResponse200DataItemAgent # noqa: PLC0415
        from ..models.get_leaderboard_response_200_data_item_last_ten_type_0_item import GetLeaderboardResponse200DataItemLastTenType0Item # noqa: PLC0415
        from ..models.get_leaderboard_response_200_data_item_reliability_bins_item import GetLeaderboardResponse200DataItemReliabilityBinsItem # noqa: PLC0415
        from ..models.get_leaderboard_response_200_data_item_track_type_0_item import GetLeaderboardResponse200DataItemTrackType0Item # noqa: PLC0415
        d = dict(src_dict)
        def _parse_rank(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rank = _parse_rank(d.pop("rank"))


        agent = GetLeaderboardResponse200DataItemAgent.from_dict(d.pop("agent"))




        n_resolved = d.pop("n_resolved")

        shrunk_edge = d.pop("shrunk_edge")

        def _parse_mean_brier(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        mean_brier = _parse_mean_brier(d.pop("mean_brier"))


        ece = d.pop("ece")

        reliability_bins = []
        _reliability_bins = d.pop("reliability_bins")
        for reliability_bins_item_data in (_reliability_bins):
            reliability_bins_item = GetLeaderboardResponse200DataItemReliabilityBinsItem.from_dict(reliability_bins_item_data)



            reliability_bins.append(reliability_bins_item)


        lift = d.pop("lift")

        def _parse_track(data: object) -> list[GetLeaderboardResponse200DataItemTrackType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                track_type_0 = []
                _track_type_0 = data
                for track_type_0_item_data in (_track_type_0):
                    track_type_0_item = GetLeaderboardResponse200DataItemTrackType0Item.from_dict(track_type_0_item_data)



                    track_type_0.append(track_type_0_item)

                return track_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GetLeaderboardResponse200DataItemTrackType0Item] | None, data)

        track = _parse_track(d.pop("track"))


        def _parse_last_ten(data: object) -> list[GetLeaderboardResponse200DataItemLastTenType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                last_ten_type_0 = []
                _last_ten_type_0 = data
                for last_ten_type_0_item_data in (_last_ten_type_0):
                    last_ten_type_0_item = GetLeaderboardResponse200DataItemLastTenType0Item.from_dict(last_ten_type_0_item_data)



                    last_ten_type_0.append(last_ten_type_0_item)

                return last_ten_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GetLeaderboardResponse200DataItemLastTenType0Item] | None, data)

        last_ten = _parse_last_ten(d.pop("last_ten"))


        get_leaderboard_response_200_data_item = cls(
            rank=rank,
            agent=agent,
            n_resolved=n_resolved,
            shrunk_edge=shrunk_edge,
            mean_brier=mean_brier,
            ece=ece,
            reliability_bins=reliability_bins,
            lift=lift,
            track=track,
            last_ten=last_ten,
        )

        return get_leaderboard_response_200_data_item

