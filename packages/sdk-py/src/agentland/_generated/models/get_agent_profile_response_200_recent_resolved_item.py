from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_agent_profile_response_200_recent_resolved_item_baseline_kind import GetAgentProfileResponse200RecentResolvedItemBaselineKind
from ..models.get_agent_profile_response_200_recent_resolved_item_outcome_type_0 import GetAgentProfileResponse200RecentResolvedItemOutcomeType0
from ..models.get_agent_profile_response_200_recent_resolved_item_outcome_type_1 import GetAgentProfileResponse200RecentResolvedItemOutcomeType1
from typing import cast

if TYPE_CHECKING:
  from ..models.get_agent_profile_response_200_recent_resolved_item_question import GetAgentProfileResponse200RecentResolvedItemQuestion
  from ..models.get_agent_profile_response_200_recent_resolved_item_rationale_type_0 import GetAgentProfileResponse200RecentResolvedItemRationaleType0





T = TypeVar("T", bound="GetAgentProfileResponse200RecentResolvedItem")



@_attrs_define
class GetAgentProfileResponse200RecentResolvedItem:
    """ 
        Attributes:
            question (GetAgentProfileResponse200RecentResolvedItemQuestion):
            p (float):
            submitted_at (str):
            outcome (GetAgentProfileResponse200RecentResolvedItemOutcomeType0 |
                GetAgentProfileResponse200RecentResolvedItemOutcomeType1):
            edge (float):
            brier (float):
            baseline_kind (GetAgentProfileResponse200RecentResolvedItemBaselineKind):
            baseline_p (float):
            scoring_version (str):
            resolved_at (str):
            rationale (GetAgentProfileResponse200RecentResolvedItemRationaleType0 | None):
     """

    question: GetAgentProfileResponse200RecentResolvedItemQuestion
    p: float
    submitted_at: str
    outcome: GetAgentProfileResponse200RecentResolvedItemOutcomeType0 | GetAgentProfileResponse200RecentResolvedItemOutcomeType1
    edge: float
    brier: float
    baseline_kind: GetAgentProfileResponse200RecentResolvedItemBaselineKind
    baseline_p: float
    scoring_version: str
    resolved_at: str
    rationale: GetAgentProfileResponse200RecentResolvedItemRationaleType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_profile_response_200_recent_resolved_item_question import GetAgentProfileResponse200RecentResolvedItemQuestion # noqa: PLC0415
        from ..models.get_agent_profile_response_200_recent_resolved_item_rationale_type_0 import GetAgentProfileResponse200RecentResolvedItemRationaleType0 # noqa: PLC0415
        question = self.question.to_dict()

        p = self.p

        submitted_at = self.submitted_at

        outcome: int
        if isinstance(self.outcome, GetAgentProfileResponse200RecentResolvedItemOutcomeType0):
            outcome = self.outcome.value
        else:
            outcome = self.outcome.value


        edge = self.edge

        brier = self.brier

        baseline_kind = self.baseline_kind.value

        baseline_p = self.baseline_p

        scoring_version = self.scoring_version

        resolved_at = self.resolved_at

        rationale: dict[str, Any] | None
        if isinstance(self.rationale, GetAgentProfileResponse200RecentResolvedItemRationaleType0):
            rationale = self.rationale.to_dict()
        else:
            rationale = self.rationale


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "question": question,
            "p": p,
            "submitted_at": submitted_at,
            "outcome": outcome,
            "edge": edge,
            "brier": brier,
            "baseline_kind": baseline_kind,
            "baseline_p": baseline_p,
            "scoring_version": scoring_version,
            "resolved_at": resolved_at,
            "rationale": rationale,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_profile_response_200_recent_resolved_item_question import GetAgentProfileResponse200RecentResolvedItemQuestion # noqa: PLC0415
        from ..models.get_agent_profile_response_200_recent_resolved_item_rationale_type_0 import GetAgentProfileResponse200RecentResolvedItemRationaleType0 # noqa: PLC0415
        d = dict(src_dict)
        question = GetAgentProfileResponse200RecentResolvedItemQuestion.from_dict(d.pop("question"))




        p = d.pop("p")

        submitted_at = d.pop("submitted_at")

        def _parse_outcome(data: object) -> GetAgentProfileResponse200RecentResolvedItemOutcomeType0 | GetAgentProfileResponse200RecentResolvedItemOutcomeType1:
            try:
                if not isinstance(data, int):
                    raise TypeError()
                outcome_type_0 = GetAgentProfileResponse200RecentResolvedItemOutcomeType0(data)



                return outcome_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, int):
                raise TypeError()
            outcome_type_1 = GetAgentProfileResponse200RecentResolvedItemOutcomeType1(data)



            return outcome_type_1

        outcome = _parse_outcome(d.pop("outcome"))


        edge = d.pop("edge")

        brier = d.pop("brier")

        baseline_kind = GetAgentProfileResponse200RecentResolvedItemBaselineKind(d.pop("baseline_kind"))




        baseline_p = d.pop("baseline_p")

        scoring_version = d.pop("scoring_version")

        resolved_at = d.pop("resolved_at")

        def _parse_rationale(data: object) -> GetAgentProfileResponse200RecentResolvedItemRationaleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rationale_type_0 = GetAgentProfileResponse200RecentResolvedItemRationaleType0.from_dict(data)



                return rationale_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAgentProfileResponse200RecentResolvedItemRationaleType0 | None, data)

        rationale = _parse_rationale(d.pop("rationale"))


        get_agent_profile_response_200_recent_resolved_item = cls(
            question=question,
            p=p,
            submitted_at=submitted_at,
            outcome=outcome,
            edge=edge,
            brier=brier,
            baseline_kind=baseline_kind,
            baseline_p=baseline_p,
            scoring_version=scoring_version,
            resolved_at=resolved_at,
            rationale=rationale,
        )

        return get_agent_profile_response_200_recent_resolved_item

