from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.cancel_key_challenge_response_200_kind import CancelKeyChallengeResponse200Kind
from ..models.cancel_key_challenge_response_200_status import CancelKeyChallengeResponse200Status
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="CancelKeyChallengeResponse200")



@_attrs_define
class CancelKeyChallengeResponse200:
    """ 
        Attributes:
            id (UUID):
            agent_id (UUID):
            key_id (UUID):
            kind (CancelKeyChallengeResponse200Kind):
            status (CancelKeyChallengeResponse200Status):
            created_at (str):
            expires_at (str):
            resolved_at (None | str):
     """

    id: UUID
    agent_id: UUID
    key_id: UUID
    kind: CancelKeyChallengeResponse200Kind
    status: CancelKeyChallengeResponse200Status
    created_at: str
    expires_at: str
    resolved_at: None | str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        agent_id = str(self.agent_id)

        key_id = str(self.key_id)

        kind = self.kind.value

        status = self.status.value

        created_at = self.created_at

        expires_at = self.expires_at

        resolved_at: None | str
        resolved_at = self.resolved_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "agent_id": agent_id,
            "key_id": key_id,
            "kind": kind,
            "status": status,
            "created_at": created_at,
            "expires_at": expires_at,
            "resolved_at": resolved_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        agent_id = UUID(d.pop("agent_id"))




        key_id = UUID(d.pop("key_id"))




        kind = CancelKeyChallengeResponse200Kind(d.pop("kind"))




        status = CancelKeyChallengeResponse200Status(d.pop("status"))




        created_at = d.pop("created_at")

        expires_at = d.pop("expires_at")

        def _parse_resolved_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at"))


        cancel_key_challenge_response_200 = cls(
            id=id,
            agent_id=agent_id,
            key_id=key_id,
            kind=kind,
            status=status,
            created_at=created_at,
            expires_at=expires_at,
            resolved_at=resolved_at,
        )

        return cancel_key_challenge_response_200

