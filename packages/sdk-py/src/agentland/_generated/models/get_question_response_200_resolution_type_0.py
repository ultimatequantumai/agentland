from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_question_response_200_resolution_type_0_outcome_type import GetQuestionResponse200ResolutionType0OutcomeType
from ..models.get_question_response_200_resolution_type_0_resolved_by import GetQuestionResponse200ResolutionType0ResolvedBy
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GetQuestionResponse200ResolutionType0")



@_attrs_define
class GetQuestionResponse200ResolutionType0:
    """ 
        Attributes:
            id (UUID):
            revision (int):
            outcome_key (None | str):
            value (None | str):
            resolution_known_at (str):
            resolved_at (str):
            resolved_by (GetQuestionResponse200ResolutionType0ResolvedBy):
            notes (str):
            dispute_id (None | UUID):
            outcome_type (GetQuestionResponse200ResolutionType0OutcomeType):
            outcome_label (None | str):
            unit (None | str):
     """

    id: UUID
    revision: int
    outcome_key: None | str
    value: None | str
    resolution_known_at: str
    resolved_at: str
    resolved_by: GetQuestionResponse200ResolutionType0ResolvedBy
    notes: str
    dispute_id: None | UUID
    outcome_type: GetQuestionResponse200ResolutionType0OutcomeType
    outcome_label: None | str
    unit: None | str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        revision = self.revision

        outcome_key: None | str
        outcome_key = self.outcome_key

        value: None | str
        value = self.value

        resolution_known_at = self.resolution_known_at

        resolved_at = self.resolved_at

        resolved_by = self.resolved_by.value

        notes = self.notes

        dispute_id: None | str
        if isinstance(self.dispute_id, UUID):
            dispute_id = str(self.dispute_id)
        else:
            dispute_id = self.dispute_id

        outcome_type = self.outcome_type.value

        outcome_label: None | str
        outcome_label = self.outcome_label

        unit: None | str
        unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "revision": revision,
            "outcome_key": outcome_key,
            "value": value,
            "resolution_known_at": resolution_known_at,
            "resolved_at": resolved_at,
            "resolved_by": resolved_by,
            "notes": notes,
            "dispute_id": dispute_id,
            "outcome_type": outcome_type,
            "outcome_label": outcome_label,
            "unit": unit,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        revision = d.pop("revision")

        def _parse_outcome_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        outcome_key = _parse_outcome_key(d.pop("outcome_key"))


        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))


        resolution_known_at = d.pop("resolution_known_at")

        resolved_at = d.pop("resolved_at")

        resolved_by = GetQuestionResponse200ResolutionType0ResolvedBy(d.pop("resolved_by"))




        notes = d.pop("notes")

        def _parse_dispute_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dispute_id_type_0 = UUID(data)



                return dispute_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        dispute_id = _parse_dispute_id(d.pop("dispute_id"))


        outcome_type = GetQuestionResponse200ResolutionType0OutcomeType(d.pop("outcome_type"))




        def _parse_outcome_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        outcome_label = _parse_outcome_label(d.pop("outcome_label"))


        def _parse_unit(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        unit = _parse_unit(d.pop("unit"))


        get_question_response_200_resolution_type_0 = cls(
            id=id,
            revision=revision,
            outcome_key=outcome_key,
            value=value,
            resolution_known_at=resolution_known_at,
            resolved_at=resolved_at,
            resolved_by=resolved_by,
            notes=notes,
            dispute_id=dispute_id,
            outcome_type=outcome_type,
            outcome_label=outcome_label,
            unit=unit,
        )

        return get_question_response_200_resolution_type_0

