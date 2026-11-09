from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ask_truth_response_200_data_item_type_0_outcome import AskTruthResponse200DataItemType0Outcome
from ..models.ask_truth_response_200_data_item_type_0_status import AskTruthResponse200DataItemType0Status
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.ask_truth_response_200_data_item_type_0_question import AskTruthResponse200DataItemType0Question





T = TypeVar("T", bound="AskTruthResponse200DataItemType0")



@_attrs_define
class AskTruthResponse200DataItemType0:
    """ 
        Attributes:
            question (AskTruthResponse200DataItemType0Question):
            outcome (AskTruthResponse200DataItemType0Outcome):
            resolution_known_at (str):
            resolved_at (str):
            source (str):
            resolution_source_url (str):
            source_market_url (None | str):
            audit_root (datetime.date | None):
            attribution (str):
            status (AskTruthResponse200DataItemType0Status):
     """

    question: AskTruthResponse200DataItemType0Question
    outcome: AskTruthResponse200DataItemType0Outcome
    resolution_known_at: str
    resolved_at: str
    source: str
    resolution_source_url: str
    source_market_url: None | str
    audit_root: datetime.date | None
    attribution: str
    status: AskTruthResponse200DataItemType0Status





    def to_dict(self) -> dict[str, Any]:
        from ..models.ask_truth_response_200_data_item_type_0_question import AskTruthResponse200DataItemType0Question # noqa: PLC0415
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

        status = self.status.value


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
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ask_truth_response_200_data_item_type_0_question import AskTruthResponse200DataItemType0Question # noqa: PLC0415
        d = dict(src_dict)
        question = AskTruthResponse200DataItemType0Question.from_dict(d.pop("question"))




        outcome = AskTruthResponse200DataItemType0Outcome(d.pop("outcome"))




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

        status = AskTruthResponse200DataItemType0Status(d.pop("status"))




        ask_truth_response_200_data_item_type_0 = cls(
            question=question,
            outcome=outcome,
            resolution_known_at=resolution_known_at,
            resolved_at=resolved_at,
            source=source,
            resolution_source_url=resolution_source_url,
            source_market_url=source_market_url,
            audit_root=audit_root,
            attribution=attribution,
            status=status,
        )

        return ask_truth_response_200_data_item_type_0

