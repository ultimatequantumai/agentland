from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SubmitRecordArtifactResponse202Challenge")



@_attrs_define
class SubmitRecordArtifactResponse202Challenge:
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

        submit_record_artifact_response_202_challenge = cls(
            slug=slug,
            title=title,
            family=family,
        )

        return submit_record_artifact_response_202_challenge

