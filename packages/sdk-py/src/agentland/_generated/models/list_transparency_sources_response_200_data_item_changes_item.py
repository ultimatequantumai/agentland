from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_transparency_sources_response_200_data_item_changes_item_status import ListTransparencySourcesResponse200DataItemChangesItemStatus






T = TypeVar("T", bound="ListTransparencySourcesResponse200DataItemChangesItem")



@_attrs_define
class ListTransparencySourcesResponse200DataItemChangesItem:
    """ 
        Attributes:
            at (str):
            status (ListTransparencySourcesResponse200DataItemChangesItemStatus):
            reason (str):
     """

    at: str
    status: ListTransparencySourcesResponse200DataItemChangesItemStatus
    reason: str





    def to_dict(self) -> dict[str, Any]:
        at = self.at

        status = self.status.value

        reason = self.reason


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "at": at,
            "status": status,
            "reason": reason,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        at = d.pop("at")

        status = ListTransparencySourcesResponse200DataItemChangesItemStatus(d.pop("status"))




        reason = d.pop("reason")

        list_transparency_sources_response_200_data_item_changes_item = cls(
            at=at,
            status=status,
            reason=reason,
        )

        return list_transparency_sources_response_200_data_item_changes_item

