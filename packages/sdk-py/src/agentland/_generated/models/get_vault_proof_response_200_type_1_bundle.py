from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_vault_proof_response_200_type_1_bundle_format import GetVaultProofResponse200Type1BundleFormat
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vault_proof_response_200_type_1_bundle_audit import GetVaultProofResponse200Type1BundleAudit
  from ..models.get_vault_proof_response_200_type_1_bundle_entries_item import GetVaultProofResponse200Type1BundleEntriesItem
  from ..models.get_vault_proof_response_200_type_1_bundle_proof import GetVaultProofResponse200Type1BundleProof





T = TypeVar("T", bound="GetVaultProofResponse200Type1Bundle")



@_attrs_define
class GetVaultProofResponse200Type1Bundle:
    """ 
        Attributes:
            format_ (GetVaultProofResponse200Type1BundleFormat):
            did (str):
            entries (list[GetVaultProofResponse200Type1BundleEntriesItem]):
            proof (GetVaultProofResponse200Type1BundleProof):
            audit (GetVaultProofResponse200Type1BundleAudit):
     """

    format_: GetVaultProofResponse200Type1BundleFormat
    did: str
    entries: list[GetVaultProofResponse200Type1BundleEntriesItem]
    proof: GetVaultProofResponse200Type1BundleProof
    audit: GetVaultProofResponse200Type1BundleAudit





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vault_proof_response_200_type_1_bundle_audit import GetVaultProofResponse200Type1BundleAudit # noqa: PLC0415
        from ..models.get_vault_proof_response_200_type_1_bundle_entries_item import GetVaultProofResponse200Type1BundleEntriesItem # noqa: PLC0415
        from ..models.get_vault_proof_response_200_type_1_bundle_proof import GetVaultProofResponse200Type1BundleProof # noqa: PLC0415
        format_ = self.format_.value

        did = self.did

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)



        proof = self.proof.to_dict()

        audit = self.audit.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "format": format_,
            "did": did,
            "entries": entries,
            "proof": proof,
            "audit": audit,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vault_proof_response_200_type_1_bundle_audit import GetVaultProofResponse200Type1BundleAudit # noqa: PLC0415
        from ..models.get_vault_proof_response_200_type_1_bundle_entries_item import GetVaultProofResponse200Type1BundleEntriesItem # noqa: PLC0415
        from ..models.get_vault_proof_response_200_type_1_bundle_proof import GetVaultProofResponse200Type1BundleProof # noqa: PLC0415
        d = dict(src_dict)
        format_ = GetVaultProofResponse200Type1BundleFormat(d.pop("format"))




        did = d.pop("did")

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in (_entries):
            entries_item = GetVaultProofResponse200Type1BundleEntriesItem.from_dict(entries_item_data)



            entries.append(entries_item)


        proof = GetVaultProofResponse200Type1BundleProof.from_dict(d.pop("proof"))




        audit = GetVaultProofResponse200Type1BundleAudit.from_dict(d.pop("audit"))




        get_vault_proof_response_200_type_1_bundle = cls(
            format_=format_,
            did=did,
            entries=entries,
            proof=proof,
            audit=audit,
        )

        return get_vault_proof_response_200_type_1_bundle

