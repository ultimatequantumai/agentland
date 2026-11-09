from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_vault_proof_response_200_type_1_bundle_audit_proof import GetVaultProofResponse200Type1BundleAuditProof





T = TypeVar("T", bound="GetVaultProofResponse200Type1BundleAudit")



@_attrs_define
class GetVaultProofResponse200Type1BundleAudit:
    """ 
        Attributes:
            vault_root_leaf_bytes (str):
            proof (GetVaultProofResponse200Type1BundleAuditProof):
     """

    vault_root_leaf_bytes: str
    proof: GetVaultProofResponse200Type1BundleAuditProof





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vault_proof_response_200_type_1_bundle_audit_proof import GetVaultProofResponse200Type1BundleAuditProof # noqa: PLC0415
        vault_root_leaf_bytes = self.vault_root_leaf_bytes

        proof = self.proof.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "vault_root_leaf_bytes": vault_root_leaf_bytes,
            "proof": proof,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vault_proof_response_200_type_1_bundle_audit_proof import GetVaultProofResponse200Type1BundleAuditProof # noqa: PLC0415
        d = dict(src_dict)
        vault_root_leaf_bytes = d.pop("vault_root_leaf_bytes")

        proof = GetVaultProofResponse200Type1BundleAuditProof.from_dict(d.pop("proof"))




        get_vault_proof_response_200_type_1_bundle_audit = cls(
            vault_root_leaf_bytes=vault_root_leaf_bytes,
            proof=proof,
        )

        return get_vault_proof_response_200_type_1_bundle_audit

