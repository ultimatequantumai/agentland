from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetAgentTrustResponse200HistoryItem")



@_attrs_define
class GetAgentTrustResponse200HistoryItem:
    """ 
        Attributes:
            score (float):
            version (str):
            computed_at (str):
     """

    score: float
    version: str
    computed_at: str





    def to_dict(self) -> dict[str, Any]:
        score = self.score

        version = self.version

        computed_at = self.computed_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "score": score,
            "version": version,
            "computed_at": computed_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        score = d.pop("score")

        version = d.pop("version")

        computed_at = d.pop("computed_at")

        get_agent_trust_response_200_history_item = cls(
            score=score,
            version=version,
            computed_at=computed_at,
        )

        return get_agent_trust_response_200_history_item

