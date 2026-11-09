from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.initiate_transfer_response_201_status import InitiateTransferResponse201Status
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="InitiateTransferResponse201")



@_attrs_define
class InitiateTransferResponse201:
    """ 
        Attributes:
            id (UUID):
            agent_id (UUID):
            from_operator_id (UUID):
            to_operator_id (UUID):
            status (InitiateTransferResponse201Status):
            created_at (str):
            expires_at (str):
            accepted_at (None | str):
     """

    id: UUID
    agent_id: UUID
    from_operator_id: UUID
    to_operator_id: UUID
    status: InitiateTransferResponse201Status
    created_at: str
    expires_at: str
    accepted_at: None | str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        agent_id = str(self.agent_id)

        from_operator_id = str(self.from_operator_id)

        to_operator_id = str(self.to_operator_id)

        status = self.status.value

        created_at = self.created_at

        expires_at = self.expires_at

        accepted_at: None | str
        accepted_at = self.accepted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "agent_id": agent_id,
            "from_operator_id": from_operator_id,
            "to_operator_id": to_operator_id,
            "status": status,
            "created_at": created_at,
            "expires_at": expires_at,
            "accepted_at": accepted_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        agent_id = UUID(d.pop("agent_id"))




        from_operator_id = UUID(d.pop("from_operator_id"))




        to_operator_id = UUID(d.pop("to_operator_id"))




        status = InitiateTransferResponse201Status(d.pop("status"))




        created_at = d.pop("created_at")

        expires_at = d.pop("expires_at")

        def _parse_accepted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        accepted_at = _parse_accepted_at(d.pop("accepted_at"))


        initiate_transfer_response_201 = cls(
            id=id,
            agent_id=agent_id,
            from_operator_id=from_operator_id,
            to_operator_id=to_operator_id,
            status=status,
            created_at=created_at,
            expires_at=expires_at,
            accepted_at=accepted_at,
        )

        return initiate_transfer_response_201

