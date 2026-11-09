from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetChallengeResponse200RecordsItemDailyRootType0")



@_attrs_define
class GetChallengeResponse200RecordsItemDailyRootType0:
    """ 
        Attributes:
            date (str):
            root (str):
     """

    date: str
    root: str





    def to_dict(self) -> dict[str, Any]:
        date = self.date

        root = self.root


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "date": date,
            "root": root,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        root = d.pop("root")

        get_challenge_response_200_records_item_daily_root_type_0 = cls(
            date=date,
            root=root,
        )

        return get_challenge_response_200_records_item_daily_root_type_0

