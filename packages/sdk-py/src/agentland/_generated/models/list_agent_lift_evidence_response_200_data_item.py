from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_agent_lift_evidence_response_200_data_item_status import ListAgentLiftEvidenceResponse200DataItemStatus
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.list_agent_lift_evidence_response_200_data_item_citing import ListAgentLiftEvidenceResponse200DataItemCiting
  from ..models.list_agent_lift_evidence_response_200_data_item_question import ListAgentLiftEvidenceResponse200DataItemQuestion
  from ..models.list_agent_lift_evidence_response_200_data_item_season import ListAgentLiftEvidenceResponse200DataItemSeason





T = TypeVar("T", bound="ListAgentLiftEvidenceResponse200DataItem")



@_attrs_define
class ListAgentLiftEvidenceResponse200DataItem:
    """ 
        Attributes:
            season (ListAgentLiftEvidenceResponse200DataItemSeason):
            citing (ListAgentLiftEvidenceResponse200DataItemCiting):
            question (ListAgentLiftEvidenceResponse200DataItemQuestion):
            rationale_id (UUID):
            final_edge (float):
            contribution (float):
            status (ListAgentLiftEvidenceResponse200DataItemStatus):
            week (datetime.date):
     """

    season: ListAgentLiftEvidenceResponse200DataItemSeason
    citing: ListAgentLiftEvidenceResponse200DataItemCiting
    question: ListAgentLiftEvidenceResponse200DataItemQuestion
    rationale_id: UUID
    final_edge: float
    contribution: float
    status: ListAgentLiftEvidenceResponse200DataItemStatus
    week: datetime.date





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_agent_lift_evidence_response_200_data_item_citing import ListAgentLiftEvidenceResponse200DataItemCiting # noqa: PLC0415
        from ..models.list_agent_lift_evidence_response_200_data_item_question import ListAgentLiftEvidenceResponse200DataItemQuestion # noqa: PLC0415
        from ..models.list_agent_lift_evidence_response_200_data_item_season import ListAgentLiftEvidenceResponse200DataItemSeason # noqa: PLC0415
        season = self.season.to_dict()

        citing = self.citing.to_dict()

        question = self.question.to_dict()

        rationale_id = str(self.rationale_id)

        final_edge = self.final_edge

        contribution = self.contribution

        status = self.status.value

        week = self.week.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "season": season,
            "citing": citing,
            "question": question,
            "rationale_id": rationale_id,
            "final_edge": final_edge,
            "contribution": contribution,
            "status": status,
            "week": week,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_agent_lift_evidence_response_200_data_item_citing import ListAgentLiftEvidenceResponse200DataItemCiting # noqa: PLC0415
        from ..models.list_agent_lift_evidence_response_200_data_item_question import ListAgentLiftEvidenceResponse200DataItemQuestion # noqa: PLC0415
        from ..models.list_agent_lift_evidence_response_200_data_item_season import ListAgentLiftEvidenceResponse200DataItemSeason # noqa: PLC0415
        d = dict(src_dict)
        season = ListAgentLiftEvidenceResponse200DataItemSeason.from_dict(d.pop("season"))




        citing = ListAgentLiftEvidenceResponse200DataItemCiting.from_dict(d.pop("citing"))




        question = ListAgentLiftEvidenceResponse200DataItemQuestion.from_dict(d.pop("question"))




        rationale_id = UUID(d.pop("rationale_id"))




        final_edge = d.pop("final_edge")

        contribution = d.pop("contribution")

        status = ListAgentLiftEvidenceResponse200DataItemStatus(d.pop("status"))




        week = datetime.date.fromisoformat(d.pop("week"))




        list_agent_lift_evidence_response_200_data_item = cls(
            season=season,
            citing=citing,
            question=question,
            rationale_id=rationale_id,
            final_edge=final_edge,
            contribution=contribution,
            status=status,
            week=week,
        )

        return list_agent_lift_evidence_response_200_data_item

