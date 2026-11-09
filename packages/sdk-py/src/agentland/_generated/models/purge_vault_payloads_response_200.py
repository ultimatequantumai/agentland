from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID






T = TypeVar("T", bound="PurgeVaultPayloadsResponse200")



@_attrs_define
class PurgeVaultPayloadsResponse200:
    """ 
        Attributes:
            agent_id (UUID):
            purged_seqs (list[str]):
     """

    agent_id: UUID
    purged_seqs: list[str]





    def to_dict(self) -> dict[str, Any]:
        agent_id = str(self.agent_id)

        purged_seqs = self.purged_seqs




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "agent_id": agent_id,
            "purged_seqs": purged_seqs,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_id = UUID(d.pop("agent_id"))




        purged_seqs = cast(list[str], d.pop("purged_seqs"))


        purge_vault_payloads_response_200 = cls(
            agent_id=agent_id,
            purged_seqs=purged_seqs,
        )

        return purge_vault_payloads_response_200

