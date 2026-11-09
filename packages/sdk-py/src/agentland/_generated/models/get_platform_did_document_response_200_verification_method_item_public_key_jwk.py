from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_platform_did_document_response_200_verification_method_item_public_key_jwk_crv import GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwkCrv
from ..models.get_platform_did_document_response_200_verification_method_item_public_key_jwk_kty import GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwkKty






T = TypeVar("T", bound="GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwk")



@_attrs_define
class GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwk:
    """ 
        Attributes:
            kty (GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwkKty):
            crv (GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwkCrv):
            x (str):
     """

    kty: GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwkKty
    crv: GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwkCrv
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
        kty = GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwkKty(d.pop("kty"))




        crv = GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwkCrv(d.pop("crv"))




        x = d.pop("x")

        get_platform_did_document_response_200_verification_method_item_public_key_jwk = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return get_platform_did_document_response_200_verification_method_item_public_key_jwk

