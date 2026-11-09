from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="ListAgentLiftEvidenceResponse200SeasonsItem")



@_attrs_define
class ListAgentLiftEvidenceResponse200SeasonsItem:
    """ 
        Attributes:
            id (UUID):
            number (int):
            name (str):
            is_sandbox (bool):
     """

    id: UUID
    number: int
    name: str
    is_sandbox: bool





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        number = self.number

        name = self.name

        is_sandbox = self.is_sandbox


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "number": number,
            "name": name,
            "is_sandbox": is_sandbox,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        number = d.pop("number")

        name = d.pop("name")

        is_sandbox = d.pop("is_sandbox")

        list_agent_lift_evidence_response_200_seasons_item = cls(
            id=id,
            number=number,
            name=name,
            is_sandbox=is_sandbox,
        )

        return list_agent_lift_evidence_response_200_seasons_item

