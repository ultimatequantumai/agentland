from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetMeResponse200Vault")



@_attrs_define
class GetMeResponse200Vault:
    """ 
        Attributes:
            seq (str):
            head_hash (str):
     """

    seq: str
    head_hash: str





    def to_dict(self) -> dict[str, Any]:
        seq = self.seq

        head_hash = self.head_hash


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "seq": seq,
            "head_hash": head_hash,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seq = d.pop("seq")

        head_hash = d.pop("head_hash")

        get_me_response_200_vault = cls(
            seq=seq,
            head_hash=head_hash,
        )

        return get_me_response_200_vault

