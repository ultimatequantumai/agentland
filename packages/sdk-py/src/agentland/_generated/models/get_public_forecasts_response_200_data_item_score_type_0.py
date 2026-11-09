from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_public_forecasts_response_200_data_item_score_type_0_baseline_kind import GetPublicForecastsResponse200DataItemScoreType0BaselineKind
from ..models.get_public_forecasts_response_200_data_item_score_type_0_outcome_type_0 import GetPublicForecastsResponse200DataItemScoreType0OutcomeType0
from ..models.get_public_forecasts_response_200_data_item_score_type_0_outcome_type_1 import GetPublicForecastsResponse200DataItemScoreType0OutcomeType1
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GetPublicForecastsResponse200DataItemScoreType0")



@_attrs_define
class GetPublicForecastsResponse200DataItemScoreType0:
    """ 
        Attributes:
            id (UUID):
            season_id (UUID):
            resolution_id (UUID):
            outcome (GetPublicForecastsResponse200DataItemScoreType0OutcomeType0 |
                GetPublicForecastsResponse200DataItemScoreType0OutcomeType1):
            p_clipped (float):
            brier (float):
            log_score (float):
            baseline_kind (GetPublicForecastsResponse200DataItemScoreType0BaselineKind):
            baseline_p (float):
            baseline_snapshot_id (None | str):
            baseline_snapshot_taken_at (None | str):
            brier_baseline (float):
            edge (float):
            scoring_version (str):
            scored_at (str):
            resolution_revision (int):
     """

    id: UUID
    season_id: UUID
    resolution_id: UUID
    outcome: GetPublicForecastsResponse200DataItemScoreType0OutcomeType0 | GetPublicForecastsResponse200DataItemScoreType0OutcomeType1
    p_clipped: float
    brier: float
    log_score: float
    baseline_kind: GetPublicForecastsResponse200DataItemScoreType0BaselineKind
    baseline_p: float
    baseline_snapshot_id: None | str
    baseline_snapshot_taken_at: None | str
    brier_baseline: float
    edge: float
    scoring_version: str
    scored_at: str
    resolution_revision: int





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        season_id = str(self.season_id)

        resolution_id = str(self.resolution_id)

        outcome: int
        if isinstance(self.outcome, GetPublicForecastsResponse200DataItemScoreType0OutcomeType0):
            outcome = self.outcome.value
        else:
            outcome = self.outcome.value


        p_clipped = self.p_clipped

        brier = self.brier

        log_score = self.log_score

        baseline_kind = self.baseline_kind.value

        baseline_p = self.baseline_p

        baseline_snapshot_id: None | str
        baseline_snapshot_id = self.baseline_snapshot_id

        baseline_snapshot_taken_at: None | str
        baseline_snapshot_taken_at = self.baseline_snapshot_taken_at

        brier_baseline = self.brier_baseline

        edge = self.edge

        scoring_version = self.scoring_version

        scored_at = self.scored_at

        resolution_revision = self.resolution_revision


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "season_id": season_id,
            "resolution_id": resolution_id,
            "outcome": outcome,
            "p_clipped": p_clipped,
            "brier": brier,
            "log_score": log_score,
            "baseline_kind": baseline_kind,
            "baseline_p": baseline_p,
            "baseline_snapshot_id": baseline_snapshot_id,
            "baseline_snapshot_taken_at": baseline_snapshot_taken_at,
            "brier_baseline": brier_baseline,
            "edge": edge,
            "scoring_version": scoring_version,
            "scored_at": scored_at,
            "resolution_revision": resolution_revision,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        season_id = UUID(d.pop("season_id"))




        resolution_id = UUID(d.pop("resolution_id"))




        def _parse_outcome(data: object) -> GetPublicForecastsResponse200DataItemScoreType0OutcomeType0 | GetPublicForecastsResponse200DataItemScoreType0OutcomeType1:
            try:
                if not isinstance(data, int):
                    raise TypeError()
                outcome_type_0 = GetPublicForecastsResponse200DataItemScoreType0OutcomeType0(data)



                return outcome_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, int):
                raise TypeError()
            outcome_type_1 = GetPublicForecastsResponse200DataItemScoreType0OutcomeType1(data)



            return outcome_type_1

        outcome = _parse_outcome(d.pop("outcome"))


        p_clipped = d.pop("p_clipped")

        brier = d.pop("brier")

        log_score = d.pop("log_score")

        baseline_kind = GetPublicForecastsResponse200DataItemScoreType0BaselineKind(d.pop("baseline_kind"))




        baseline_p = d.pop("baseline_p")

        def _parse_baseline_snapshot_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        baseline_snapshot_id = _parse_baseline_snapshot_id(d.pop("baseline_snapshot_id"))


        def _parse_baseline_snapshot_taken_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        baseline_snapshot_taken_at = _parse_baseline_snapshot_taken_at(d.pop("baseline_snapshot_taken_at"))


        brier_baseline = d.pop("brier_baseline")

        edge = d.pop("edge")

        scoring_version = d.pop("scoring_version")

        scored_at = d.pop("scored_at")

        resolution_revision = d.pop("resolution_revision")

        get_public_forecasts_response_200_data_item_score_type_0 = cls(
            id=id,
            season_id=season_id,
            resolution_id=resolution_id,
            outcome=outcome,
            p_clipped=p_clipped,
            brier=brier,
            log_score=log_score,
            baseline_kind=baseline_kind,
            baseline_p=baseline_p,
            baseline_snapshot_id=baseline_snapshot_id,
            baseline_snapshot_taken_at=baseline_snapshot_taken_at,
            brier_baseline=brier_baseline,
            edge=edge,
            scoring_version=scoring_version,
            scored_at=scored_at,
            resolution_revision=resolution_revision,
        )

        return get_public_forecasts_response_200_data_item_score_type_0

