from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rotate_signing_key_response_201_type_0_key_public_key_crv import RotateSigningKeyResponse201Type0KeyPublicKeyCrv
from ..models.rotate_signing_key_response_201_type_0_key_public_key_kty import RotateSigningKeyResponse201Type0KeyPublicKeyKty






T = TypeVar("T", bound="RotateSigningKeyResponse201Type0KeyPublicKey")



@_attrs_define
class RotateSigningKeyResponse201Type0KeyPublicKey:
    """ 
        Attributes:
            kty (RotateSigningKeyResponse201Type0KeyPublicKeyKty):
            crv (RotateSigningKeyResponse201Type0KeyPublicKeyCrv):
            x (str):
     """

    kty: RotateSigningKeyResponse201Type0KeyPublicKeyKty
    crv: RotateSigningKeyResponse201Type0KeyPublicKeyCrv
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
        kty = RotateSigningKeyResponse201Type0KeyPublicKeyKty(d.pop("kty"))




        crv = RotateSigningKeyResponse201Type0KeyPublicKeyCrv(d.pop("crv"))




        x = d.pop("x")

        rotate_signing_key_response_201_type_0_key_public_key = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return rotate_signing_key_response_201_type_0_key_public_key

