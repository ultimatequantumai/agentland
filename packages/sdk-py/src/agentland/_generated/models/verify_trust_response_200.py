from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.verify_trust_response_200_record_summary_type_0 import VerifyTrustResponse200RecordSummaryType0





T = TypeVar("T", bound="VerifyTrustResponse200")



@_attrs_define
class VerifyTrustResponse200:
    """ 
        Attributes:
            valid (bool):
            trust (float | None):
            record_summary (None | VerifyTrustResponse200RecordSummaryType0):
     """

    valid: bool
    trust: float | None
    record_summary: None | VerifyTrustResponse200RecordSummaryType0





    def to_dict(self) -> dict[str, Any]:
        from ..models.verify_trust_response_200_record_summary_type_0 import VerifyTrustResponse200RecordSummaryType0 # noqa: PLC0415
        valid = self.valid

        trust: float | None
        trust = self.trust

        record_summary: dict[str, Any] | None
        if isinstance(self.record_summary, VerifyTrustResponse200RecordSummaryType0):
            record_summary = self.record_summary.to_dict()
        else:
            record_summary = self.record_summary


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "valid": valid,
            "trust": trust,
            "record_summary": record_summary,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.verify_trust_response_200_record_summary_type_0 import VerifyTrustResponse200RecordSummaryType0 # noqa: PLC0415
        d = dict(src_dict)
        valid = d.pop("valid")

        def _parse_trust(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        trust = _parse_trust(d.pop("trust"))


        def _parse_record_summary(data: object) -> None | VerifyTrustResponse200RecordSummaryType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                record_summary_type_0 = VerifyTrustResponse200RecordSummaryType0.from_dict(data)



                return record_summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | VerifyTrustResponse200RecordSummaryType0, data)

        record_summary = _parse_record_summary(d.pop("record_summary"))


        verify_trust_response_200 = cls(
            valid=valid,
            trust=trust,
            record_summary=record_summary,
        )

        return verify_trust_response_200

