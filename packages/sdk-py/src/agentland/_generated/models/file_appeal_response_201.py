from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="FileAppealResponse201")



@_attrs_define
class FileAppealResponse201:
    """ 
        Attributes:
            id (UUID):
            action_id (UUID):
            filed_at (str):
            due_at (str):
     """

    id: UUID
    action_id: UUID
    filed_at: str
    due_at: str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        action_id = str(self.action_id)

        filed_at = self.filed_at

        due_at = self.due_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "action_id": action_id,
            "filed_at": filed_at,
            "due_at": due_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        action_id = UUID(d.pop("action_id"))




        filed_at = d.pop("filed_at")

        due_at = d.pop("due_at")

        file_appeal_response_201 = cls(
            id=id,
            action_id=action_id,
            filed_at=filed_at,
            due_at=due_at,
        )

        return file_appeal_response_201

