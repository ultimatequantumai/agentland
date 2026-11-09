from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_latest_digest_response_200_issue_type_0_records_item_challenge_family import GetLatestDigestResponse200IssueType0RecordsItemChallengeFamily
from ..models.get_latest_digest_response_200_issue_type_0_records_item_challenge_objective import GetLatestDigestResponse200IssueType0RecordsItemChallengeObjective






T = TypeVar("T", bound="GetLatestDigestResponse200IssueType0RecordsItemChallenge")



@_attrs_define
class GetLatestDigestResponse200IssueType0RecordsItemChallenge:
    """ 
        Attributes:
            slug (str):
            title (str):
            family (GetLatestDigestResponse200IssueType0RecordsItemChallengeFamily):
            objective (GetLatestDigestResponse200IssueType0RecordsItemChallengeObjective):
     """

    slug: str
    title: str
    family: GetLatestDigestResponse200IssueType0RecordsItemChallengeFamily
    objective: GetLatestDigestResponse200IssueType0RecordsItemChallengeObjective





    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        title = self.title

        family = self.family.value

        objective = self.objective.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "slug": slug,
            "title": title,
            "family": family,
            "objective": objective,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        title = d.pop("title")

        family = GetLatestDigestResponse200IssueType0RecordsItemChallengeFamily(d.pop("family"))




        objective = GetLatestDigestResponse200IssueType0RecordsItemChallengeObjective(d.pop("objective"))




        get_latest_digest_response_200_issue_type_0_records_item_challenge = cls(
            slug=slug,
            title=title,
            family=family,
            objective=objective,
        )

        return get_latest_digest_response_200_issue_type_0_records_item_challenge

