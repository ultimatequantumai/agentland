from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_agent_profile_response_200_recent_resolved_item_question_horizon import GetAgentProfileResponse200RecentResolvedItemQuestionHorizon
from ..models.get_agent_profile_response_200_recent_resolved_item_question_topic import GetAgentProfileResponse200RecentResolvedItemQuestionTopic
from uuid import UUID






T = TypeVar("T", bound="GetAgentProfileResponse200RecentResolvedItemQuestion")



@_attrs_define
class GetAgentProfileResponse200RecentResolvedItemQuestion:
    """ 
        Attributes:
            id (UUID):
            slug (str):
            title (str):
            horizon (GetAgentProfileResponse200RecentResolvedItemQuestionHorizon):
            topic (GetAgentProfileResponse200RecentResolvedItemQuestionTopic):
     """

    id: UUID
    slug: str
    title: str
    horizon: GetAgentProfileResponse200RecentResolvedItemQuestionHorizon
    topic: GetAgentProfileResponse200RecentResolvedItemQuestionTopic





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        slug = self.slug

        title = self.title

        horizon = self.horizon.value

        topic = self.topic.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "slug": slug,
            "title": title,
            "horizon": horizon,
            "topic": topic,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        slug = d.pop("slug")

        title = d.pop("title")

        horizon = GetAgentProfileResponse200RecentResolvedItemQuestionHorizon(d.pop("horizon"))




        topic = GetAgentProfileResponse200RecentResolvedItemQuestionTopic(d.pop("topic"))




        get_agent_profile_response_200_recent_resolved_item_question = cls(
            id=id,
            slug=slug,
            title=title,
            horizon=horizon,
            topic=topic,
        )

        return get_agent_profile_response_200_recent_resolved_item_question

