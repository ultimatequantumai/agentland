from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetDailyResponse200SeriesItem")



@_attrs_define
class GetDailyResponse200SeriesItem:
    """ 
        Attributes:
            key (str):
            title (str):
            resolved_count (int):
     """

    key: str
    title: str
    resolved_count: int





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        title = self.title

        resolved_count = self.resolved_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
            "title": title,
            "resolved_count": resolved_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        title = d.pop("title")

        resolved_count = d.pop("resolved_count")

        get_daily_response_200_series_item = cls(
            key=key,
            title=title,
            resolved_count=resolved_count,
        )

        return get_daily_response_200_series_item

