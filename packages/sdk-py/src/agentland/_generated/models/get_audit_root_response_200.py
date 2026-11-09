from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_audit_root_response_200_format import GetAuditRootResponse200Format
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_audit_root_response_200_anchors_item import GetAuditRootResponse200AnchorsItem
  from ..models.get_audit_root_response_200_leaves_item import GetAuditRootResponse200LeavesItem





T = TypeVar("T", bound="GetAuditRootResponse200")



@_attrs_define
class GetAuditRootResponse200:
    """ 
        Attributes:
            format_ (GetAuditRootResponse200Format):
            date (datetime.date):
            root (str):
            prev_root (str):
            published_at (str):
            leaves (list[GetAuditRootResponse200LeavesItem]):
            anchors (list[GetAuditRootResponse200AnchorsItem]):
     """

    format_: GetAuditRootResponse200Format
    date: datetime.date
    root: str
    prev_root: str
    published_at: str
    leaves: list[GetAuditRootResponse200LeavesItem]
    anchors: list[GetAuditRootResponse200AnchorsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_audit_root_response_200_anchors_item import GetAuditRootResponse200AnchorsItem # noqa: PLC0415
        from ..models.get_audit_root_response_200_leaves_item import GetAuditRootResponse200LeavesItem # noqa: PLC0415
        format_ = self.format_.value

        date = self.date.isoformat()

        root = self.root

        prev_root = self.prev_root

        published_at = self.published_at

        leaves = []
        for leaves_item_data in self.leaves:
            leaves_item = leaves_item_data.to_dict()
            leaves.append(leaves_item)



        anchors = []
        for anchors_item_data in self.anchors:
            anchors_item = anchors_item_data.to_dict()
            anchors.append(anchors_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "format": format_,
            "date": date,
            "root": root,
            "prev_root": prev_root,
            "published_at": published_at,
            "leaves": leaves,
            "anchors": anchors,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_audit_root_response_200_anchors_item import GetAuditRootResponse200AnchorsItem # noqa: PLC0415
        from ..models.get_audit_root_response_200_leaves_item import GetAuditRootResponse200LeavesItem # noqa: PLC0415
        d = dict(src_dict)
        format_ = GetAuditRootResponse200Format(d.pop("format"))




        date = datetime.date.fromisoformat(d.pop("date"))




        root = d.pop("root")

        prev_root = d.pop("prev_root")

        published_at = d.pop("published_at")

        leaves = []
        _leaves = d.pop("leaves")
        for leaves_item_data in (_leaves):
            leaves_item = GetAuditRootResponse200LeavesItem.from_dict(leaves_item_data)



            leaves.append(leaves_item)


        anchors = []
        _anchors = d.pop("anchors")
        for anchors_item_data in (_anchors):
            anchors_item = GetAuditRootResponse200AnchorsItem.from_dict(anchors_item_data)



            anchors.append(anchors_item)


        get_audit_root_response_200 = cls(
            format_=format_,
            date=date,
            root=root,
            prev_root=prev_root,
            published_at=published_at,
            leaves=leaves,
            anchors=anchors,
        )

        return get_audit_root_response_200

