from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_season_notes_response_200_edges_item_question_horizon import GetSeasonNotesResponse200EdgesItemQuestionHorizon
from ..models.get_season_notes_response_200_edges_item_question_topic import GetSeasonNotesResponse200EdgesItemQuestionTopic
from uuid import UUID






T = TypeVar("T", bound="GetSeasonNotesResponse200EdgesItemQuestion")



@_attrs_define
class GetSeasonNotesResponse200EdgesItemQuestion:
    """ 
        Attributes:
            id (UUID):
            slug (str):
            title (str):
            topic (GetSeasonNotesResponse200EdgesItemQuestionTopic):
            horizon (GetSeasonNotesResponse200EdgesItemQuestionHorizon):
     """

    id: UUID
    slug: str
    title: str
    topic: GetSeasonNotesResponse200EdgesItemQuestionTopic
    horizon: GetSeasonNotesResponse200EdgesItemQuestionHorizon





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        slug = self.slug

        title = self.title

        topic = self.topic.value

        horizon = self.horizon.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "slug": slug,
            "title": title,
            "topic": topic,
            "horizon": horizon,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        slug = d.pop("slug")

        title = d.pop("title")

        topic = GetSeasonNotesResponse200EdgesItemQuestionTopic(d.pop("topic"))




        horizon = GetSeasonNotesResponse200EdgesItemQuestionHorizon(d.pop("horizon"))




        get_season_notes_response_200_edges_item_question = cls(
            id=id,
            slug=slug,
            title=title,
            topic=topic,
            horizon=horizon,
        )

        return get_season_notes_response_200_edges_item_question

