from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_operator_agent_response_200_pending_key_challenges_item_kind import GetOperatorAgentResponse200PendingKeyChallengesItemKind
from uuid import UUID






T = TypeVar("T", bound="GetOperatorAgentResponse200PendingKeyChallengesItem")



@_attrs_define
class GetOperatorAgentResponse200PendingKeyChallengesItem:
    """ 
        Attributes:
            id (UUID):
            kid (str):
            kind (GetOperatorAgentResponse200PendingKeyChallengesItemKind):
            created_at (str):
            expires_at (str):
     """

    id: UUID
    kid: str
    kind: GetOperatorAgentResponse200PendingKeyChallengesItemKind
    created_at: str
    expires_at: str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        kid = self.kid

        kind = self.kind.value

        created_at = self.created_at

        expires_at = self.expires_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "kid": kid,
            "kind": kind,
            "created_at": created_at,
            "expires_at": expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        kid = d.pop("kid")

        kind = GetOperatorAgentResponse200PendingKeyChallengesItemKind(d.pop("kind"))




        created_at = d.pop("created_at")

        expires_at = d.pop("expires_at")

        get_operator_agent_response_200_pending_key_challenges_item = cls(
            id=id,
            kid=kid,
            kind=kind,
            created_at=created_at,
            expires_at=expires_at,
        )

        return get_operator_agent_response_200_pending_key_challenges_item

