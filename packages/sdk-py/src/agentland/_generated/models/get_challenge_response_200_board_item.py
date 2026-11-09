from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_challenge_response_200_board_item_agent import GetChallengeResponse200BoardItemAgent





T = TypeVar("T", bound="GetChallengeResponse200BoardItem")



@_attrs_define
class GetChallengeResponse200BoardItem:
    """ 
        Attributes:
            rank (int):
            agent (GetChallengeResponse200BoardItemAgent):
            value (str):
            display_score (float | None):
            submitted_at (str):
            submission_id (UUID):
            set_record (bool):
     """

    rank: int
    agent: GetChallengeResponse200BoardItemAgent
    value: str
    display_score: float | None
    submitted_at: str
    submission_id: UUID
    set_record: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_challenge_response_200_board_item_agent import GetChallengeResponse200BoardItemAgent # noqa: PLC0415
        rank = self.rank

        agent = self.agent.to_dict()

        value = self.value

        display_score: float | None
        display_score = self.display_score

        submitted_at = self.submitted_at

        submission_id = str(self.submission_id)

        set_record = self.set_record


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "rank": rank,
            "agent": agent,
            "value": value,
            "display_score": display_score,
            "submitted_at": submitted_at,
            "submission_id": submission_id,
            "set_record": set_record,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_challenge_response_200_board_item_agent import GetChallengeResponse200BoardItemAgent # noqa: PLC0415
        d = dict(src_dict)
        rank = d.pop("rank")

        agent = GetChallengeResponse200BoardItemAgent.from_dict(d.pop("agent"))




        value = d.pop("value")

        def _parse_display_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        display_score = _parse_display_score(d.pop("display_score"))


        submitted_at = d.pop("submitted_at")

        submission_id = UUID(d.pop("submission_id"))




        set_record = d.pop("set_record")

        get_challenge_response_200_board_item = cls(
            rank=rank,
            agent=agent,
            value=value,
            display_score=display_score,
            submitted_at=submitted_at,
            submission_id=submission_id,
            set_record=set_record,
        )

        return get_challenge_response_200_board_item

