from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="ListTransparencyResolutionsResponse200DataItemQuestion")



@_attrs_define
class ListTransparencyResolutionsResponse200DataItemQuestion:
    """ 
        Attributes:
            id (UUID):
            slug (str):
            title (str):
            source (str):
     """

    id: UUID
    slug: str
    title: str
    source: str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        slug = self.slug

        title = self.title

        source = self.source


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "slug": slug,
            "title": title,
            "source": source,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        slug = d.pop("slug")

        title = d.pop("title")

        source = d.pop("source")

        list_transparency_resolutions_response_200_data_item_question = cls(
            id=id,
            slug=slug,
            title=title,
            source=source,
        )

        return list_transparency_resolutions_response_200_data_item_question

