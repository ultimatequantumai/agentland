from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_vault_proof_response_200_type_0_status import GetVaultProofResponse200Type0Status
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vault_proof_response_200_type_0_entry import GetVaultProofResponse200Type0Entry





T = TypeVar("T", bound="GetVaultProofResponse200Type0")



@_attrs_define
class GetVaultProofResponse200Type0:
    """ 
        Attributes:
            status (GetVaultProofResponse200Type0Status):
            entry (GetVaultProofResponse200Type0Entry):
            hash_ (str):
     """

    status: GetVaultProofResponse200Type0Status
    entry: GetVaultProofResponse200Type0Entry
    hash_: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vault_proof_response_200_type_0_entry import GetVaultProofResponse200Type0Entry # noqa: PLC0415
        status = self.status.value

        entry = self.entry.to_dict()

        hash_ = self.hash_


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "entry": entry,
            "hash": hash_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vault_proof_response_200_type_0_entry import GetVaultProofResponse200Type0Entry # noqa: PLC0415
        d = dict(src_dict)
        status = GetVaultProofResponse200Type0Status(d.pop("status"))




        entry = GetVaultProofResponse200Type0Entry.from_dict(d.pop("entry"))




        hash_ = d.pop("hash")

        get_vault_proof_response_200_type_0 = cls(
            status=status,
            entry=entry,
            hash_=hash_,
        )

        return get_vault_proof_response_200_type_0

