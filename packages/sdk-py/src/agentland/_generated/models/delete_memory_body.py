from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DeleteMemoryBody")



@_attrs_define
class DeleteMemoryBody:
    """ 
        Attributes:
            if_seq (str | Unset):
            signature (str | Unset):
     """

    if_seq: str | Unset = UNSET
    signature: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        if_seq = self.if_seq

        signature = self.signature


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if if_seq is not UNSET:
            field_dict["if_seq"] = if_seq
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        if_seq = d.pop("if_seq", UNSET)

        signature = d.pop("signature", UNSET)

        delete_memory_body = cls(
            if_seq=if_seq,
            signature=signature,
        )

        return delete_memory_body

