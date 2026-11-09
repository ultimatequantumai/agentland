from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_season_notes_response_200_edges_item_agent import GetSeasonNotesResponse200EdgesItemAgent
  from ..models.get_season_notes_response_200_edges_item_question import GetSeasonNotesResponse200EdgesItemQuestion





T = TypeVar("T", bound="GetSeasonNotesResponse200EdgesItem")



@_attrs_define
class GetSeasonNotesResponse200EdgesItem:
    """ 
        Attributes:
            scope_label (str):
            agent (GetSeasonNotesResponse200EdgesItemAgent):
            question (GetSeasonNotesResponse200EdgesItemQuestion):
            forecast_id (UUID):
            edge (float):
     """

    scope_label: str
    agent: GetSeasonNotesResponse200EdgesItemAgent
    question: GetSeasonNotesResponse200EdgesItemQuestion
    forecast_id: UUID
    edge: float





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_season_notes_response_200_edges_item_agent import GetSeasonNotesResponse200EdgesItemAgent # noqa: PLC0415
        from ..models.get_season_notes_response_200_edges_item_question import GetSeasonNotesResponse200EdgesItemQuestion # noqa: PLC0415
        scope_label = self.scope_label

        agent = self.agent.to_dict()

        question = self.question.to_dict()

        forecast_id = str(self.forecast_id)

        edge = self.edge


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "scope_label": scope_label,
            "agent": agent,
            "question": question,
            "forecast_id": forecast_id,
            "edge": edge,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_season_notes_response_200_edges_item_agent import GetSeasonNotesResponse200EdgesItemAgent # noqa: PLC0415
        from ..models.get_season_notes_response_200_edges_item_question import GetSeasonNotesResponse200EdgesItemQuestion # noqa: PLC0415
        d = dict(src_dict)
        scope_label = d.pop("scope_label")

        agent = GetSeasonNotesResponse200EdgesItemAgent.from_dict(d.pop("agent"))




        question = GetSeasonNotesResponse200EdgesItemQuestion.from_dict(d.pop("question"))




        forecast_id = UUID(d.pop("forecast_id"))




        edge = d.pop("edge")

        get_season_notes_response_200_edges_item = cls(
            scope_label=scope_label,
            agent=agent,
            question=question,
            forecast_id=forecast_id,
            edge=edge,
        )

        return get_season_notes_response_200_edges_item

