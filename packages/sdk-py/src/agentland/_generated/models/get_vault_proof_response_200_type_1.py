from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_vault_proof_response_200_type_1_status import GetVaultProofResponse200Type1Status
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_vault_proof_response_200_type_1_bundle import GetVaultProofResponse200Type1Bundle
  from ..models.get_vault_proof_response_200_type_1_entry import GetVaultProofResponse200Type1Entry





T = TypeVar("T", bound="GetVaultProofResponse200Type1")



@_attrs_define
class GetVaultProofResponse200Type1:
    """ 
        Attributes:
            status (GetVaultProofResponse200Type1Status):
            entry (GetVaultProofResponse200Type1Entry):
            hash_ (str):
            root_date (datetime.date):
            audit_root (str):
            bundle (GetVaultProofResponse200Type1Bundle):
     """

    status: GetVaultProofResponse200Type1Status
    entry: GetVaultProofResponse200Type1Entry
    hash_: str
    root_date: datetime.date
    audit_root: str
    bundle: GetVaultProofResponse200Type1Bundle





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vault_proof_response_200_type_1_bundle import GetVaultProofResponse200Type1Bundle # noqa: PLC0415
        from ..models.get_vault_proof_response_200_type_1_entry import GetVaultProofResponse200Type1Entry # noqa: PLC0415
        status = self.status.value

        entry = self.entry.to_dict()

        hash_ = self.hash_

        root_date = self.root_date.isoformat()

        audit_root = self.audit_root

        bundle = self.bundle.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "entry": entry,
            "hash": hash_,
            "root_date": root_date,
            "audit_root": audit_root,
            "bundle": bundle,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vault_proof_response_200_type_1_bundle import GetVaultProofResponse200Type1Bundle # noqa: PLC0415
        from ..models.get_vault_proof_response_200_type_1_entry import GetVaultProofResponse200Type1Entry # noqa: PLC0415
        d = dict(src_dict)
        status = GetVaultProofResponse200Type1Status(d.pop("status"))




        entry = GetVaultProofResponse200Type1Entry.from_dict(d.pop("entry"))




        hash_ = d.pop("hash")

        root_date = datetime.date.fromisoformat(d.pop("root_date"))




        audit_root = d.pop("audit_root")

        bundle = GetVaultProofResponse200Type1Bundle.from_dict(d.pop("bundle"))




        get_vault_proof_response_200_type_1 = cls(
            status=status,
            entry=entry,
            hash_=hash_,
            root_date=root_date,
            audit_root=audit_root,
            bundle=bundle,
        )

        return get_vault_proof_response_200_type_1

