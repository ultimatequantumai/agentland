from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="MarkInboxReadResponse200")



@_attrs_define
class MarkInboxReadResponse200:
    """ 
        Attributes:
            id (str):
            read_at (str):
     """

    id: str
    read_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        read_at = self.read_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "read_at": read_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        read_at = d.pop("read_at")

        mark_inbox_read_response_200 = cls(
            id=id,
            read_at=read_at,
        )

        return mark_inbox_read_response_200

