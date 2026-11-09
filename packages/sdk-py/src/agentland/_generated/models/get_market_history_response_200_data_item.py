from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetMarketHistoryResponse200DataItem")



@_attrs_define
class GetMarketHistoryResponse200DataItem:
    """ 
        Attributes:
            taken_at (str):
            p_yes (float):
     """

    taken_at: str
    p_yes: float





    def to_dict(self) -> dict[str, Any]:
        taken_at = self.taken_at

        p_yes = self.p_yes


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "taken_at": taken_at,
            "p_yes": p_yes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        taken_at = d.pop("taken_at")

        p_yes = d.pop("p_yes")

        get_market_history_response_200_data_item = cls(
            taken_at=taken_at,
            p_yes=p_yes,
        )

        return get_market_history_response_200_data_item

