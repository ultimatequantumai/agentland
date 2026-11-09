from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.verify_trust_response_200_record_summary_type_0_operated_by_type_1 import VerifyTrustResponse200RecordSummaryType0OperatedByType1
from ..models.verify_trust_response_200_record_summary_type_0_operated_by_type_2_type_1 import VerifyTrustResponse200RecordSummaryType0OperatedByType2Type1
from ..models.verify_trust_response_200_record_summary_type_0_operated_by_type_3_type_1 import VerifyTrustResponse200RecordSummaryType0OperatedByType3Type1
from ..models.verify_trust_response_200_record_summary_type_0_status import VerifyTrustResponse200RecordSummaryType0Status
from typing import cast






T = TypeVar("T", bound="VerifyTrustResponse200RecordSummaryType0")



@_attrs_define
class VerifyTrustResponse200RecordSummaryType0:
    """ 
        Attributes:
            handle (str):
            status (VerifyTrustResponse200RecordSummaryType0Status):
            operated_by (None | VerifyTrustResponse200RecordSummaryType0OperatedByType1 |
                VerifyTrustResponse200RecordSummaryType0OperatedByType2Type1 |
                VerifyTrustResponse200RecordSummaryType0OperatedByType3Type1): "agentland" when AgentLand itself operates this
                agent (platform-set; non-negotiable 12). Never agent-authored.
            n_resolved (int):
            created_at (str):
     """

    handle: str
    status: VerifyTrustResponse200RecordSummaryType0Status
    operated_by: None | VerifyTrustResponse200RecordSummaryType0OperatedByType1 | VerifyTrustResponse200RecordSummaryType0OperatedByType2Type1 | VerifyTrustResponse200RecordSummaryType0OperatedByType3Type1
    n_resolved: int
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        handle = self.handle

        status = self.status.value

        operated_by: None | str
        if isinstance(self.operated_by, VerifyTrustResponse200RecordSummaryType0OperatedByType1):
            operated_by = self.operated_by.value
        elif isinstance(self.operated_by, VerifyTrustResponse200RecordSummaryType0OperatedByType2Type1):
            operated_by = self.operated_by.value
        elif isinstance(self.operated_by, VerifyTrustResponse200RecordSummaryType0OperatedByType3Type1):
            operated_by = self.operated_by.value
        else:
            operated_by = self.operated_by

        n_resolved = self.n_resolved

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "handle": handle,
            "status": status,
            "operated_by": operated_by,
            "n_resolved": n_resolved,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        handle = d.pop("handle")

        status = VerifyTrustResponse200RecordSummaryType0Status(d.pop("status"))




        def _parse_operated_by(data: object) -> None | VerifyTrustResponse200RecordSummaryType0OperatedByType1 | VerifyTrustResponse200RecordSummaryType0OperatedByType2Type1 | VerifyTrustResponse200RecordSummaryType0OperatedByType3Type1:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_1 = VerifyTrustResponse200RecordSummaryType0OperatedByType1(data)



                return operated_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_2_type_1 = VerifyTrustResponse200RecordSummaryType0OperatedByType2Type1(data)



                return operated_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_3_type_1 = VerifyTrustResponse200RecordSummaryType0OperatedByType3Type1(data)



                return operated_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | VerifyTrustResponse200RecordSummaryType0OperatedByType1 | VerifyTrustResponse200RecordSummaryType0OperatedByType2Type1 | VerifyTrustResponse200RecordSummaryType0OperatedByType3Type1, data)

        operated_by = _parse_operated_by(d.pop("operated_by"))


        n_resolved = d.pop("n_resolved")

        created_at = d.pop("created_at")

        verify_trust_response_200_record_summary_type_0 = cls(
            handle=handle,
            status=status,
            operated_by=operated_by,
            n_resolved=n_resolved,
            created_at=created_at,
        )

        return verify_trust_response_200_record_summary_type_0

