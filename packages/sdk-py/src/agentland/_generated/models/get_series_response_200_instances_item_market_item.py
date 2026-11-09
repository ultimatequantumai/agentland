from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetSeriesResponse200InstancesItemMarketItem")



@_attrs_define
class GetSeriesResponse200InstancesItemMarketItem:
    """ 
        Attributes:
            t (str):
            p (float):
     """

    t: str
    p: float





    def to_dict(self) -> dict[str, Any]:
        t = self.t

        p = self.p


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "t": t,
            "p": p,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        t = d.pop("t")

        p = d.pop("p")

        get_series_response_200_instances_item_market_item = cls(
            t=t,
            p=p,
        )

        return get_series_response_200_instances_item_market_item

