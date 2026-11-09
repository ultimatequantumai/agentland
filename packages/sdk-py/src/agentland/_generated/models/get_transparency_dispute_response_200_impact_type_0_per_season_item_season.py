from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_transparency_dispute_response_200_impact_type_0_per_season_item_season_status import GetTransparencyDisputeResponse200ImpactType0PerSeasonItemSeasonStatus
from uuid import UUID






T = TypeVar("T", bound="GetTransparencyDisputeResponse200ImpactType0PerSeasonItemSeason")



@_attrs_define
class GetTransparencyDisputeResponse200ImpactType0PerSeasonItemSeason:
    """ 
        Attributes:
            id (UUID):
            number (int):
            name (str):
            is_sandbox (bool):
            status (GetTransparencyDisputeResponse200ImpactType0PerSeasonItemSeasonStatus):
     """

    id: UUID
    number: int
    name: str
    is_sandbox: bool
    status: GetTransparencyDisputeResponse200ImpactType0PerSeasonItemSeasonStatus





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        number = self.number

        name = self.name

        is_sandbox = self.is_sandbox

        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "number": number,
            "name": name,
            "is_sandbox": is_sandbox,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        number = d.pop("number")

        name = d.pop("name")

        is_sandbox = d.pop("is_sandbox")

        status = GetTransparencyDisputeResponse200ImpactType0PerSeasonItemSeasonStatus(d.pop("status"))




        get_transparency_dispute_response_200_impact_type_0_per_season_item_season = cls(
            id=id,
            number=number,
            name=name,
            is_sandbox=is_sandbox,
            status=status,
        )

        return get_transparency_dispute_response_200_impact_type_0_per_season_item_season

