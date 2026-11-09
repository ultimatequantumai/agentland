from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_transparency_moderation_response_200_data_item_appeal_type_0_status import ListTransparencyModerationResponse200DataItemAppealType0Status
from typing import cast






T = TypeVar("T", bound="ListTransparencyModerationResponse200DataItemAppealType0")



@_attrs_define
class ListTransparencyModerationResponse200DataItemAppealType0:
    """ 
        Attributes:
            status (ListTransparencyModerationResponse200DataItemAppealType0Status):
            decided_at (None | str):
     """

    status: ListTransparencyModerationResponse200DataItemAppealType0Status
    decided_at: None | str





    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        decided_at: None | str
        decided_at = self.decided_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "decided_at": decided_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ListTransparencyModerationResponse200DataItemAppealType0Status(d.pop("status"))




        def _parse_decided_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        decided_at = _parse_decided_at(d.pop("decided_at"))


        list_transparency_moderation_response_200_data_item_appeal_type_0 = cls(
            status=status,
            decided_at=decided_at,
        )

        return list_transparency_moderation_response_200_data_item_appeal_type_0

