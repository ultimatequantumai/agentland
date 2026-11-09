from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_platform_did_document_response_200_verification_method_item_type import GetPlatformDidDocumentResponse200VerificationMethodItemType
from typing import cast

if TYPE_CHECKING:
  from ..models.get_platform_did_document_response_200_verification_method_item_public_key_jwk import GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwk





T = TypeVar("T", bound="GetPlatformDidDocumentResponse200VerificationMethodItem")



@_attrs_define
class GetPlatformDidDocumentResponse200VerificationMethodItem:
    """ 
        Attributes:
            id (str):
            controller (str):
            type_ (GetPlatformDidDocumentResponse200VerificationMethodItemType):
            public_key_jwk (GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwk):
     """

    id: str
    controller: str
    type_: GetPlatformDidDocumentResponse200VerificationMethodItemType
    public_key_jwk: GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwk





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_platform_did_document_response_200_verification_method_item_public_key_jwk import GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwk # noqa: PLC0415
        id = self.id

        controller = self.controller

        type_ = self.type_.value

        public_key_jwk = self.public_key_jwk.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "controller": controller,
            "type": type_,
            "publicKeyJwk": public_key_jwk,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_platform_did_document_response_200_verification_method_item_public_key_jwk import GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwk # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        controller = d.pop("controller")

        type_ = GetPlatformDidDocumentResponse200VerificationMethodItemType(d.pop("type"))




        public_key_jwk = GetPlatformDidDocumentResponse200VerificationMethodItemPublicKeyJwk.from_dict(d.pop("publicKeyJwk"))




        get_platform_did_document_response_200_verification_method_item = cls(
            id=id,
            controller=controller,
            type_=type_,
            public_key_jwk=public_key_jwk,
        )

        return get_platform_did_document_response_200_verification_method_item

