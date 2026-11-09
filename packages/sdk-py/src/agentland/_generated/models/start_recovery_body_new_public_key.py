from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.start_recovery_body_new_public_key_crv import StartRecoveryBodyNewPublicKeyCrv
from ..models.start_recovery_body_new_public_key_kty import StartRecoveryBodyNewPublicKeyKty






T = TypeVar("T", bound="StartRecoveryBodyNewPublicKey")



@_attrs_define
class StartRecoveryBodyNewPublicKey:
    """ 
        Attributes:
            kty (StartRecoveryBodyNewPublicKeyKty):
            crv (StartRecoveryBodyNewPublicKeyCrv):
            x (str):
     """

    kty: StartRecoveryBodyNewPublicKeyKty
    crv: StartRecoveryBodyNewPublicKeyCrv
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
        kty = StartRecoveryBodyNewPublicKeyKty(d.pop("kty"))




        crv = StartRecoveryBodyNewPublicKeyCrv(d.pop("crv"))




        x = d.pop("x")

        start_recovery_body_new_public_key = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return start_recovery_body_new_public_key

