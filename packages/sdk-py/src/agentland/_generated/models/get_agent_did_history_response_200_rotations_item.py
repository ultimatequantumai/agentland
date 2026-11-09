from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_agent_did_history_response_200_rotations_item_signatures import GetAgentDidHistoryResponse200RotationsItemSignatures
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_agent_did_history_response_200_rotations_item_statement import GetAgentDidHistoryResponse200RotationsItemStatement





T = TypeVar("T", bound="GetAgentDidHistoryResponse200RotationsItem")



@_attrs_define
class GetAgentDidHistoryResponse200RotationsItem:
    """ 
        Attributes:
            statement (GetAgentDidHistoryResponse200RotationsItemStatement):
            sig_old (str):
            signatures (GetAgentDidHistoryResponse200RotationsItemSignatures):
            sig_new (str | Unset):
     """

    statement: GetAgentDidHistoryResponse200RotationsItemStatement
    sig_old: str
    signatures: GetAgentDidHistoryResponse200RotationsItemSignatures
    sig_new: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_did_history_response_200_rotations_item_statement import GetAgentDidHistoryResponse200RotationsItemStatement # noqa: PLC0415
        statement = self.statement.to_dict()

        sig_old = self.sig_old

        signatures = self.signatures.value

        sig_new = self.sig_new


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "statement": statement,
            "sig_old": sig_old,
            "signatures": signatures,
        })
        if sig_new is not UNSET:
            field_dict["sig_new"] = sig_new

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_did_history_response_200_rotations_item_statement import GetAgentDidHistoryResponse200RotationsItemStatement # noqa: PLC0415
        d = dict(src_dict)
        statement = GetAgentDidHistoryResponse200RotationsItemStatement.from_dict(d.pop("statement"))




        sig_old = d.pop("sig_old")

        signatures = GetAgentDidHistoryResponse200RotationsItemSignatures(d.pop("signatures"))




        sig_new = d.pop("sig_new", UNSET)

        get_agent_did_history_response_200_rotations_item = cls(
            statement=statement,
            sig_old=sig_old,
            signatures=signatures,
            sig_new=sig_new,
        )

        return get_agent_did_history_response_200_rotations_item

