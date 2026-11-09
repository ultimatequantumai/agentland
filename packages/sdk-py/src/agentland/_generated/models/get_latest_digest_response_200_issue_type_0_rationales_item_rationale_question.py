from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_latest_digest_response_200_issue_type_0_rationales_item_rationale_question_horizon import GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestionHorizon
from ..models.get_latest_digest_response_200_issue_type_0_rationales_item_rationale_question_status import GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestionStatus
from ..models.get_latest_digest_response_200_issue_type_0_rationales_item_rationale_question_topic import GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestionTopic
from uuid import UUID






T = TypeVar("T", bound="GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestion")



@_attrs_define
class GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestion:
    """ 
        Attributes:
            id (UUID):
            slug (str):
            title (str):
            topic (GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestionTopic):
            horizon (GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestionHorizon):
            status (GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestionStatus):
     """

    id: UUID
    slug: str
    title: str
    topic: GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestionTopic
    horizon: GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestionHorizon
    status: GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestionStatus





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

        topic = GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestionTopic(d.pop("topic"))




        horizon = GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestionHorizon(d.pop("horizon"))




        status = GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestionStatus(d.pop("status"))




        get_latest_digest_response_200_issue_type_0_rationales_item_rationale_question = cls(
            id=id,
            slug=slug,
            title=title,
            topic=topic,
            horizon=horizon,
            status=status,
        )

        return get_latest_digest_response_200_issue_type_0_rationales_item_rationale_question

