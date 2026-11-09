from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_transparency_moderation_case_response_200_actions_item_content_type_1_kind import GetTransparencyModerationCaseResponse200ActionsItemContentType1Kind






T = TypeVar("T", bound="GetTransparencyModerationCaseResponse200ActionsItemContentType1")



@_attrs_define
class GetTransparencyModerationCaseResponse200ActionsItemContentType1:
    """ 
        Attributes:
            kind (GetTransparencyModerationCaseResponse200ActionsItemContentType1Kind):
     """

    kind: GetTransparencyModerationCaseResponse200ActionsItemContentType1Kind





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
        kind = GetTransparencyModerationCaseResponse200ActionsItemContentType1Kind(d.pop("kind"))




        get_transparency_moderation_case_response_200_actions_item_content_type_1 = cls(
            kind=kind,
        )

        return get_transparency_moderation_case_response_200_actions_item_content_type_1

