from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_latest_digest_response_200_issue_type_0_records_item_agent import GetLatestDigestResponse200IssueType0RecordsItemAgent
  from ..models.get_latest_digest_response_200_issue_type_0_records_item_challenge import GetLatestDigestResponse200IssueType0RecordsItemChallenge





T = TypeVar("T", bound="GetLatestDigestResponse200IssueType0RecordsItem")



@_attrs_define
class GetLatestDigestResponse200IssueType0RecordsItem:
    """ 
        Attributes:
            record_id (UUID):
            challenge (GetLatestDigestResponse200IssueType0RecordsItemChallenge):
            agent (GetLatestDigestResponse200IssueType0RecordsItemAgent):
            previous_value (str):
            new_value (str):
            display_score (float | None):
            set_at (str):
     """

    record_id: UUID
    challenge: GetLatestDigestResponse200IssueType0RecordsItemChallenge
    agent: GetLatestDigestResponse200IssueType0RecordsItemAgent
    previous_value: str
    new_value: str
    display_score: float | None
    set_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_latest_digest_response_200_issue_type_0_records_item_agent import GetLatestDigestResponse200IssueType0RecordsItemAgent # noqa: PLC0415
        from ..models.get_latest_digest_response_200_issue_type_0_records_item_challenge import GetLatestDigestResponse200IssueType0RecordsItemChallenge # noqa: PLC0415
        record_id = str(self.record_id)

        challenge = self.challenge.to_dict()

        agent = self.agent.to_dict()

        previous_value = self.previous_value

        new_value = self.new_value

        display_score: float | None
        display_score = self.display_score

        set_at = self.set_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "record_id": record_id,
            "challenge": challenge,
            "agent": agent,
            "previous_value": previous_value,
            "new_value": new_value,
            "display_score": display_score,
            "set_at": set_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_latest_digest_response_200_issue_type_0_records_item_agent import GetLatestDigestResponse200IssueType0RecordsItemAgent # noqa: PLC0415
        from ..models.get_latest_digest_response_200_issue_type_0_records_item_challenge import GetLatestDigestResponse200IssueType0RecordsItemChallenge # noqa: PLC0415
        d = dict(src_dict)
        record_id = UUID(d.pop("record_id"))




        challenge = GetLatestDigestResponse200IssueType0RecordsItemChallenge.from_dict(d.pop("challenge"))




        agent = GetLatestDigestResponse200IssueType0RecordsItemAgent.from_dict(d.pop("agent"))




        previous_value = d.pop("previous_value")

        new_value = d.pop("new_value")

        def _parse_display_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        display_score = _parse_display_score(d.pop("display_score"))


        set_at = d.pop("set_at")

        get_latest_digest_response_200_issue_type_0_records_item = cls(
            record_id=record_id,
            challenge=challenge,
            agent=agent,
            previous_value=previous_value,
            new_value=new_value,
            display_score=display_score,
            set_at=set_at,
        )

        return get_latest_digest_response_200_issue_type_0_records_item

