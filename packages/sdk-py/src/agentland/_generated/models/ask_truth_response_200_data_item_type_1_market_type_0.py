from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AskTruthResponse200DataItemType1MarketType0")



@_attrs_define
class AskTruthResponse200DataItemType1MarketType0:
    """ 
        Attributes:
            p (float):
            taken_at (str):
     """

    p: float
    taken_at: str





    def to_dict(self) -> dict[str, Any]:
        p = self.p

        taken_at = self.taken_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "p": p,
            "taken_at": taken_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        p = d.pop("p")

        taken_at = d.pop("taken_at")

        ask_truth_response_200_data_item_type_1_market_type_0 = cls(
            p=p,
            taken_at=taken_at,
        )

        return ask_truth_response_200_data_item_type_1_market_type_0

