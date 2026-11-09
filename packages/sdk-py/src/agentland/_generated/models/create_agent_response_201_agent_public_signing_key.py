from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_agent_response_201_agent_public_signing_key_crv import CreateAgentResponse201AgentPublicSigningKeyCrv
from ..models.create_agent_response_201_agent_public_signing_key_kty import CreateAgentResponse201AgentPublicSigningKeyKty






T = TypeVar("T", bound="CreateAgentResponse201AgentPublicSigningKey")



@_attrs_define
class CreateAgentResponse201AgentPublicSigningKey:
    """ 
        Attributes:
            kty (CreateAgentResponse201AgentPublicSigningKeyKty):
            crv (CreateAgentResponse201AgentPublicSigningKeyCrv):
            x (str):
     """

    kty: CreateAgentResponse201AgentPublicSigningKeyKty
    crv: CreateAgentResponse201AgentPublicSigningKeyCrv
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
        kty = CreateAgentResponse201AgentPublicSigningKeyKty(d.pop("kty"))




        crv = CreateAgentResponse201AgentPublicSigningKeyCrv(d.pop("crv"))




        x = d.pop("x")

        create_agent_response_201_agent_public_signing_key = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return create_agent_response_201_agent_public_signing_key

