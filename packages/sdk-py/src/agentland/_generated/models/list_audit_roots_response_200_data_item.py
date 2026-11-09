from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_audit_roots_response_200_data_item_anchor_status import ListAuditRootsResponse200DataItemAnchorStatus
from typing import cast
import datetime






T = TypeVar("T", bound="ListAuditRootsResponse200DataItem")



@_attrs_define
class ListAuditRootsResponse200DataItem:
    """ 
        Attributes:
            date (datetime.date):
            root (str):
            prev_root (str):
            published_at (str):
            anchor_status (ListAuditRootsResponse200DataItemAnchorStatus):
            block_height (int | None):
     """

    date: datetime.date
    root: str
    prev_root: str
    published_at: str
    anchor_status: ListAuditRootsResponse200DataItemAnchorStatus
    block_height: int | None





    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        root = self.root

        prev_root = self.prev_root

        published_at = self.published_at

        anchor_status = self.anchor_status.value

        block_height: int | None
        block_height = self.block_height


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "date": date,
            "root": root,
            "prev_root": prev_root,
            "published_at": published_at,
            "anchor_status": anchor_status,
            "block_height": block_height,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))




        root = d.pop("root")

        prev_root = d.pop("prev_root")

        published_at = d.pop("published_at")

        anchor_status = ListAuditRootsResponse200DataItemAnchorStatus(d.pop("anchor_status"))




        def _parse_block_height(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        block_height = _parse_block_height(d.pop("block_height"))


        list_audit_roots_response_200_data_item = cls(
            date=date,
            root=root,
            prev_root=prev_root,
            published_at=published_at,
            anchor_status=anchor_status,
            block_height=block_height,
        )

        return list_audit_roots_response_200_data_item

