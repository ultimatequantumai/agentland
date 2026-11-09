from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_transparency_response_200_moderation_data_item_content_type_1_kind import SearchTransparencyResponse200ModerationDataItemContentType1Kind






T = TypeVar("T", bound="SearchTransparencyResponse200ModerationDataItemContentType1")



@_attrs_define
class SearchTransparencyResponse200ModerationDataItemContentType1:
    """ 
        Attributes:
            kind (SearchTransparencyResponse200ModerationDataItemContentType1Kind):
     """

    kind: SearchTransparencyResponse200ModerationDataItemContentType1Kind





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = SearchTransparencyResponse200ModerationDataItemContentType1Kind(d.pop("kind"))




        search_transparency_response_200_moderation_data_item_content_type_1 = cls(
            kind=kind,
        )

        return search_transparency_response_200_moderation_data_item_content_type_1

