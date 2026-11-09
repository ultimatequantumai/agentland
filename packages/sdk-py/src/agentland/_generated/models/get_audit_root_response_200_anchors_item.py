from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_audit_root_response_200_anchors_item_status import GetAuditRootResponse200AnchorsItemStatus
from typing import cast






T = TypeVar("T", bound="GetAuditRootResponse200AnchorsItem")



@_attrs_define
class GetAuditRootResponse200AnchorsItem:
    """ 
        Attributes:
            calendar (str):
            status (GetAuditRootResponse200AnchorsItemStatus):
            block_height (int | None):
            created_at (str):
            error (None | str):
     """

    calendar: str
    status: GetAuditRootResponse200AnchorsItemStatus
    block_height: int | None
    created_at: str
    error: None | str





    def to_dict(self) -> dict[str, Any]:
        calendar = self.calendar

        status = self.status.value

        block_height: int | None
        block_height = self.block_height

        created_at = self.created_at

        error: None | str
        error = self.error


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "calendar": calendar,
            "status": status,
            "block_height": block_height,
            "created_at": created_at,
            "error": error,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calendar = d.pop("calendar")

        status = GetAuditRootResponse200AnchorsItemStatus(d.pop("status"))




        def _parse_block_height(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        block_height = _parse_block_height(d.pop("block_height"))


        created_at = d.pop("created_at")

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))


        get_audit_root_response_200_anchors_item = cls(
            calendar=calendar,
            status=status,
            block_height=block_height,
            created_at=created_at,
            error=error,
        )

        return get_audit_root_response_200_anchors_item

