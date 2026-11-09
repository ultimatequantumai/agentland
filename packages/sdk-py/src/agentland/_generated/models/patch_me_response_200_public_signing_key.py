from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.patch_me_response_200_public_signing_key_crv import PatchMeResponse200PublicSigningKeyCrv
from ..models.patch_me_response_200_public_signing_key_kty import PatchMeResponse200PublicSigningKeyKty






T = TypeVar("T", bound="PatchMeResponse200PublicSigningKey")



@_attrs_define
class PatchMeResponse200PublicSigningKey:
    """ 
        Attributes:
            kty (PatchMeResponse200PublicSigningKeyKty):
            crv (PatchMeResponse200PublicSigningKeyCrv):
            x (str):
     """

    kty: PatchMeResponse200PublicSigningKeyKty
    crv: PatchMeResponse200PublicSigningKeyCrv
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
        kty = PatchMeResponse200PublicSigningKeyKty(d.pop("kty"))




        crv = PatchMeResponse200PublicSigningKeyCrv(d.pop("crv"))




        x = d.pop("x")

        patch_me_response_200_public_signing_key = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return patch_me_response_200_public_signing_key

