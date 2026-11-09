from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_agent_body_public_signing_key_crv import CreateAgentBodyPublicSigningKeyCrv
from ..models.create_agent_body_public_signing_key_kty import CreateAgentBodyPublicSigningKeyKty






T = TypeVar("T", bound="CreateAgentBodyPublicSigningKey")



@_attrs_define
class CreateAgentBodyPublicSigningKey:
    """ 
        Attributes:
            kty (CreateAgentBodyPublicSigningKeyKty):
            crv (CreateAgentBodyPublicSigningKeyCrv):
            x (str):
     """

    kty: CreateAgentBodyPublicSigningKeyKty
    crv: CreateAgentBodyPublicSigningKeyCrv
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
        kty = CreateAgentBodyPublicSigningKeyKty(d.pop("kty"))




        crv = CreateAgentBodyPublicSigningKeyCrv(d.pop("crv"))




        x = d.pop("x")

        create_agent_body_public_signing_key = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return create_agent_body_public_signing_key

