from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_incidents_response_200_data_item_updates_item_kind import ListIncidentsResponse200DataItemUpdatesItemKind






T = TypeVar("T", bound="ListIncidentsResponse200DataItemUpdatesItem")



@_attrs_define
class ListIncidentsResponse200DataItemUpdatesItem:
    """ 
        Attributes:
            kind (ListIncidentsResponse200DataItemUpdatesItemKind):
            body (str):
            created_at (str):
     """

    kind: ListIncidentsResponse200DataItemUpdatesItemKind
    body: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        body = self.body

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
            "body": body,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = ListIncidentsResponse200DataItemUpdatesItemKind(d.pop("kind"))




        body = d.pop("body")

        created_at = d.pop("created_at")

        list_incidents_response_200_data_item_updates_item = cls(
            kind=kind,
            body=body,
            created_at=created_at,
        )

        return list_incidents_response_200_data_item_updates_item

