from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.start_recovery_response_201_status import StartRecoveryResponse201Status
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.start_recovery_response_201_new_public_key import StartRecoveryResponse201NewPublicKey





T = TypeVar("T", bound="StartRecoveryResponse201")



@_attrs_define
class StartRecoveryResponse201:
    """ 
        Attributes:
            id (UUID):
            agent_id (UUID):
            status (StartRecoveryResponse201Status):
            new_public_key (StartRecoveryResponse201NewPublicKey):
            created_at (str):
            completes_at (str):
     """

    id: UUID
    agent_id: UUID
    status: StartRecoveryResponse201Status
    new_public_key: StartRecoveryResponse201NewPublicKey
    created_at: str
    completes_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.start_recovery_response_201_new_public_key import StartRecoveryResponse201NewPublicKey # noqa: PLC0415
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
        from ..models.start_recovery_response_201_new_public_key import StartRecoveryResponse201NewPublicKey # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        agent_id = UUID(d.pop("agent_id"))




        status = StartRecoveryResponse201Status(d.pop("status"))




        new_public_key = StartRecoveryResponse201NewPublicKey.from_dict(d.pop("new_public_key"))




        created_at = d.pop("created_at")

        completes_at = d.pop("completes_at")

        start_recovery_response_201 = cls(
            id=id,
            agent_id=agent_id,
            status=status,
            new_public_key=new_public_key,
            created_at=created_at,
            completes_at=completes_at,
        )

        return start_recovery_response_201

