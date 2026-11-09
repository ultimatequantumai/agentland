from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.cancel_recovery_by_operator_response_200_new_public_key_crv import CancelRecoveryByOperatorResponse200NewPublicKeyCrv
from ..models.cancel_recovery_by_operator_response_200_new_public_key_kty import CancelRecoveryByOperatorResponse200NewPublicKeyKty






T = TypeVar("T", bound="CancelRecoveryByOperatorResponse200NewPublicKey")



@_attrs_define
class CancelRecoveryByOperatorResponse200NewPublicKey:
    """ 
        Attributes:
            kty (CancelRecoveryByOperatorResponse200NewPublicKeyKty):
            crv (CancelRecoveryByOperatorResponse200NewPublicKeyCrv):
            x (str):
     """

    kty: CancelRecoveryByOperatorResponse200NewPublicKeyKty
    crv: CancelRecoveryByOperatorResponse200NewPublicKeyCrv
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
        kty = CancelRecoveryByOperatorResponse200NewPublicKeyKty(d.pop("kty"))




        crv = CancelRecoveryByOperatorResponse200NewPublicKeyCrv(d.pop("crv"))




        x = d.pop("x")

        cancel_recovery_by_operator_response_200_new_public_key = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return cancel_recovery_by_operator_response_200_new_public_key

