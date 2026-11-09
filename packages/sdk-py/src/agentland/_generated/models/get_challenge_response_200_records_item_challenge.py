from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_challenge_response_200_records_item_challenge_family import GetChallengeResponse200RecordsItemChallengeFamily
from ..models.get_challenge_response_200_records_item_challenge_objective import GetChallengeResponse200RecordsItemChallengeObjective






T = TypeVar("T", bound="GetChallengeResponse200RecordsItemChallenge")



@_attrs_define
class GetChallengeResponse200RecordsItemChallenge:
    """ 
        Attributes:
            slug (str):
            title (str):
            family (GetChallengeResponse200RecordsItemChallengeFamily):
            objective (GetChallengeResponse200RecordsItemChallengeObjective):
     """

    slug: str
    title: str
    family: GetChallengeResponse200RecordsItemChallengeFamily
    objective: GetChallengeResponse200RecordsItemChallengeObjective





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

        family = GetChallengeResponse200RecordsItemChallengeFamily(d.pop("family"))




        objective = GetChallengeResponse200RecordsItemChallengeObjective(d.pop("objective"))




        get_challenge_response_200_records_item_challenge = cls(
            slug=slug,
            title=title,
            family=family,
            objective=objective,
        )

        return get_challenge_response_200_records_item_challenge

