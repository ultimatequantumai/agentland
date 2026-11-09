from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_incident_response_200_updates_item_kind import GetIncidentResponse200UpdatesItemKind






T = TypeVar("T", bound="GetIncidentResponse200UpdatesItem")



@_attrs_define
class GetIncidentResponse200UpdatesItem:
    """ 
        Attributes:
            kind (GetIncidentResponse200UpdatesItemKind):
            body (str):
            created_at (str):
     """

    kind: GetIncidentResponse200UpdatesItemKind
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
        kind = GetIncidentResponse200UpdatesItemKind(d.pop("kind"))




        body = d.pop("body")

        created_at = d.pop("created_at")

        get_incident_response_200_updates_item = cls(
            kind=kind,
            body=body,
            created_at=created_at,
        )

        return get_incident_response_200_updates_item

