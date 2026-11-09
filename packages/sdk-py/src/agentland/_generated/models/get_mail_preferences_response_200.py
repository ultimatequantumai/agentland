from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetMailPreferencesResponse200")



@_attrs_define
class GetMailPreferencesResponse200:
    """ 
        Attributes:
            season_notes (bool):
            report_card (bool):
            inactivity_nudge (bool):
            season_summary (bool):
            can_edit (bool):
     """

    season_notes: bool
    report_card: bool
    inactivity_nudge: bool
    season_summary: bool
    can_edit: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        season_notes = self.season_notes

        report_card = self.report_card

        inactivity_nudge = self.inactivity_nudge

        season_summary = self.season_summary

        can_edit = self.can_edit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "season_notes": season_notes,
            "report_card": report_card,
            "inactivity_nudge": inactivity_nudge,
            "season_summary": season_summary,
            "can_edit": can_edit,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        season_notes = d.pop("season_notes")

        report_card = d.pop("report_card")

        inactivity_nudge = d.pop("inactivity_nudge")

        season_summary = d.pop("season_summary")

        can_edit = d.pop("can_edit")

        get_mail_preferences_response_200 = cls(
            season_notes=season_notes,
            report_card=report_card,
            inactivity_nudge=inactivity_nudge,
            season_summary=season_summary,
            can_edit=can_edit,
        )


        get_mail_preferences_response_200.additional_properties = d
        return get_mail_preferences_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
