from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="GetMeResponse200SeasonType0")



@_attrs_define
class GetMeResponse200SeasonType0:
    """ 
        Attributes:
            id (UUID):
            number (int):
            name (str):
            ends_at (str):
     """

    id: UUID
    number: int
    name: str
    ends_at: str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        number = self.number

        name = self.name

        ends_at = self.ends_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "number": number,
            "name": name,
            "ends_at": ends_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        number = d.pop("number")

        name = d.pop("name")

        ends_at = d.pop("ends_at")

        get_me_response_200_season_type_0 = cls(
            id=id,
            number=number,
            name=name,
            ends_at=ends_at,
        )

        return get_me_response_200_season_type_0

