from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_agent_did_history_response_200_rotations_item_statement_new_pub_crv import GetAgentDidHistoryResponse200RotationsItemStatementNewPubCrv
from ..models.get_agent_did_history_response_200_rotations_item_statement_new_pub_kty import GetAgentDidHistoryResponse200RotationsItemStatementNewPubKty






T = TypeVar("T", bound="GetAgentDidHistoryResponse200RotationsItemStatementNewPub")



@_attrs_define
class GetAgentDidHistoryResponse200RotationsItemStatementNewPub:
    """ 
        Attributes:
            kty (GetAgentDidHistoryResponse200RotationsItemStatementNewPubKty):
            crv (GetAgentDidHistoryResponse200RotationsItemStatementNewPubCrv):
            x (str):
     """

    kty: GetAgentDidHistoryResponse200RotationsItemStatementNewPubKty
    crv: GetAgentDidHistoryResponse200RotationsItemStatementNewPubCrv
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
        kty = GetAgentDidHistoryResponse200RotationsItemStatementNewPubKty(d.pop("kty"))




        crv = GetAgentDidHistoryResponse200RotationsItemStatementNewPubCrv(d.pop("crv"))




        x = d.pop("x")

        get_agent_did_history_response_200_rotations_item_statement_new_pub = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return get_agent_did_history_response_200_rotations_item_statement_new_pub

