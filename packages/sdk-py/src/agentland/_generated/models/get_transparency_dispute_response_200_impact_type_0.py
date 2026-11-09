from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_transparency_dispute_response_200_impact_type_0_state import GetTransparencyDisputeResponse200ImpactType0State
from typing import cast

if TYPE_CHECKING:
  from ..models.get_transparency_dispute_response_200_impact_type_0_per_season_item import GetTransparencyDisputeResponse200ImpactType0PerSeasonItem





T = TypeVar("T", bound="GetTransparencyDisputeResponse200ImpactType0")



@_attrs_define
class GetTransparencyDisputeResponse200ImpactType0:
    """ 
        Attributes:
            state (GetTransparencyDisputeResponse200ImpactType0State):
            per_season (list[GetTransparencyDisputeResponse200ImpactType0PerSeasonItem]):
     """

    state: GetTransparencyDisputeResponse200ImpactType0State
    per_season: list[GetTransparencyDisputeResponse200ImpactType0PerSeasonItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_transparency_dispute_response_200_impact_type_0_per_season_item import GetTransparencyDisputeResponse200ImpactType0PerSeasonItem # noqa: PLC0415
        state = self.state.value

        per_season = []
        for per_season_item_data in self.per_season:
            per_season_item = per_season_item_data.to_dict()
            per_season.append(per_season_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "state": state,
            "per_season": per_season,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_transparency_dispute_response_200_impact_type_0_per_season_item import GetTransparencyDisputeResponse200ImpactType0PerSeasonItem # noqa: PLC0415
        d = dict(src_dict)
        state = GetTransparencyDisputeResponse200ImpactType0State(d.pop("state"))




        per_season = []
        _per_season = d.pop("per_season")
        for per_season_item_data in (_per_season):
            per_season_item = GetTransparencyDisputeResponse200ImpactType0PerSeasonItem.from_dict(per_season_item_data)



            per_season.append(per_season_item)


        get_transparency_dispute_response_200_impact_type_0 = cls(
            state=state,
            per_season=per_season,
        )

        return get_transparency_dispute_response_200_impact_type_0

