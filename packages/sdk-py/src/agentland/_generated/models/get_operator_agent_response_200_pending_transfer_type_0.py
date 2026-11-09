from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_operator_agent_response_200_pending_transfer_type_0_status import GetOperatorAgentResponse200PendingTransferType0Status
from uuid import UUID






T = TypeVar("T", bound="GetOperatorAgentResponse200PendingTransferType0")



@_attrs_define
class GetOperatorAgentResponse200PendingTransferType0:
    """ 
        Attributes:
            id (UUID):
            status (GetOperatorAgentResponse200PendingTransferType0Status):
            created_at (str):
            expires_at (str):
     """

    id: UUID
    status: GetOperatorAgentResponse200PendingTransferType0Status
    created_at: str
    expires_at: str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        status = self.status.value

        created_at = self.created_at

        expires_at = self.expires_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "status": status,
            "created_at": created_at,
            "expires_at": expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        status = GetOperatorAgentResponse200PendingTransferType0Status(d.pop("status"))




        created_at = d.pop("created_at")

        expires_at = d.pop("expires_at")

        get_operator_agent_response_200_pending_transfer_type_0 = cls(
            id=id,
            status=status,
            created_at=created_at,
            expires_at=expires_at,
        )

        return get_operator_agent_response_200_pending_transfer_type_0

