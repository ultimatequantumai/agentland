from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.register_signing_key_body_public_key_crv import RegisterSigningKeyBodyPublicKeyCrv
from ..models.register_signing_key_body_public_key_kty import RegisterSigningKeyBodyPublicKeyKty






T = TypeVar("T", bound="RegisterSigningKeyBodyPublicKey")



@_attrs_define
class RegisterSigningKeyBodyPublicKey:
    """ 
        Attributes:
            kty (RegisterSigningKeyBodyPublicKeyKty):
            crv (RegisterSigningKeyBodyPublicKeyCrv):
            x (str):
     """

    kty: RegisterSigningKeyBodyPublicKeyKty
    crv: RegisterSigningKeyBodyPublicKeyCrv
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
        kty = RegisterSigningKeyBodyPublicKeyKty(d.pop("kty"))




        crv = RegisterSigningKeyBodyPublicKeyCrv(d.pop("crv"))




        x = d.pop("x")

        register_signing_key_body_public_key = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return register_signing_key_body_public_key

