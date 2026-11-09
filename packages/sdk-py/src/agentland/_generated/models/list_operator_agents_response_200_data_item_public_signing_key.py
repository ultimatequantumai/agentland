from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_operator_agents_response_200_data_item_public_signing_key_crv import ListOperatorAgentsResponse200DataItemPublicSigningKeyCrv
from ..models.list_operator_agents_response_200_data_item_public_signing_key_kty import ListOperatorAgentsResponse200DataItemPublicSigningKeyKty






T = TypeVar("T", bound="ListOperatorAgentsResponse200DataItemPublicSigningKey")



@_attrs_define
class ListOperatorAgentsResponse200DataItemPublicSigningKey:
    """ 
        Attributes:
            kty (ListOperatorAgentsResponse200DataItemPublicSigningKeyKty):
            crv (ListOperatorAgentsResponse200DataItemPublicSigningKeyCrv):
            x (str):
     """

    kty: ListOperatorAgentsResponse200DataItemPublicSigningKeyKty
    crv: ListOperatorAgentsResponse200DataItemPublicSigningKeyCrv
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
        kty = ListOperatorAgentsResponse200DataItemPublicSigningKeyKty(d.pop("kty"))




        crv = ListOperatorAgentsResponse200DataItemPublicSigningKeyCrv(d.pop("crv"))




        x = d.pop("x")

        list_operator_agents_response_200_data_item_public_signing_key = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return list_operator_agents_response_200_data_item_public_signing_key

