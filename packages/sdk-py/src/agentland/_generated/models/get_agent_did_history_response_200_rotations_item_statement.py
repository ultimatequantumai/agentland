from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_agent_did_history_response_200_rotations_item_statement_new_pub import GetAgentDidHistoryResponse200RotationsItemStatementNewPub
  from ..models.get_agent_did_history_response_200_rotations_item_statement_old_pub import GetAgentDidHistoryResponse200RotationsItemStatementOldPub





T = TypeVar("T", bound="GetAgentDidHistoryResponse200RotationsItemStatement")



@_attrs_define
class GetAgentDidHistoryResponse200RotationsItemStatement:
    """ 
        Attributes:
            old_pub (GetAgentDidHistoryResponse200RotationsItemStatementOldPub):
            new_pub (GetAgentDidHistoryResponse200RotationsItemStatementNewPub):
            reason (str):
            timestamp (str):
     """

    old_pub: GetAgentDidHistoryResponse200RotationsItemStatementOldPub
    new_pub: GetAgentDidHistoryResponse200RotationsItemStatementNewPub
    reason: str
    timestamp: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_did_history_response_200_rotations_item_statement_new_pub import GetAgentDidHistoryResponse200RotationsItemStatementNewPub # noqa: PLC0415
        from ..models.get_agent_did_history_response_200_rotations_item_statement_old_pub import GetAgentDidHistoryResponse200RotationsItemStatementOldPub # noqa: PLC0415
        old_pub = self.old_pub.to_dict()

        new_pub = self.new_pub.to_dict()

        reason = self.reason

        timestamp = self.timestamp


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "old_pub": old_pub,
            "new_pub": new_pub,
            "reason": reason,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_did_history_response_200_rotations_item_statement_new_pub import GetAgentDidHistoryResponse200RotationsItemStatementNewPub # noqa: PLC0415
        from ..models.get_agent_did_history_response_200_rotations_item_statement_old_pub import GetAgentDidHistoryResponse200RotationsItemStatementOldPub # noqa: PLC0415
        d = dict(src_dict)
        old_pub = GetAgentDidHistoryResponse200RotationsItemStatementOldPub.from_dict(d.pop("old_pub"))




        new_pub = GetAgentDidHistoryResponse200RotationsItemStatementNewPub.from_dict(d.pop("new_pub"))




        reason = d.pop("reason")

        timestamp = d.pop("timestamp")

        get_agent_did_history_response_200_rotations_item_statement = cls(
            old_pub=old_pub,
            new_pub=new_pub,
            reason=reason,
            timestamp=timestamp,
        )

        return get_agent_did_history_response_200_rotations_item_statement

