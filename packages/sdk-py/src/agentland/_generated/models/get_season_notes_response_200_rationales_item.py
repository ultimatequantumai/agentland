from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_season_notes_response_200_rationales_item_rationale import GetSeasonNotesResponse200RationalesItemRationale





T = TypeVar("T", bound="GetSeasonNotesResponse200RationalesItem")



@_attrs_define
class GetSeasonNotesResponse200RationalesItem:
    """ 
        Attributes:
            scope_label (str):
            rationale (GetSeasonNotesResponse200RationalesItemRationale):
     """

    scope_label: str
    rationale: GetSeasonNotesResponse200RationalesItemRationale





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_season_notes_response_200_rationales_item_rationale import GetSeasonNotesResponse200RationalesItemRationale # noqa: PLC0415
        scope_label = self.scope_label

        rationale = self.rationale.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "scope_label": scope_label,
            "rationale": rationale,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_season_notes_response_200_rationales_item_rationale import GetSeasonNotesResponse200RationalesItemRationale # noqa: PLC0415
        d = dict(src_dict)
        scope_label = d.pop("scope_label")

        rationale = GetSeasonNotesResponse200RationalesItemRationale.from_dict(d.pop("rationale"))




        get_season_notes_response_200_rationales_item = cls(
            scope_label=scope_label,
            rationale=rationale,
        )

        return get_season_notes_response_200_rationales_item

