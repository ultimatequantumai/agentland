from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.start_recovery_response_201_new_public_key_crv import StartRecoveryResponse201NewPublicKeyCrv
from ..models.start_recovery_response_201_new_public_key_kty import StartRecoveryResponse201NewPublicKeyKty






T = TypeVar("T", bound="StartRecoveryResponse201NewPublicKey")



@_attrs_define
class StartRecoveryResponse201NewPublicKey:
    """ 
        Attributes:
            kty (StartRecoveryResponse201NewPublicKeyKty):
            crv (StartRecoveryResponse201NewPublicKeyCrv):
            x (str):
     """

    kty: StartRecoveryResponse201NewPublicKeyKty
    crv: StartRecoveryResponse201NewPublicKeyCrv
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
        kty = StartRecoveryResponse201NewPublicKeyKty(d.pop("kty"))




        crv = StartRecoveryResponse201NewPublicKeyCrv(d.pop("crv"))




        x = d.pop("x")

        start_recovery_response_201_new_public_key = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return start_recovery_response_201_new_public_key

