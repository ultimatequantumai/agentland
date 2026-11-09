from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ListAgentLiftEvidenceResponse200SummaryType0")



@_attrs_define
class ListAgentLiftEvidenceResponse200SummaryType0:
    """ 
        Attributes:
            lift (float):
            citations_received (int):
            shrunk_lift (float):
     """

    lift: float
    citations_received: int
    shrunk_lift: float





    def to_dict(self) -> dict[str, Any]:
        lift = self.lift

        citations_received = self.citations_received

        shrunk_lift = self.shrunk_lift


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "lift": lift,
            "citations_received": citations_received,
            "shrunk_lift": shrunk_lift,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lift = d.pop("lift")

        citations_received = d.pop("citations_received")

        shrunk_lift = d.pop("shrunk_lift")

        list_agent_lift_evidence_response_200_summary_type_0 = cls(
            lift=lift,
            citations_received=citations_received,
            shrunk_lift=shrunk_lift,
        )

        return list_agent_lift_evidence_response_200_summary_type_0

