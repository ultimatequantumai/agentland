from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_record_response_200_challenge_family import GetRecordResponse200ChallengeFamily
from ..models.get_record_response_200_challenge_objective import GetRecordResponse200ChallengeObjective






T = TypeVar("T", bound="GetRecordResponse200Challenge")



@_attrs_define
class GetRecordResponse200Challenge:
    """ 
        Attributes:
            slug (str):
            title (str):
            family (GetRecordResponse200ChallengeFamily):
            objective (GetRecordResponse200ChallengeObjective):
     """

    slug: str
    title: str
    family: GetRecordResponse200ChallengeFamily
    objective: GetRecordResponse200ChallengeObjective





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

        family = GetRecordResponse200ChallengeFamily(d.pop("family"))




        objective = GetRecordResponse200ChallengeObjective(d.pop("objective"))




        get_record_response_200_challenge = cls(
            slug=slug,
            title=title,
            family=family,
            objective=objective,
        )

        return get_record_response_200_challenge

