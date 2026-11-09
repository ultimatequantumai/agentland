from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_me_response_200_agent_public_signing_key_crv import GetMeResponse200AgentPublicSigningKeyCrv
from ..models.get_me_response_200_agent_public_signing_key_kty import GetMeResponse200AgentPublicSigningKeyKty






T = TypeVar("T", bound="GetMeResponse200AgentPublicSigningKey")



@_attrs_define
class GetMeResponse200AgentPublicSigningKey:
    """ 
        Attributes:
            kty (GetMeResponse200AgentPublicSigningKeyKty):
            crv (GetMeResponse200AgentPublicSigningKeyCrv):
            x (str):
     """

    kty: GetMeResponse200AgentPublicSigningKeyKty
    crv: GetMeResponse200AgentPublicSigningKeyCrv
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
        kty = GetMeResponse200AgentPublicSigningKeyKty(d.pop("kty"))




        crv = GetMeResponse200AgentPublicSigningKeyCrv(d.pop("crv"))




        x = d.pop("x")

        get_me_response_200_agent_public_signing_key = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return get_me_response_200_agent_public_signing_key

