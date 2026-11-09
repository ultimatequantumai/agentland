from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.put_memory_response_201_entry import PutMemoryResponse201Entry





T = TypeVar("T", bound="PutMemoryResponse201")



@_attrs_define
class PutMemoryResponse201:
    """ 
        Attributes:
            entry (PutMemoryResponse201Entry):
            hash_ (str):
     """

    entry: PutMemoryResponse201Entry
    hash_: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_memory_response_201_entry import PutMemoryResponse201Entry # noqa: PLC0415
        entry = self.entry.to_dict()

        hash_ = self.hash_


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "entry": entry,
            "hash": hash_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_memory_response_201_entry import PutMemoryResponse201Entry # noqa: PLC0415
        d = dict(src_dict)
        entry = PutMemoryResponse201Entry.from_dict(d.pop("entry"))




        hash_ = d.pop("hash")

        put_memory_response_201 = cls(
            entry=entry,
            hash_=hash_,
        )

        return put_memory_response_201

