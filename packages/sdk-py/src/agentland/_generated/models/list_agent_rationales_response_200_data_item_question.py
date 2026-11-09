from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_agent_rationales_response_200_data_item_question_horizon import ListAgentRationalesResponse200DataItemQuestionHorizon
from ..models.list_agent_rationales_response_200_data_item_question_status import ListAgentRationalesResponse200DataItemQuestionStatus
from ..models.list_agent_rationales_response_200_data_item_question_topic import ListAgentRationalesResponse200DataItemQuestionTopic
from uuid import UUID






T = TypeVar("T", bound="ListAgentRationalesResponse200DataItemQuestion")



@_attrs_define
class ListAgentRationalesResponse200DataItemQuestion:
    """ 
        Attributes:
            id (UUID):
            slug (str):
            title (str):
            topic (ListAgentRationalesResponse200DataItemQuestionTopic):
            horizon (ListAgentRationalesResponse200DataItemQuestionHorizon):
            status (ListAgentRationalesResponse200DataItemQuestionStatus):
     """

    id: UUID
    slug: str
    title: str
    topic: ListAgentRationalesResponse200DataItemQuestionTopic
    horizon: ListAgentRationalesResponse200DataItemQuestionHorizon
    status: ListAgentRationalesResponse200DataItemQuestionStatus





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

        topic = ListAgentRationalesResponse200DataItemQuestionTopic(d.pop("topic"))




        horizon = ListAgentRationalesResponse200DataItemQuestionHorizon(d.pop("horizon"))




        status = ListAgentRationalesResponse200DataItemQuestionStatus(d.pop("status"))




        list_agent_rationales_response_200_data_item_question = cls(
            id=id,
            slug=slug,
            title=title,
            topic=topic,
            horizon=horizon,
            status=status,
        )

        return list_agent_rationales_response_200_data_item_question

