from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_season_notes_response_200_rationales_item_rationale_question_horizon import GetSeasonNotesResponse200RationalesItemRationaleQuestionHorizon
from ..models.get_season_notes_response_200_rationales_item_rationale_question_status import GetSeasonNotesResponse200RationalesItemRationaleQuestionStatus
from ..models.get_season_notes_response_200_rationales_item_rationale_question_topic import GetSeasonNotesResponse200RationalesItemRationaleQuestionTopic
from uuid import UUID






T = TypeVar("T", bound="GetSeasonNotesResponse200RationalesItemRationaleQuestion")



@_attrs_define
class GetSeasonNotesResponse200RationalesItemRationaleQuestion:
    """ 
        Attributes:
            id (UUID):
            slug (str):
            title (str):
            topic (GetSeasonNotesResponse200RationalesItemRationaleQuestionTopic):
            horizon (GetSeasonNotesResponse200RationalesItemRationaleQuestionHorizon):
            status (GetSeasonNotesResponse200RationalesItemRationaleQuestionStatus):
     """

    id: UUID
    slug: str
    title: str
    topic: GetSeasonNotesResponse200RationalesItemRationaleQuestionTopic
    horizon: GetSeasonNotesResponse200RationalesItemRationaleQuestionHorizon
    status: GetSeasonNotesResponse200RationalesItemRationaleQuestionStatus





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        slug = self.slug

        title = self.title

        topic = self.topic.value

        horizon = self.horizon.value

        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "slug": slug,
            "title": title,
            "topic": topic,
            "horizon": horizon,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        slug = d.pop("slug")

        title = d.pop("title")

        topic = GetSeasonNotesResponse200RationalesItemRationaleQuestionTopic(d.pop("topic"))




        horizon = GetSeasonNotesResponse200RationalesItemRationaleQuestionHorizon(d.pop("horizon"))




        status = GetSeasonNotesResponse200RationalesItemRationaleQuestionStatus(d.pop("status"))




        get_season_notes_response_200_rationales_item_rationale_question = cls(
            id=id,
            slug=slug,
            title=title,
            topic=topic,
            horizon=horizon,
            status=status,
        )

        return get_season_notes_response_200_rationales_item_rationale_question

