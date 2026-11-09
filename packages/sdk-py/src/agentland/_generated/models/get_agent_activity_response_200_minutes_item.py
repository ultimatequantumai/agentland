from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetAgentActivityResponse200MinutesItem")



@_attrs_define
class GetAgentActivityResponse200MinutesItem:
    """ 
        Attributes:
            t (str):
            calls (int):
            errors (int):
     """

    t: str
    calls: int
    errors: int





    def to_dict(self) -> dict[str, Any]:
        t = self.t

        calls = self.calls

        errors = self.errors


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "t": t,
            "calls": calls,
            "errors": errors,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        t = d.pop("t")

        calls = d.pop("calls")

        errors = d.pop("errors")

        get_agent_activity_response_200_minutes_item = cls(
            t=t,
            calls=calls,
            errors=errors,
        )

        return get_agent_activity_response_200_minutes_item

