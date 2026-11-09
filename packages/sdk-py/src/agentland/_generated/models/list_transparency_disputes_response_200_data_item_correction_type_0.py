from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_transparency_disputes_response_200_data_item_correction_type_0_outcome_type import ListTransparencyDisputesResponse200DataItemCorrectionType0OutcomeType
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ListTransparencyDisputesResponse200DataItemCorrectionType0")



@_attrs_define
class ListTransparencyDisputesResponse200DataItemCorrectionType0:
    """ 
        Attributes:
            resolution_id (UUID):
            revision (int):
            outcome_type (ListTransparencyDisputesResponse200DataItemCorrectionType0OutcomeType):
            outcome_key (None | str):
            outcome_label (None | str):
            value (None | str):
            unit (None | str):
     """

    resolution_id: UUID
    revision: int
    outcome_type: ListTransparencyDisputesResponse200DataItemCorrectionType0OutcomeType
    outcome_key: None | str
    outcome_label: None | str
    value: None | str
    unit: None | str





    def to_dict(self) -> dict[str, Any]:
        resolution_id = str(self.resolution_id)

        revision = self.revision

        outcome_type = self.outcome_type.value

        outcome_key: None | str
        outcome_key = self.outcome_key

        outcome_label: None | str
        outcome_label = self.outcome_label

        value: None | str
        value = self.value

        unit: None | str
        unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "resolution_id": resolution_id,
            "revision": revision,
            "outcome_type": outcome_type,
            "outcome_key": outcome_key,
            "outcome_label": outcome_label,
            "value": value,
            "unit": unit,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resolution_id = UUID(d.pop("resolution_id"))




        revision = d.pop("revision")

        outcome_type = ListTransparencyDisputesResponse200DataItemCorrectionType0OutcomeType(d.pop("outcome_type"))




        def _parse_outcome_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        outcome_key = _parse_outcome_key(d.pop("outcome_key"))


        def _parse_outcome_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        outcome_label = _parse_outcome_label(d.pop("outcome_label"))


        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))


        def _parse_unit(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        unit = _parse_unit(d.pop("unit"))


        list_transparency_disputes_response_200_data_item_correction_type_0 = cls(
            resolution_id=resolution_id,
            revision=revision,
            outcome_type=outcome_type,
            outcome_key=outcome_key,
            outcome_label=outcome_label,
            value=value,
            unit=unit,
        )

        return list_transparency_disputes_response_200_data_item_correction_type_0

