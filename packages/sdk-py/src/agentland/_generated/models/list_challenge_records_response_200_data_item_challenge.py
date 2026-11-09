from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_challenge_records_response_200_data_item_challenge_family import ListChallengeRecordsResponse200DataItemChallengeFamily
from ..models.list_challenge_records_response_200_data_item_challenge_objective import ListChallengeRecordsResponse200DataItemChallengeObjective






T = TypeVar("T", bound="ListChallengeRecordsResponse200DataItemChallenge")



@_attrs_define
class ListChallengeRecordsResponse200DataItemChallenge:
    """ 
        Attributes:
            slug (str):
            title (str):
            family (ListChallengeRecordsResponse200DataItemChallengeFamily):
            objective (ListChallengeRecordsResponse200DataItemChallengeObjective):
     """

    slug: str
    title: str
    family: ListChallengeRecordsResponse200DataItemChallengeFamily
    objective: ListChallengeRecordsResponse200DataItemChallengeObjective





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

        family = ListChallengeRecordsResponse200DataItemChallengeFamily(d.pop("family"))




        objective = ListChallengeRecordsResponse200DataItemChallengeObjective(d.pop("objective"))




        list_challenge_records_response_200_data_item_challenge = cls(
            slug=slug,
            title=title,
            family=family,
            objective=objective,
        )

        return list_challenge_records_response_200_data_item_challenge

