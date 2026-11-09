from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetStatsResponse200CurrentSeasonsItem")



@_attrs_define
class GetStatsResponse200CurrentSeasonsItem:
    """ 
        Attributes:
            number (int):
            name (str):
            is_sandbox (bool):
     """

    number: int
    name: str
    is_sandbox: bool





    def to_dict(self) -> dict[str, Any]:
        number = self.number

        name = self.name

        is_sandbox = self.is_sandbox


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "number": number,
            "name": name,
            "is_sandbox": is_sandbox,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number = d.pop("number")

        name = d.pop("name")

        is_sandbox = d.pop("is_sandbox")

        get_stats_response_200_current_seasons_item = cls(
            number=number,
            name=name,
            is_sandbox=is_sandbox,
        )

        return get_stats_response_200_current_seasons_item

