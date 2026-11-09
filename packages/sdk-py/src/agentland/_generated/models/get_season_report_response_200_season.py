from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetSeasonReportResponse200Season")



@_attrs_define
class GetSeasonReportResponse200Season:
    """ 
        Attributes:
            number (int):
            name (str):
            starts_at (str):
            ends_at (str):
     """

    number: int
    name: str
    starts_at: str
    ends_at: str





    def to_dict(self) -> dict[str, Any]:
        number = self.number

        name = self.name

        starts_at = self.starts_at

        ends_at = self.ends_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "number": number,
            "name": name,
            "starts_at": starts_at,
            "ends_at": ends_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number = d.pop("number")

        name = d.pop("name")

        starts_at = d.pop("starts_at")

        ends_at = d.pop("ends_at")

        get_season_report_response_200_season = cls(
            number=number,
            name=name,
            starts_at=starts_at,
            ends_at=ends_at,
        )

        return get_season_report_response_200_season

