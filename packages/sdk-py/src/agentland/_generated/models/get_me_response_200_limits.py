from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetMeResponse200Limits")



@_attrs_define
class GetMeResponse200Limits:
    """ 
        Attributes:
            vault_entries (None | str):
            vault_bytes (None | str):
            forecasts_per_day (int | None):
            outbound_mail (bool):
            sealed_eligible (bool):
            semantic_search_eligible (bool):
            consult_respondent_eligible (bool):
            record_submissions_per_day (int | None):
     """

    vault_entries: None | str
    vault_bytes: None | str
    forecasts_per_day: int | None
    outbound_mail: bool
    sealed_eligible: bool
    semantic_search_eligible: bool
    consult_respondent_eligible: bool
    record_submissions_per_day: int | None





    def to_dict(self) -> dict[str, Any]:
        vault_entries: None | str
        vault_entries = self.vault_entries

        vault_bytes: None | str
        vault_bytes = self.vault_bytes

        forecasts_per_day: int | None
        forecasts_per_day = self.forecasts_per_day

        outbound_mail = self.outbound_mail

        sealed_eligible = self.sealed_eligible

        semantic_search_eligible = self.semantic_search_eligible

        consult_respondent_eligible = self.consult_respondent_eligible

        record_submissions_per_day: int | None
        record_submissions_per_day = self.record_submissions_per_day


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "vault_entries": vault_entries,
            "vault_bytes": vault_bytes,
            "forecasts_per_day": forecasts_per_day,
            "outbound_mail": outbound_mail,
            "sealed_eligible": sealed_eligible,
            "semantic_search_eligible": semantic_search_eligible,
            "consult_respondent_eligible": consult_respondent_eligible,
            "record_submissions_per_day": record_submissions_per_day,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_vault_entries(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        vault_entries = _parse_vault_entries(d.pop("vault_entries"))


        def _parse_vault_bytes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        vault_bytes = _parse_vault_bytes(d.pop("vault_bytes"))


        def _parse_forecasts_per_day(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        forecasts_per_day = _parse_forecasts_per_day(d.pop("forecasts_per_day"))


        outbound_mail = d.pop("outbound_mail")

        sealed_eligible = d.pop("sealed_eligible")

        semantic_search_eligible = d.pop("semantic_search_eligible")

        consult_respondent_eligible = d.pop("consult_respondent_eligible")

        def _parse_record_submissions_per_day(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        record_submissions_per_day = _parse_record_submissions_per_day(d.pop("record_submissions_per_day"))


        get_me_response_200_limits = cls(
            vault_entries=vault_entries,
            vault_bytes=vault_bytes,
            forecasts_per_day=forecasts_per_day,
            outbound_mail=outbound_mail,
            sealed_eligible=sealed_eligible,
            semantic_search_eligible=semantic_search_eligible,
            consult_respondent_eligible=consult_respondent_eligible,
            record_submissions_per_day=record_submissions_per_day,
        )

        return get_me_response_200_limits

