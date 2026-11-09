from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_latest_digest_response_200_issue_type_0_edges_item_question_horizon import GetLatestDigestResponse200IssueType0EdgesItemQuestionHorizon
from ..models.get_latest_digest_response_200_issue_type_0_edges_item_question_topic import GetLatestDigestResponse200IssueType0EdgesItemQuestionTopic
from uuid import UUID






T = TypeVar("T", bound="GetLatestDigestResponse200IssueType0EdgesItemQuestion")



@_attrs_define
class GetLatestDigestResponse200IssueType0EdgesItemQuestion:
    """ 
        Attributes:
            id (UUID):
            slug (str):
            title (str):
            topic (GetLatestDigestResponse200IssueType0EdgesItemQuestionTopic):
            horizon (GetLatestDigestResponse200IssueType0EdgesItemQuestionHorizon):
     """

    id: UUID
    slug: str
    title: str
    topic: GetLatestDigestResponse200IssueType0EdgesItemQuestionTopic
    horizon: GetLatestDigestResponse200IssueType0EdgesItemQuestionHorizon





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

        topic = GetLatestDigestResponse200IssueType0EdgesItemQuestionTopic(d.pop("topic"))




        horizon = GetLatestDigestResponse200IssueType0EdgesItemQuestionHorizon(d.pop("horizon"))




        get_latest_digest_response_200_issue_type_0_edges_item_question = cls(
            id=id,
            slug=slug,
            title=title,
            topic=topic,
            horizon=horizon,
        )

        return get_latest_digest_response_200_issue_type_0_edges_item_question

