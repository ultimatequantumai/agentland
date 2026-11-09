from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetMySubmissionResponse200Challenge")



@_attrs_define
class GetMySubmissionResponse200Challenge:
    """ 
        Attributes:
            slug (str):
            title (str):
            family (str):
     """

    slug: str
    title: str
    family: str





    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        title = self.title

        family = self.family


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "slug": slug,
            "title": title,
            "family": family,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        title = d.pop("title")

        family = d.pop("family")

        get_my_submission_response_200_challenge = cls(
            slug=slug,
            title=title,
            family=family,
        )

        return get_my_submission_response_200_challenge

