from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_agent_resolved_response_200_data_item_question_horizon import ListAgentResolvedResponse200DataItemQuestionHorizon
from ..models.list_agent_resolved_response_200_data_item_question_topic import ListAgentResolvedResponse200DataItemQuestionTopic
from uuid import UUID






T = TypeVar("T", bound="ListAgentResolvedResponse200DataItemQuestion")



@_attrs_define
class ListAgentResolvedResponse200DataItemQuestion:
    """ 
        Attributes:
            id (UUID):
            slug (str):
            title (str):
            horizon (ListAgentResolvedResponse200DataItemQuestionHorizon):
            topic (ListAgentResolvedResponse200DataItemQuestionTopic):
     """

    id: UUID
    slug: str
    title: str
    horizon: ListAgentResolvedResponse200DataItemQuestionHorizon
    topic: ListAgentResolvedResponse200DataItemQuestionTopic





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

        horizon = ListAgentResolvedResponse200DataItemQuestionHorizon(d.pop("horizon"))




        topic = ListAgentResolvedResponse200DataItemQuestionTopic(d.pop("topic"))




        list_agent_resolved_response_200_data_item_question = cls(
            id=id,
            slug=slug,
            title=title,
            horizon=horizon,
            topic=topic,
        )

        return list_agent_resolved_response_200_data_item_question

