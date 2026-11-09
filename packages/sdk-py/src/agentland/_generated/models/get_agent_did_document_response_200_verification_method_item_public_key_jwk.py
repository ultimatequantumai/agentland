from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_agent_did_document_response_200_verification_method_item_public_key_jwk_crv import GetAgentDidDocumentResponse200VerificationMethodItemPublicKeyJwkCrv
from ..models.get_agent_did_document_response_200_verification_method_item_public_key_jwk_kty import GetAgentDidDocumentResponse200VerificationMethodItemPublicKeyJwkKty






T = TypeVar("T", bound="GetAgentDidDocumentResponse200VerificationMethodItemPublicKeyJwk")



@_attrs_define
class GetAgentDidDocumentResponse200VerificationMethodItemPublicKeyJwk:
    """ 
        Attributes:
            kty (GetAgentDidDocumentResponse200VerificationMethodItemPublicKeyJwkKty):
            crv (GetAgentDidDocumentResponse200VerificationMethodItemPublicKeyJwkCrv):
            x (str):
     """

    kty: GetAgentDidDocumentResponse200VerificationMethodItemPublicKeyJwkKty
    crv: GetAgentDidDocumentResponse200VerificationMethodItemPublicKeyJwkCrv
    x: str





    def to_dict(self) -> dict[str, Any]:
        kty = self.kty.value

        crv = self.crv.value

        x = self.x


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kty": kty,
            "crv": crv,
            "x": x,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kty = GetAgentDidDocumentResponse200VerificationMethodItemPublicKeyJwkKty(d.pop("kty"))




        crv = GetAgentDidDocumentResponse200VerificationMethodItemPublicKeyJwkCrv(d.pop("crv"))




        x = d.pop("x")

        get_agent_did_document_response_200_verification_method_item_public_key_jwk = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return get_agent_did_document_response_200_verification_method_item_public_key_jwk

