from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_transparency_moderation_response_200_data_item_content_type_1_kind import ListTransparencyModerationResponse200DataItemContentType1Kind






T = TypeVar("T", bound="ListTransparencyModerationResponse200DataItemContentType1")



@_attrs_define
class ListTransparencyModerationResponse200DataItemContentType1:
    """ 
        Attributes:
            kind (ListTransparencyModerationResponse200DataItemContentType1Kind):
     """

    kind: ListTransparencyModerationResponse200DataItemContentType1Kind





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
        kind = ListTransparencyModerationResponse200DataItemContentType1Kind(d.pop("kind"))




        list_transparency_moderation_response_200_data_item_content_type_1 = cls(
            kind=kind,
        )

        return list_transparency_moderation_response_200_data_item_content_type_1

