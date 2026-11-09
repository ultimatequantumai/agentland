from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rotate_signing_key_body_new_public_key_crv import RotateSigningKeyBodyNewPublicKeyCrv
from ..models.rotate_signing_key_body_new_public_key_kty import RotateSigningKeyBodyNewPublicKeyKty






T = TypeVar("T", bound="RotateSigningKeyBodyNewPublicKey")



@_attrs_define
class RotateSigningKeyBodyNewPublicKey:
    """ 
        Attributes:
            kty (RotateSigningKeyBodyNewPublicKeyKty):
            crv (RotateSigningKeyBodyNewPublicKeyCrv):
            x (str):
     """

    kty: RotateSigningKeyBodyNewPublicKeyKty
    crv: RotateSigningKeyBodyNewPublicKeyCrv
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
        kty = RotateSigningKeyBodyNewPublicKeyKty(d.pop("kty"))




        crv = RotateSigningKeyBodyNewPublicKeyCrv(d.pop("crv"))




        x = d.pop("x")

        rotate_signing_key_body_new_public_key = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return rotate_signing_key_body_new_public_key

