from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_leaderboard_response_200_data_item_last_ten_type_0_item_outcome_type import GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType
from ..models.get_leaderboard_response_200_data_item_last_ten_type_0_item_outcome_type_0 import GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType0
from ..models.get_leaderboard_response_200_data_item_last_ten_type_0_item_outcome_type_1 import GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType1
from typing import cast

if TYPE_CHECKING:
  from ..models.get_leaderboard_response_200_data_item_last_ten_type_0_item_question import GetLeaderboardResponse200DataItemLastTenType0ItemQuestion





T = TypeVar("T", bound="GetLeaderboardResponse200DataItemLastTenType0Item")



@_attrs_define
class GetLeaderboardResponse200DataItemLastTenType0Item:
    """ 
        Attributes:
            question (GetLeaderboardResponse200DataItemLastTenType0ItemQuestion):
            resolved_at (str):
            outcome (GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType0 |
                GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType1):
            outcome_type (GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType):
            outcome_label (None | str):
            edge (float):
     """

    question: GetLeaderboardResponse200DataItemLastTenType0ItemQuestion
    resolved_at: str
    outcome: GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType0 | GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType1
    outcome_type: GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType
    outcome_label: None | str
    edge: float





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_leaderboard_response_200_data_item_last_ten_type_0_item_question import GetLeaderboardResponse200DataItemLastTenType0ItemQuestion # noqa: PLC0415
        question = self.question.to_dict()

        resolved_at = self.resolved_at

        outcome: int
        if isinstance(self.outcome, GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType0):
            outcome = self.outcome.value
        else:
            outcome = self.outcome.value


        outcome_type = self.outcome_type.value

        outcome_label: None | str
        outcome_label = self.outcome_label

        edge = self.edge


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "question": question,
            "resolved_at": resolved_at,
            "outcome": outcome,
            "outcome_type": outcome_type,
            "outcome_label": outcome_label,
            "edge": edge,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_leaderboard_response_200_data_item_last_ten_type_0_item_question import GetLeaderboardResponse200DataItemLastTenType0ItemQuestion # noqa: PLC0415
        d = dict(src_dict)
        question = GetLeaderboardResponse200DataItemLastTenType0ItemQuestion.from_dict(d.pop("question"))




        resolved_at = d.pop("resolved_at")

        def _parse_outcome(data: object) -> GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType0 | GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType1:
            try:
                if not isinstance(data, int):
                    raise TypeError()
                outcome_type_0 = GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType0(data)



                return outcome_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, int):
                raise TypeError()
            outcome_type_1 = GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType1(data)



            return outcome_type_1

        outcome = _parse_outcome(d.pop("outcome"))


        outcome_type = GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType(d.pop("outcome_type"))




        def _parse_outcome_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        outcome_label = _parse_outcome_label(d.pop("outcome_label"))


        edge = d.pop("edge")

        get_leaderboard_response_200_data_item_last_ten_type_0_item = cls(
            question=question,
            resolved_at=resolved_at,
            outcome=outcome,
            outcome_type=outcome_type,
            outcome_label=outcome_label,
            edge=edge,
        )

        return get_leaderboard_response_200_data_item_last_ten_type_0_item

