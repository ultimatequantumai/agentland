from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_transparency_response_200_sources_data_item_changes_item_status import SearchTransparencyResponse200SourcesDataItemChangesItemStatus






T = TypeVar("T", bound="SearchTransparencyResponse200SourcesDataItemChangesItem")



@_attrs_define
class SearchTransparencyResponse200SourcesDataItemChangesItem:
    """ 
        Attributes:
            at (str):
            status (SearchTransparencyResponse200SourcesDataItemChangesItemStatus):
            reason (str):
     """

    at: str
    status: SearchTransparencyResponse200SourcesDataItemChangesItemStatus
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

        status = SearchTransparencyResponse200SourcesDataItemChangesItemStatus(d.pop("status"))




        reason = d.pop("reason")

        search_transparency_response_200_sources_data_item_changes_item = cls(
            at=at,
            status=status,
            reason=reason,
        )

        return search_transparency_response_200_sources_data_item_changes_item

