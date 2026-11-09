from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_audit_root_response_200_leaves_item_kind import GetAuditRootResponse200LeavesItemKind






T = TypeVar("T", bound="GetAuditRootResponse200LeavesItem")



@_attrs_define
class GetAuditRootResponse200LeavesItem:
    """ 
        Attributes:
            kind (GetAuditRootResponse200LeavesItemKind):
            leaf (str):
     """

    kind: GetAuditRootResponse200LeavesItemKind
    leaf: str





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        leaf = self.leaf


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
            "leaf": leaf,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = GetAuditRootResponse200LeavesItemKind(d.pop("kind"))




        leaf = d.pop("leaf")

        get_audit_root_response_200_leaves_item = cls(
            kind=kind,
            leaf=leaf,
        )

        return get_audit_root_response_200_leaves_item

