from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_operator_credits_response_200_data_item_reason import ListOperatorCreditsResponse200DataItemReason
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.list_operator_credits_response_200_data_item_agent_type_0 import ListOperatorCreditsResponse200DataItemAgentType0
  from ..models.list_operator_credits_response_200_data_item_challenge_type_0 import ListOperatorCreditsResponse200DataItemChallengeType0
  from ..models.list_operator_credits_response_200_data_item_submission_type_0 import ListOperatorCreditsResponse200DataItemSubmissionType0





T = TypeVar("T", bound="ListOperatorCreditsResponse200DataItem")



@_attrs_define
class ListOperatorCreditsResponse200DataItem:
    """ 
        Attributes:
            id (UUID):
            created_at (str):
            delta (int):
            reason (ListOperatorCreditsResponse200DataItemReason):
            balance_after (int):
            agent (ListOperatorCreditsResponse200DataItemAgentType0 | None):
            challenge (ListOperatorCreditsResponse200DataItemChallengeType0 | None):
            submission (ListOperatorCreditsResponse200DataItemSubmissionType0 | None):
     """

    id: UUID
    created_at: str
    delta: int
    reason: ListOperatorCreditsResponse200DataItemReason
    balance_after: int
    agent: ListOperatorCreditsResponse200DataItemAgentType0 | None
    challenge: ListOperatorCreditsResponse200DataItemChallengeType0 | None
    submission: ListOperatorCreditsResponse200DataItemSubmissionType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_operator_credits_response_200_data_item_agent_type_0 import ListOperatorCreditsResponse200DataItemAgentType0 # noqa: PLC0415
        from ..models.list_operator_credits_response_200_data_item_challenge_type_0 import ListOperatorCreditsResponse200DataItemChallengeType0 # noqa: PLC0415
        from ..models.list_operator_credits_response_200_data_item_submission_type_0 import ListOperatorCreditsResponse200DataItemSubmissionType0 # noqa: PLC0415
        id = str(self.id)

        created_at = self.created_at

        delta = self.delta

        reason = self.reason.value

        balance_after = self.balance_after

        agent: dict[str, Any] | None
        if isinstance(self.agent, ListOperatorCreditsResponse200DataItemAgentType0):
            agent = self.agent.to_dict()
        else:
            agent = self.agent

        challenge: dict[str, Any] | None
        if isinstance(self.challenge, ListOperatorCreditsResponse200DataItemChallengeType0):
            challenge = self.challenge.to_dict()
        else:
            challenge = self.challenge

        submission: dict[str, Any] | None
        if isinstance(self.submission, ListOperatorCreditsResponse200DataItemSubmissionType0):
            submission = self.submission.to_dict()
        else:
            submission = self.submission


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "created_at": created_at,
            "delta": delta,
            "reason": reason,
            "balance_after": balance_after,
            "agent": agent,
            "challenge": challenge,
            "submission": submission,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_operator_credits_response_200_data_item_agent_type_0 import ListOperatorCreditsResponse200DataItemAgentType0 # noqa: PLC0415
        from ..models.list_operator_credits_response_200_data_item_challenge_type_0 import ListOperatorCreditsResponse200DataItemChallengeType0 # noqa: PLC0415
        from ..models.list_operator_credits_response_200_data_item_submission_type_0 import ListOperatorCreditsResponse200DataItemSubmissionType0 # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        created_at = d.pop("created_at")

        delta = d.pop("delta")

        reason = ListOperatorCreditsResponse200DataItemReason(d.pop("reason"))




        balance_after = d.pop("balance_after")

        def _parse_agent(data: object) -> ListOperatorCreditsResponse200DataItemAgentType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                agent_type_0 = ListOperatorCreditsResponse200DataItemAgentType0.from_dict(data)



                return agent_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListOperatorCreditsResponse200DataItemAgentType0 | None, data)

        agent = _parse_agent(d.pop("agent"))


        def _parse_challenge(data: object) -> ListOperatorCreditsResponse200DataItemChallengeType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                challenge_type_0 = ListOperatorCreditsResponse200DataItemChallengeType0.from_dict(data)



                return challenge_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListOperatorCreditsResponse200DataItemChallengeType0 | None, data)

        challenge = _parse_challenge(d.pop("challenge"))


        def _parse_submission(data: object) -> ListOperatorCreditsResponse200DataItemSubmissionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                submission_type_0 = ListOperatorCreditsResponse200DataItemSubmissionType0.from_dict(data)



                return submission_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListOperatorCreditsResponse200DataItemSubmissionType0 | None, data)

        submission = _parse_submission(d.pop("submission"))


        list_operator_credits_response_200_data_item = cls(
            id=id,
            created_at=created_at,
            delta=delta,
            reason=reason,
            balance_after=balance_after,
            agent=agent,
            challenge=challenge,
            submission=submission,
        )

        return list_operator_credits_response_200_data_item

