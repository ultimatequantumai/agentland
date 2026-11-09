from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_agent_records_response_200_data_item_challenge_family import ListAgentRecordsResponse200DataItemChallengeFamily
from ..models.list_agent_records_response_200_data_item_challenge_objective import ListAgentRecordsResponse200DataItemChallengeObjective






T = TypeVar("T", bound="ListAgentRecordsResponse200DataItemChallenge")



@_attrs_define
class ListAgentRecordsResponse200DataItemChallenge:
    """ 
        Attributes:
            slug (str):
            title (str):
            family (ListAgentRecordsResponse200DataItemChallengeFamily):
            objective (ListAgentRecordsResponse200DataItemChallengeObjective):
     """

    slug: str
    title: str
    family: ListAgentRecordsResponse200DataItemChallengeFamily
    objective: ListAgentRecordsResponse200DataItemChallengeObjective





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

        family = ListAgentRecordsResponse200DataItemChallengeFamily(d.pop("family"))




        objective = ListAgentRecordsResponse200DataItemChallengeObjective(d.pop("objective"))




        list_agent_records_response_200_data_item_challenge = cls(
            slug=slug,
            title=title,
            family=family,
            objective=objective,
        )

        return list_agent_records_response_200_data_item_challenge

