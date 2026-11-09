from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_my_forecasts_response_200_data_item_multi_score_type_0_baseline_kind import ListMyForecastsResponse200DataItemMultiScoreType0BaselineKind
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ListMyForecastsResponse200DataItemMultiScoreType0")



@_attrs_define
class ListMyForecastsResponse200DataItemMultiScoreType0:
    """ 
        Attributes:
            id (UUID):
            season_id (UUID):
            resolution_id (UUID):
            outcome_key (str):
            p_realized (float):
            brier (float):
            log_score (float):
            edge (float):
            baseline_kind (ListMyForecastsResponse200DataItemMultiScoreType0BaselineKind):
            baseline_p_realized (float):
            baseline_snapshot_id (None | str):
            brier_baseline (float):
            scoring_version (str):
            scored_at (str):
     """

    id: UUID
    season_id: UUID
    resolution_id: UUID
    outcome_key: str
    p_realized: float
    brier: float
    log_score: float
    edge: float
    baseline_kind: ListMyForecastsResponse200DataItemMultiScoreType0BaselineKind
    baseline_p_realized: float
    baseline_snapshot_id: None | str
    brier_baseline: float
    scoring_version: str
    scored_at: str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        season_id = str(self.season_id)

        resolution_id = str(self.resolution_id)

        outcome_key = self.outcome_key

        p_realized = self.p_realized

        brier = self.brier

        log_score = self.log_score

        edge = self.edge

        baseline_kind = self.baseline_kind.value

        baseline_p_realized = self.baseline_p_realized

        baseline_snapshot_id: None | str
        baseline_snapshot_id = self.baseline_snapshot_id

        brier_baseline = self.brier_baseline

        scoring_version = self.scoring_version

        scored_at = self.scored_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "season_id": season_id,
            "resolution_id": resolution_id,
            "outcome_key": outcome_key,
            "p_realized": p_realized,
            "brier": brier,
            "log_score": log_score,
            "edge": edge,
            "baseline_kind": baseline_kind,
            "baseline_p_realized": baseline_p_realized,
            "baseline_snapshot_id": baseline_snapshot_id,
            "brier_baseline": brier_baseline,
            "scoring_version": scoring_version,
            "scored_at": scored_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        season_id = UUID(d.pop("season_id"))




        resolution_id = UUID(d.pop("resolution_id"))




        outcome_key = d.pop("outcome_key")

        p_realized = d.pop("p_realized")

        brier = d.pop("brier")

        log_score = d.pop("log_score")

        edge = d.pop("edge")

        baseline_kind = ListMyForecastsResponse200DataItemMultiScoreType0BaselineKind(d.pop("baseline_kind"))




        baseline_p_realized = d.pop("baseline_p_realized")

        def _parse_baseline_snapshot_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        baseline_snapshot_id = _parse_baseline_snapshot_id(d.pop("baseline_snapshot_id"))


        brier_baseline = d.pop("brier_baseline")

        scoring_version = d.pop("scoring_version")

        scored_at = d.pop("scored_at")

        list_my_forecasts_response_200_data_item_multi_score_type_0 = cls(
            id=id,
            season_id=season_id,
            resolution_id=resolution_id,
            outcome_key=outcome_key,
            p_realized=p_realized,
            brier=brier,
            log_score=log_score,
            edge=edge,
            baseline_kind=baseline_kind,
            baseline_p_realized=baseline_p_realized,
            baseline_snapshot_id=baseline_snapshot_id,
            brier_baseline=brier_baseline,
            scoring_version=scoring_version,
            scored_at=scored_at,
        )

        return list_my_forecasts_response_200_data_item_multi_score_type_0

