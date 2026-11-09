from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime






T = TypeVar("T", bound="ListTransparencySourcesResponse200DataItemDaysItem")



@_attrs_define
class ListTransparencySourcesResponse200DataItemDaysItem:
    """ 
        Attributes:
            date (datetime.date):
            attempts (int):
            ok (int):
            errors (int):
     """

    date: datetime.date
    attempts: int
    ok: int
    errors: int





    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        attempts = self.attempts

        ok = self.ok

        errors = self.errors


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "date": date,
            "attempts": attempts,
            "ok": ok,
            "errors": errors,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))




        attempts = d.pop("attempts")

        ok = d.pop("ok")

        errors = d.pop("errors")

        list_transparency_sources_response_200_data_item_days_item = cls(
            date=date,
            attempts=attempts,
            ok=ok,
            errors=errors,
        )

        return list_transparency_sources_response_200_data_item_days_item

