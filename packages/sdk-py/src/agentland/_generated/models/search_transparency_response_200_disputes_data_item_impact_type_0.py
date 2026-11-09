from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_transparency_response_200_disputes_data_item_impact_type_0_state import SearchTransparencyResponse200DisputesDataItemImpactType0State
from typing import cast

if TYPE_CHECKING:
  from ..models.search_transparency_response_200_disputes_data_item_impact_type_0_per_season_item import SearchTransparencyResponse200DisputesDataItemImpactType0PerSeasonItem





T = TypeVar("T", bound="SearchTransparencyResponse200DisputesDataItemImpactType0")



@_attrs_define
class SearchTransparencyResponse200DisputesDataItemImpactType0:
    """ 
        Attributes:
            state (SearchTransparencyResponse200DisputesDataItemImpactType0State):
            per_season (list[SearchTransparencyResponse200DisputesDataItemImpactType0PerSeasonItem]):
     """

    state: SearchTransparencyResponse200DisputesDataItemImpactType0State
    per_season: list[SearchTransparencyResponse200DisputesDataItemImpactType0PerSeasonItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_transparency_response_200_disputes_data_item_impact_type_0_per_season_item import SearchTransparencyResponse200DisputesDataItemImpactType0PerSeasonItem # noqa: PLC0415
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
        from ..models.search_transparency_response_200_disputes_data_item_impact_type_0_per_season_item import SearchTransparencyResponse200DisputesDataItemImpactType0PerSeasonItem # noqa: PLC0415
        d = dict(src_dict)
        state = SearchTransparencyResponse200DisputesDataItemImpactType0State(d.pop("state"))




        per_season = []
        _per_season = d.pop("per_season")
        for per_season_item_data in (_per_season):
            per_season_item = SearchTransparencyResponse200DisputesDataItemImpactType0PerSeasonItem.from_dict(per_season_item_data)



            per_season.append(per_season_item)


        search_transparency_response_200_disputes_data_item_impact_type_0 = cls(
            state=state,
            per_season=per_season,
        )

        return search_transparency_response_200_disputes_data_item_impact_type_0

