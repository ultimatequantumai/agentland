from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="ListOperatorCreditsResponse200DataItemAgentType0")



@_attrs_define
class ListOperatorCreditsResponse200DataItemAgentType0:
    """ 
        Attributes:
            id (UUID):
            handle (str):
     """

    id: UUID
    handle: str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        handle = self.handle


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "handle": handle,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        handle = d.pop("handle")

        list_operator_credits_response_200_data_item_agent_type_0 = cls(
            id=id,
            handle=handle,
        )

        return list_operator_credits_response_200_data_item_agent_type_0

