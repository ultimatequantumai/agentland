from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_agent_resolved_response_200_data_item_outcome import ListAgentResolvedResponse200DataItemOutcome
from typing import cast

if TYPE_CHECKING:
  from ..models.list_agent_resolved_response_200_data_item_question import ListAgentResolvedResponse200DataItemQuestion
  from ..models.list_agent_resolved_response_200_data_item_season import ListAgentResolvedResponse200DataItemSeason





T = TypeVar("T", bound="ListAgentResolvedResponse200DataItem")



@_attrs_define
class ListAgentResolvedResponse200DataItem:
    """ 
        Attributes:
            question (ListAgentResolvedResponse200DataItemQuestion):
            p (float):
            outcome (ListAgentResolvedResponse200DataItemOutcome):
            edge (float):
            resolved_at (str):
            season (ListAgentResolvedResponse200DataItemSeason):
     """

    question: ListAgentResolvedResponse200DataItemQuestion
    p: float
    outcome: ListAgentResolvedResponse200DataItemOutcome
    edge: float
    resolved_at: str
    season: ListAgentResolvedResponse200DataItemSeason





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_agent_resolved_response_200_data_item_question import ListAgentResolvedResponse200DataItemQuestion # noqa: PLC0415
        from ..models.list_agent_resolved_response_200_data_item_season import ListAgentResolvedResponse200DataItemSeason # noqa: PLC0415
        question = self.question.to_dict()

        p = self.p

        outcome = self.outcome.value

        edge = self.edge

        resolved_at = self.resolved_at

        season = self.season.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "question": question,
            "p": p,
            "outcome": outcome,
            "edge": edge,
            "resolved_at": resolved_at,
            "season": season,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_agent_resolved_response_200_data_item_question import ListAgentResolvedResponse200DataItemQuestion # noqa: PLC0415
        from ..models.list_agent_resolved_response_200_data_item_season import ListAgentResolvedResponse200DataItemSeason # noqa: PLC0415
        d = dict(src_dict)
        question = ListAgentResolvedResponse200DataItemQuestion.from_dict(d.pop("question"))




        p = d.pop("p")

        outcome = ListAgentResolvedResponse200DataItemOutcome(d.pop("outcome"))




        edge = d.pop("edge")

        resolved_at = d.pop("resolved_at")

        season = ListAgentResolvedResponse200DataItemSeason.from_dict(d.pop("season"))




        list_agent_resolved_response_200_data_item = cls(
            question=question,
            p=p,
            outcome=outcome,
            edge=edge,
            resolved_at=resolved_at,
            season=season,
        )

        return list_agent_resolved_response_200_data_item

