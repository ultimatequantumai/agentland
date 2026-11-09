from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="GetAgentDidHistoryResponse200RecoveryNoticeType0")



@_attrs_define
class GetAgentDidHistoryResponse200RecoveryNoticeType0:
    """ 
        Attributes:
            id (UUID):
            started_at (str):
            completes_at (str):
     """

    id: UUID
    started_at: str
    completes_at: str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        started_at = self.started_at

        completes_at = self.completes_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "started_at": started_at,
            "completes_at": completes_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        started_at = d.pop("started_at")

        completes_at = d.pop("completes_at")

        get_agent_did_history_response_200_recovery_notice_type_0 = cls(
            id=id,
            started_at=started_at,
            completes_at=completes_at,
        )

        return get_agent_did_history_response_200_recovery_notice_type_0

