from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.cancel_recovery_by_operator_response_200_status import CancelRecoveryByOperatorResponse200Status
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.cancel_recovery_by_operator_response_200_new_public_key import CancelRecoveryByOperatorResponse200NewPublicKey





T = TypeVar("T", bound="CancelRecoveryByOperatorResponse200")



@_attrs_define
class CancelRecoveryByOperatorResponse200:
    """ 
        Attributes:
            id (UUID):
            agent_id (UUID):
            status (CancelRecoveryByOperatorResponse200Status):
            new_public_key (CancelRecoveryByOperatorResponse200NewPublicKey):
            created_at (str):
            completes_at (str):
     """

    id: UUID
    agent_id: UUID
    status: CancelRecoveryByOperatorResponse200Status
    new_public_key: CancelRecoveryByOperatorResponse200NewPublicKey
    created_at: str
    completes_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.cancel_recovery_by_operator_response_200_new_public_key import CancelRecoveryByOperatorResponse200NewPublicKey # noqa: PLC0415
        id = str(self.id)

        agent_id = str(self.agent_id)

        status = self.status.value

        new_public_key = self.new_public_key.to_dict()

        created_at = self.created_at

        completes_at = self.completes_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "agent_id": agent_id,
            "status": status,
            "new_public_key": new_public_key,
            "created_at": created_at,
            "completes_at": completes_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cancel_recovery_by_operator_response_200_new_public_key import CancelRecoveryByOperatorResponse200NewPublicKey # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        agent_id = UUID(d.pop("agent_id"))




        status = CancelRecoveryByOperatorResponse200Status(d.pop("status"))




        new_public_key = CancelRecoveryByOperatorResponse200NewPublicKey.from_dict(d.pop("new_public_key"))




        created_at = d.pop("created_at")

        completes_at = d.pop("completes_at")

        cancel_recovery_by_operator_response_200 = cls(
            id=id,
            agent_id=agent_id,
            status=status,
            new_public_key=new_public_key,
            created_at=created_at,
            completes_at=completes_at,
        )

        return cancel_recovery_by_operator_response_200

