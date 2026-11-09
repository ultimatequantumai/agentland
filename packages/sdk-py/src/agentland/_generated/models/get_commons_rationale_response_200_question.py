from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_commons_rationale_response_200_question_horizon import GetCommonsRationaleResponse200QuestionHorizon
from ..models.get_commons_rationale_response_200_question_status import GetCommonsRationaleResponse200QuestionStatus
from ..models.get_commons_rationale_response_200_question_topic import GetCommonsRationaleResponse200QuestionTopic
from uuid import UUID






T = TypeVar("T", bound="GetCommonsRationaleResponse200Question")



@_attrs_define
class GetCommonsRationaleResponse200Question:
    """ 
        Attributes:
            id (UUID):
            slug (str):
            title (str):
            topic (GetCommonsRationaleResponse200QuestionTopic):
            horizon (GetCommonsRationaleResponse200QuestionHorizon):
            status (GetCommonsRationaleResponse200QuestionStatus):
     """

    id: UUID
    slug: str
    title: str
    topic: GetCommonsRationaleResponse200QuestionTopic
    horizon: GetCommonsRationaleResponse200QuestionHorizon
    status: GetCommonsRationaleResponse200QuestionStatus





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

        topic = GetCommonsRationaleResponse200QuestionTopic(d.pop("topic"))




        horizon = GetCommonsRationaleResponse200QuestionHorizon(d.pop("horizon"))




        status = GetCommonsRationaleResponse200QuestionStatus(d.pop("status"))




        get_commons_rationale_response_200_question = cls(
            id=id,
            slug=slug,
            title=title,
            topic=topic,
            horizon=horizon,
            status=status,
        )

        return get_commons_rationale_response_200_question

