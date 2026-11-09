from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_agent_response_201_scout_type_0_status import CreateAgentResponse201ScoutType0Status






T = TypeVar("T", bound="CreateAgentResponse201ScoutType0")



@_attrs_define
class CreateAgentResponse201ScoutType0:
    """ 
        Attributes:
            handle (str):
            status (CreateAgentResponse201ScoutType0Status):
     """

    handle: str
    status: CreateAgentResponse201ScoutType0Status





    def to_dict(self) -> dict[str, Any]:
        handle = self.handle

        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "handle": handle,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        handle = d.pop("handle")

        status = CreateAgentResponse201ScoutType0Status(d.pop("status"))




        create_agent_response_201_scout_type_0 = cls(
            handle=handle,
            status=status,
        )

        return create_agent_response_201_scout_type_0

