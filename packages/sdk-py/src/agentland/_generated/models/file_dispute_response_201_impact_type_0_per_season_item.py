from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.file_dispute_response_201_impact_type_0_per_season_item_season import FileDisputeResponse201ImpactType0PerSeasonItemSeason





T = TypeVar("T", bound="FileDisputeResponse201ImpactType0PerSeasonItem")



@_attrs_define
class FileDisputeResponse201ImpactType0PerSeasonItem:
    """ 
        Attributes:
            season (FileDisputeResponse201ImpactType0PerSeasonItemSeason):
            original_scores (int):
            appended_scores (int):
     """

    season: FileDisputeResponse201ImpactType0PerSeasonItemSeason
    original_scores: int
    appended_scores: int





    def to_dict(self) -> dict[str, Any]:
        from ..models.file_dispute_response_201_impact_type_0_per_season_item_season import FileDisputeResponse201ImpactType0PerSeasonItemSeason # noqa: PLC0415
        season = self.season.to_dict()

        original_scores = self.original_scores

        appended_scores = self.appended_scores


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "season": season,
            "original_scores": original_scores,
            "appended_scores": appended_scores,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_dispute_response_201_impact_type_0_per_season_item_season import FileDisputeResponse201ImpactType0PerSeasonItemSeason # noqa: PLC0415
        d = dict(src_dict)
        season = FileDisputeResponse201ImpactType0PerSeasonItemSeason.from_dict(d.pop("season"))




        original_scores = d.pop("original_scores")

        appended_scores = d.pop("appended_scores")

        file_dispute_response_201_impact_type_0_per_season_item = cls(
            season=season,
            original_scores=original_scores,
            appended_scores=appended_scores,
        )

        return file_dispute_response_201_impact_type_0_per_season_item

