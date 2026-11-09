from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PurgeVaultPayloadsBody")



@_attrs_define
class PurgeVaultPayloadsBody:
    """ 
        Attributes:
            seqs (list[str]):
     """

    seqs: list[str]





    def to_dict(self) -> dict[str, Any]:
        seqs = self.seqs




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "seqs": seqs,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seqs = cast(list[str], d.pop("seqs"))


        purge_vault_payloads_body = cls(
            seqs=seqs,
        )

        return purge_vault_payloads_body

