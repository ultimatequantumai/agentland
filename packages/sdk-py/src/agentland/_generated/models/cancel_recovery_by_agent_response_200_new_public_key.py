from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.cancel_recovery_by_agent_response_200_new_public_key_crv import CancelRecoveryByAgentResponse200NewPublicKeyCrv
from ..models.cancel_recovery_by_agent_response_200_new_public_key_kty import CancelRecoveryByAgentResponse200NewPublicKeyKty






T = TypeVar("T", bound="CancelRecoveryByAgentResponse200NewPublicKey")



@_attrs_define
class CancelRecoveryByAgentResponse200NewPublicKey:
    """ 
        Attributes:
            kty (CancelRecoveryByAgentResponse200NewPublicKeyKty):
            crv (CancelRecoveryByAgentResponse200NewPublicKeyCrv):
            x (str):
     """

    kty: CancelRecoveryByAgentResponse200NewPublicKeyKty
    crv: CancelRecoveryByAgentResponse200NewPublicKeyCrv
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
        kty = CancelRecoveryByAgentResponse200NewPublicKeyKty(d.pop("kty"))




        crv = CancelRecoveryByAgentResponse200NewPublicKeyCrv(d.pop("crv"))




        x = d.pop("x")

        cancel_recovery_by_agent_response_200_new_public_key = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return cancel_recovery_by_agent_response_200_new_public_key

