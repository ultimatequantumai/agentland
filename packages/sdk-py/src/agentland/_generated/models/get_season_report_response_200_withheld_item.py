from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetSeasonReportResponse200WithheldItem")



@_attrs_define
class GetSeasonReportResponse200WithheldItem:
    """ 
        Attributes:
            source (str):
            reason (str):
     """

    source: str
    reason: str





    def to_dict(self) -> dict[str, Any]:
        source = self.source

        reason = self.reason


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "source": source,
            "reason": reason,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        reason = d.pop("reason")

        get_season_report_response_200_withheld_item = cls(
            source=source,
            reason=reason,
        )

        return get_season_report_response_200_withheld_item

