from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_status_response_200_open_incidents_item_latest_update_kind import GetStatusResponse200OpenIncidentsItemLatestUpdateKind






T = TypeVar("T", bound="GetStatusResponse200OpenIncidentsItemLatestUpdate")



@_attrs_define
class GetStatusResponse200OpenIncidentsItemLatestUpdate:
    """ 
        Attributes:
            kind (GetStatusResponse200OpenIncidentsItemLatestUpdateKind):
            created_at (str):
     """

    kind: GetStatusResponse200OpenIncidentsItemLatestUpdateKind
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = GetStatusResponse200OpenIncidentsItemLatestUpdateKind(d.pop("kind"))




        created_at = d.pop("created_at")

        get_status_response_200_open_incidents_item_latest_update = cls(
            kind=kind,
            created_at=created_at,
        )

        return get_status_response_200_open_incidents_item_latest_update

