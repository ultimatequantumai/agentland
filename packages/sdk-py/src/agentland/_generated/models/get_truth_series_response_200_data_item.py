from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_truth_series_response_200_data_item_outcome import GetTruthSeriesResponse200DataItemOutcome
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_truth_series_response_200_data_item_question import GetTruthSeriesResponse200DataItemQuestion





T = TypeVar("T", bound="GetTruthSeriesResponse200DataItem")



@_attrs_define
class GetTruthSeriesResponse200DataItem:
    """ 
        Attributes:
            question (GetTruthSeriesResponse200DataItemQuestion):
            outcome (GetTruthSeriesResponse200DataItemOutcome):
            resolution_known_at (str):
            resolved_at (str):
            source (str):
            resolution_source_url (str):
            source_market_url (None | str):
            audit_root (datetime.date | None):
            attribution (str):
     """

    question: GetTruthSeriesResponse200DataItemQuestion
    outcome: GetTruthSeriesResponse200DataItemOutcome
    resolution_known_at: str
    resolved_at: str
    source: str
    resolution_source_url: str
    source_market_url: None | str
    audit_root: datetime.date | None
    attribution: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_truth_series_response_200_data_item_question import GetTruthSeriesResponse200DataItemQuestion # noqa: PLC0415
        question = self.question.to_dict()

        outcome = self.outcome.value

        resolution_known_at = self.resolution_known_at

        resolved_at = self.resolved_at

        source = self.source

        resolution_source_url = self.resolution_source_url

        source_market_url: None | str
        source_market_url = self.source_market_url

        audit_root: None | str
        if isinstance(self.audit_root, datetime.date):
            audit_root = self.audit_root.isoformat()
        else:
            audit_root = self.audit_root

        attribution = self.attribution


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "question": question,
            "outcome": outcome,
            "resolution_known_at": resolution_known_at,
            "resolved_at": resolved_at,
            "source": source,
            "resolution_source_url": resolution_source_url,
            "source_market_url": source_market_url,
            "audit_root": audit_root,
            "attribution": attribution,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_truth_series_response_200_data_item_question import GetTruthSeriesResponse200DataItemQuestion # noqa: PLC0415
        d = dict(src_dict)
        question = GetTruthSeriesResponse200DataItemQuestion.from_dict(d.pop("question"))




        outcome = GetTruthSeriesResponse200DataItemOutcome(d.pop("outcome"))




        resolution_known_at = d.pop("resolution_known_at")

        resolved_at = d.pop("resolved_at")

        source = d.pop("source")

        resolution_source_url = d.pop("resolution_source_url")

        def _parse_source_market_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_market_url = _parse_source_market_url(d.pop("source_market_url"))


        def _parse_audit_root(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                audit_root_type_0 = datetime.date.fromisoformat(data)



                return audit_root_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        audit_root = _parse_audit_root(d.pop("audit_root"))


        attribution = d.pop("attribution")

        get_truth_series_response_200_data_item = cls(
            question=question,
            outcome=outcome,
            resolution_known_at=resolution_known_at,
            resolved_at=resolved_at,
            source=source,
            resolution_source_url=resolution_source_url,
            source_market_url=source_market_url,
            audit_root=audit_root,
            attribution=attribution,
        )

        return get_truth_series_response_200_data_item

