from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_public_forecasts_response_200_data_item_numeric_score_type_0_baseline_kind import GetPublicForecastsResponse200DataItemNumericScoreType0BaselineKind
from uuid import UUID






T = TypeVar("T", bound="GetPublicForecastsResponse200DataItemNumericScoreType0")



@_attrs_define
class GetPublicForecastsResponse200DataItemNumericScoreType0:
    """ 
        Attributes:
            id (UUID):
            season_id (UUID):
            resolution_id (UUID):
            crps (float):
            crps_baseline (float):
            crps_edge (float):
            baseline_kind (GetPublicForecastsResponse200DataItemNumericScoreType0BaselineKind):
            scoring_version (str):
            scored_at (str):
     """

    id: UUID
    season_id: UUID
    resolution_id: UUID
    crps: float
    crps_baseline: float
    crps_edge: float
    baseline_kind: GetPublicForecastsResponse200DataItemNumericScoreType0BaselineKind
    scoring_version: str
    scored_at: str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        season_id = str(self.season_id)

        resolution_id = str(self.resolution_id)

        crps = self.crps

        crps_baseline = self.crps_baseline

        crps_edge = self.crps_edge

        baseline_kind = self.baseline_kind.value

        scoring_version = self.scoring_version

        scored_at = self.scored_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "season_id": season_id,
            "resolution_id": resolution_id,
            "crps": crps,
            "crps_baseline": crps_baseline,
            "crps_edge": crps_edge,
            "baseline_kind": baseline_kind,
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




        crps = d.pop("crps")

        crps_baseline = d.pop("crps_baseline")

        crps_edge = d.pop("crps_edge")

        baseline_kind = GetPublicForecastsResponse200DataItemNumericScoreType0BaselineKind(d.pop("baseline_kind"))




        scoring_version = d.pop("scoring_version")

        scored_at = d.pop("scored_at")

        get_public_forecasts_response_200_data_item_numeric_score_type_0 = cls(
            id=id,
            season_id=season_id,
            resolution_id=resolution_id,
            crps=crps,
            crps_baseline=crps_baseline,
            crps_edge=crps_edge,
            baseline_kind=baseline_kind,
            scoring_version=scoring_version,
            scored_at=scored_at,
        )

        return get_public_forecasts_response_200_data_item_numeric_score_type_0

