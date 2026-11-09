from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.register_signing_key_response_201_public_key_crv import RegisterSigningKeyResponse201PublicKeyCrv
from ..models.register_signing_key_response_201_public_key_kty import RegisterSigningKeyResponse201PublicKeyKty






T = TypeVar("T", bound="RegisterSigningKeyResponse201PublicKey")



@_attrs_define
class RegisterSigningKeyResponse201PublicKey:
    """ 
        Attributes:
            kty (RegisterSigningKeyResponse201PublicKeyKty):
            crv (RegisterSigningKeyResponse201PublicKeyCrv):
            x (str):
     """

    kty: RegisterSigningKeyResponse201PublicKeyKty
    crv: RegisterSigningKeyResponse201PublicKeyCrv
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
        kty = RegisterSigningKeyResponse201PublicKeyKty(d.pop("kty"))




        crv = RegisterSigningKeyResponse201PublicKeyCrv(d.pop("crv"))




        x = d.pop("x")

        register_signing_key_response_201_public_key = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return register_signing_key_response_201_public_key

