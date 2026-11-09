from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.delete_memory_response_201_entry import DeleteMemoryResponse201Entry





T = TypeVar("T", bound="DeleteMemoryResponse201")



@_attrs_define
class DeleteMemoryResponse201:
    """ 
        Attributes:
            entry (DeleteMemoryResponse201Entry):
            hash_ (str):
     """

    entry: DeleteMemoryResponse201Entry
    hash_: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.delete_memory_response_201_entry import DeleteMemoryResponse201Entry # noqa: PLC0415
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
        from ..models.delete_memory_response_201_entry import DeleteMemoryResponse201Entry # noqa: PLC0415
        d = dict(src_dict)
        entry = DeleteMemoryResponse201Entry.from_dict(d.pop("entry"))




        hash_ = d.pop("hash")

        delete_memory_response_201 = cls(
            entry=entry,
            hash_=hash_,
        )

        return delete_memory_response_201

