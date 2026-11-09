from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PutMailPreferencesBody")



@_attrs_define
class PutMailPreferencesBody:
    """ 
        Attributes:
            season_notes (bool):
            report_card (bool):
            inactivity_nudge (bool):
            season_summary (bool):
     """

    season_notes: bool
    report_card: bool
    inactivity_nudge: bool
    season_summary: bool





    def to_dict(self) -> dict[str, Any]:
        season_notes = self.season_notes

        report_card = self.report_card

        inactivity_nudge = self.inactivity_nudge

        season_summary = self.season_summary


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "season_notes": season_notes,
            "report_card": report_card,
            "inactivity_nudge": inactivity_nudge,
            "season_summary": season_summary,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        season_notes = d.pop("season_notes")

        report_card = d.pop("report_card")

        inactivity_nudge = d.pop("inactivity_nudge")

        season_summary = d.pop("season_summary")

        put_mail_preferences_body = cls(
            season_notes=season_notes,
            report_card=report_card,
            inactivity_nudge=inactivity_nudge,
            season_summary=season_summary,
        )

        return put_mail_preferences_body

