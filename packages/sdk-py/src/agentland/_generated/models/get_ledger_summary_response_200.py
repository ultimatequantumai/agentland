from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_ledger_summary_response_200_by_horizon import GetLedgerSummaryResponse200ByHorizon
  from ..models.get_ledger_summary_response_200_by_topic import GetLedgerSummaryResponse200ByTopic
  from ..models.get_ledger_summary_response_200_recent_lessons_item import GetLedgerSummaryResponse200RecentLessonsItem
  from ..models.get_ledger_summary_response_200_reliability_bins_item import GetLedgerSummaryResponse200ReliabilityBinsItem
  from ..models.get_ledger_summary_response_200_streaks import GetLedgerSummaryResponse200Streaks





T = TypeVar("T", bound="GetLedgerSummaryResponse200")



@_attrs_define
class GetLedgerSummaryResponse200:
    """ 
        Attributes:
            season_id (None | UUID):
            scoring_version (str):
            n_resolved (int):
            mean_brier (float | None):
            mean_log (float | None):
            mean_edge (float | None):
            shrunk_edge (float):
            ece (float):
            reliability_bins (list[GetLedgerSummaryResponse200ReliabilityBinsItem]):
            by_horizon (GetLedgerSummaryResponse200ByHorizon):
            by_topic (GetLedgerSummaryResponse200ByTopic):
            streaks (GetLedgerSummaryResponse200Streaks):
            recent_lessons (list[GetLedgerSummaryResponse200RecentLessonsItem]):
     """

    season_id: None | UUID
    scoring_version: str
    n_resolved: int
    mean_brier: float | None
    mean_log: float | None
    mean_edge: float | None
    shrunk_edge: float
    ece: float
    reliability_bins: list[GetLedgerSummaryResponse200ReliabilityBinsItem]
    by_horizon: GetLedgerSummaryResponse200ByHorizon
    by_topic: GetLedgerSummaryResponse200ByTopic
    streaks: GetLedgerSummaryResponse200Streaks
    recent_lessons: list[GetLedgerSummaryResponse200RecentLessonsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_ledger_summary_response_200_by_horizon import GetLedgerSummaryResponse200ByHorizon # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic import GetLedgerSummaryResponse200ByTopic # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_recent_lessons_item import GetLedgerSummaryResponse200RecentLessonsItem # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_reliability_bins_item import GetLedgerSummaryResponse200ReliabilityBinsItem # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_streaks import GetLedgerSummaryResponse200Streaks # noqa: PLC0415
        season_id: None | str
        if isinstance(self.season_id, UUID):
            season_id = str(self.season_id)
        else:
            season_id = self.season_id

        scoring_version = self.scoring_version

        n_resolved = self.n_resolved

        mean_brier: float | None
        mean_brier = self.mean_brier

        mean_log: float | None
        mean_log = self.mean_log

        mean_edge: float | None
        mean_edge = self.mean_edge

        shrunk_edge = self.shrunk_edge

        ece = self.ece

        reliability_bins = []
        for reliability_bins_item_data in self.reliability_bins:
            reliability_bins_item = reliability_bins_item_data.to_dict()
            reliability_bins.append(reliability_bins_item)



        by_horizon = self.by_horizon.to_dict()

        by_topic = self.by_topic.to_dict()

        streaks = self.streaks.to_dict()

        recent_lessons = []
        for recent_lessons_item_data in self.recent_lessons:
            recent_lessons_item = recent_lessons_item_data.to_dict()
            recent_lessons.append(recent_lessons_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "season_id": season_id,
            "scoring_version": scoring_version,
            "n_resolved": n_resolved,
            "mean_brier": mean_brier,
            "mean_log": mean_log,
            "mean_edge": mean_edge,
            "shrunk_edge": shrunk_edge,
            "ece": ece,
            "reliability_bins": reliability_bins,
            "by_horizon": by_horizon,
            "by_topic": by_topic,
            "streaks": streaks,
            "recent_lessons": recent_lessons,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_ledger_summary_response_200_by_horizon import GetLedgerSummaryResponse200ByHorizon # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_by_topic import GetLedgerSummaryResponse200ByTopic # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_recent_lessons_item import GetLedgerSummaryResponse200RecentLessonsItem # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_reliability_bins_item import GetLedgerSummaryResponse200ReliabilityBinsItem # noqa: PLC0415
        from ..models.get_ledger_summary_response_200_streaks import GetLedgerSummaryResponse200Streaks # noqa: PLC0415
        d = dict(src_dict)
        def _parse_season_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                season_id_type_0 = UUID(data)



                return season_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        season_id = _parse_season_id(d.pop("season_id"))


        scoring_version = d.pop("scoring_version")

        n_resolved = d.pop("n_resolved")

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


        def _parse_mean_edge(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        mean_edge = _parse_mean_edge(d.pop("mean_edge"))


        shrunk_edge = d.pop("shrunk_edge")

        ece = d.pop("ece")

        reliability_bins = []
        _reliability_bins = d.pop("reliability_bins")
        for reliability_bins_item_data in (_reliability_bins):
            reliability_bins_item = GetLedgerSummaryResponse200ReliabilityBinsItem.from_dict(reliability_bins_item_data)



            reliability_bins.append(reliability_bins_item)


        by_horizon = GetLedgerSummaryResponse200ByHorizon.from_dict(d.pop("by_horizon"))




        by_topic = GetLedgerSummaryResponse200ByTopic.from_dict(d.pop("by_topic"))




        streaks = GetLedgerSummaryResponse200Streaks.from_dict(d.pop("streaks"))




        recent_lessons = []
        _recent_lessons = d.pop("recent_lessons")
        for recent_lessons_item_data in (_recent_lessons):
            recent_lessons_item = GetLedgerSummaryResponse200RecentLessonsItem.from_dict(recent_lessons_item_data)



            recent_lessons.append(recent_lessons_item)


        get_ledger_summary_response_200 = cls(
            season_id=season_id,
            scoring_version=scoring_version,
            n_resolved=n_resolved,
            mean_brier=mean_brier,
            mean_log=mean_log,
            mean_edge=mean_edge,
            shrunk_edge=shrunk_edge,
            ece=ece,
            reliability_bins=reliability_bins,
            by_horizon=by_horizon,
            by_topic=by_topic,
            streaks=streaks,
            recent_lessons=recent_lessons,
        )

        return get_ledger_summary_response_200

