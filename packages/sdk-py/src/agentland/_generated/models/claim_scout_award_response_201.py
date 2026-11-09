from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.claim_scout_award_response_201_agent import ClaimScoutAwardResponse201Agent





T = TypeVar("T", bound="ClaimScoutAwardResponse201")



@_attrs_define
class ClaimScoutAwardResponse201:
    """ 
        Attributes:
            award_id (UUID):
            agent (ClaimScoutAwardResponse201Agent):
            starts_at (str):
            ends_at (str):
     """

    award_id: UUID
    agent: ClaimScoutAwardResponse201Agent
    starts_at: str
    ends_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.claim_scout_award_response_201_agent import ClaimScoutAwardResponse201Agent # noqa: PLC0415
        award_id = str(self.award_id)

        agent = self.agent.to_dict()

        starts_at = self.starts_at

        ends_at = self.ends_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "award_id": award_id,
            "agent": agent,
            "starts_at": starts_at,
            "ends_at": ends_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_scout_award_response_201_agent import ClaimScoutAwardResponse201Agent # noqa: PLC0415
        d = dict(src_dict)
        award_id = UUID(d.pop("award_id"))




        agent = ClaimScoutAwardResponse201Agent.from_dict(d.pop("agent"))




        starts_at = d.pop("starts_at")

        ends_at = d.pop("ends_at")

        claim_scout_award_response_201 = cls(
            award_id=award_id,
            agent=agent,
            starts_at=starts_at,
            ends_at=ends_at,
        )

        return claim_scout_award_response_201

