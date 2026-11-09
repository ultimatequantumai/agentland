from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_question_disputes_response_200_data_item_impact_type_0_state import ListQuestionDisputesResponse200DataItemImpactType0State
from typing import cast

if TYPE_CHECKING:
  from ..models.list_question_disputes_response_200_data_item_impact_type_0_per_season_item import ListQuestionDisputesResponse200DataItemImpactType0PerSeasonItem





T = TypeVar("T", bound="ListQuestionDisputesResponse200DataItemImpactType0")



@_attrs_define
class ListQuestionDisputesResponse200DataItemImpactType0:
    """ 
        Attributes:
            state (ListQuestionDisputesResponse200DataItemImpactType0State):
            per_season (list[ListQuestionDisputesResponse200DataItemImpactType0PerSeasonItem]):
     """

    state: ListQuestionDisputesResponse200DataItemImpactType0State
    per_season: list[ListQuestionDisputesResponse200DataItemImpactType0PerSeasonItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_question_disputes_response_200_data_item_impact_type_0_per_season_item import ListQuestionDisputesResponse200DataItemImpactType0PerSeasonItem # noqa: PLC0415
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
        from ..models.list_question_disputes_response_200_data_item_impact_type_0_per_season_item import ListQuestionDisputesResponse200DataItemImpactType0PerSeasonItem # noqa: PLC0415
        d = dict(src_dict)
        state = ListQuestionDisputesResponse200DataItemImpactType0State(d.pop("state"))




        per_season = []
        _per_season = d.pop("per_season")
        for per_season_item_data in (_per_season):
            per_season_item = ListQuestionDisputesResponse200DataItemImpactType0PerSeasonItem.from_dict(per_season_item_data)



            per_season.append(per_season_item)


        list_question_disputes_response_200_data_item_impact_type_0 = cls(
            state=state,
            per_season=per_season,
        )

        return list_question_disputes_response_200_data_item_impact_type_0

