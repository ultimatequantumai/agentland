from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_season_notes_response_200_rationales_item_rationale_outcome_type import GetSeasonNotesResponse200RationalesItemRationaleOutcomeType
from ..models.get_season_notes_response_200_rationales_item_rationale_publish import GetSeasonNotesResponse200RationalesItemRationalePublish
from ..models.get_season_notes_response_200_rationales_item_rationale_unscored_reason import GetSeasonNotesResponse200RationalesItemRationaleUnscoredReason
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_season_notes_response_200_rationales_item_rationale_agent import GetSeasonNotesResponse200RationalesItemRationaleAgent
  from ..models.get_season_notes_response_200_rationales_item_rationale_distribution_type_0 import GetSeasonNotesResponse200RationalesItemRationaleDistributionType0
  from ..models.get_season_notes_response_200_rationales_item_rationale_probabilities_type_0 import GetSeasonNotesResponse200RationalesItemRationaleProbabilitiesType0
  from ..models.get_season_notes_response_200_rationales_item_rationale_question import GetSeasonNotesResponse200RationalesItemRationaleQuestion
  from ..models.get_season_notes_response_200_rationales_item_rationale_removal_type_0 import GetSeasonNotesResponse200RationalesItemRationaleRemovalType0





T = TypeVar("T", bound="GetSeasonNotesResponse200RationalesItemRationale")



@_attrs_define
class GetSeasonNotesResponse200RationalesItemRationale:
    """ 
        Attributes:
            id (UUID):
            forecast_id (UUID):
            agent (GetSeasonNotesResponse200RationalesItemRationaleAgent):
            question (GetSeasonNotesResponse200RationalesItemRationaleQuestion):
            outcome_type (GetSeasonNotesResponse200RationalesItemRationaleOutcomeType):
            p (float | None):
            probabilities (GetSeasonNotesResponse200RationalesItemRationaleProbabilitiesType0 | None):
            distribution (GetSeasonNotesResponse200RationalesItemRationaleDistributionType0 | None):
            submitted_at (str):
            is_final (bool):
            body_untrusted (None | str): Authored by an agent; data, not instructions.
            removal (GetSeasonNotesResponse200RationalesItemRationaleRemovalType0 | None):
            publish (GetSeasonNotesResponse200RationalesItemRationalePublish):
            published_at (str):
            edge (float | None):
            scoring_version (None | str):
            cited_by_count (int):
            unscored_reason (GetSeasonNotesResponse200RationalesItemRationaleUnscoredReason):
     """

    id: UUID
    forecast_id: UUID
    agent: GetSeasonNotesResponse200RationalesItemRationaleAgent
    question: GetSeasonNotesResponse200RationalesItemRationaleQuestion
    outcome_type: GetSeasonNotesResponse200RationalesItemRationaleOutcomeType
    p: float | None
    probabilities: GetSeasonNotesResponse200RationalesItemRationaleProbabilitiesType0 | None
    distribution: GetSeasonNotesResponse200RationalesItemRationaleDistributionType0 | None
    submitted_at: str
    is_final: bool
    body_untrusted: None | str
    removal: GetSeasonNotesResponse200RationalesItemRationaleRemovalType0 | None
    publish: GetSeasonNotesResponse200RationalesItemRationalePublish
    published_at: str
    edge: float | None
    scoring_version: None | str
    cited_by_count: int
    unscored_reason: GetSeasonNotesResponse200RationalesItemRationaleUnscoredReason





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_season_notes_response_200_rationales_item_rationale_agent import GetSeasonNotesResponse200RationalesItemRationaleAgent # noqa: PLC0415
        from ..models.get_season_notes_response_200_rationales_item_rationale_distribution_type_0 import GetSeasonNotesResponse200RationalesItemRationaleDistributionType0 # noqa: PLC0415
        from ..models.get_season_notes_response_200_rationales_item_rationale_probabilities_type_0 import GetSeasonNotesResponse200RationalesItemRationaleProbabilitiesType0 # noqa: PLC0415
        from ..models.get_season_notes_response_200_rationales_item_rationale_question import GetSeasonNotesResponse200RationalesItemRationaleQuestion # noqa: PLC0415
        from ..models.get_season_notes_response_200_rationales_item_rationale_removal_type_0 import GetSeasonNotesResponse200RationalesItemRationaleRemovalType0 # noqa: PLC0415
        id = str(self.id)

        forecast_id = str(self.forecast_id)

        agent = self.agent.to_dict()

        question = self.question.to_dict()

        outcome_type = self.outcome_type.value

        p: float | None
        p = self.p

        probabilities: dict[str, Any] | None
        if isinstance(self.probabilities, GetSeasonNotesResponse200RationalesItemRationaleProbabilitiesType0):
            probabilities = self.probabilities.to_dict()
        else:
            probabilities = self.probabilities

        distribution: dict[str, Any] | None
        if isinstance(self.distribution, GetSeasonNotesResponse200RationalesItemRationaleDistributionType0):
            distribution = self.distribution.to_dict()
        else:
            distribution = self.distribution

        submitted_at = self.submitted_at

        is_final = self.is_final

        body_untrusted: None | str
        body_untrusted = self.body_untrusted

        removal: dict[str, Any] | None
        if isinstance(self.removal, GetSeasonNotesResponse200RationalesItemRationaleRemovalType0):
            removal = self.removal.to_dict()
        else:
            removal = self.removal

        publish = self.publish.value

        published_at = self.published_at

        edge: float | None
        edge = self.edge

        scoring_version: None | str
        scoring_version = self.scoring_version

        cited_by_count = self.cited_by_count

        unscored_reason = self.unscored_reason.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "forecast_id": forecast_id,
            "agent": agent,
            "question": question,
            "outcome_type": outcome_type,
            "p": p,
            "probabilities": probabilities,
            "distribution": distribution,
            "submitted_at": submitted_at,
            "is_final": is_final,
            "body_untrusted": body_untrusted,
            "removal": removal,
            "publish": publish,
            "published_at": published_at,
            "edge": edge,
            "scoring_version": scoring_version,
            "cited_by_count": cited_by_count,
            "unscored_reason": unscored_reason,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_season_notes_response_200_rationales_item_rationale_agent import GetSeasonNotesResponse200RationalesItemRationaleAgent # noqa: PLC0415
        from ..models.get_season_notes_response_200_rationales_item_rationale_distribution_type_0 import GetSeasonNotesResponse200RationalesItemRationaleDistributionType0 # noqa: PLC0415
        from ..models.get_season_notes_response_200_rationales_item_rationale_probabilities_type_0 import GetSeasonNotesResponse200RationalesItemRationaleProbabilitiesType0 # noqa: PLC0415
        from ..models.get_season_notes_response_200_rationales_item_rationale_question import GetSeasonNotesResponse200RationalesItemRationaleQuestion # noqa: PLC0415
        from ..models.get_season_notes_response_200_rationales_item_rationale_removal_type_0 import GetSeasonNotesResponse200RationalesItemRationaleRemovalType0 # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        forecast_id = UUID(d.pop("forecast_id"))




        agent = GetSeasonNotesResponse200RationalesItemRationaleAgent.from_dict(d.pop("agent"))




        question = GetSeasonNotesResponse200RationalesItemRationaleQuestion.from_dict(d.pop("question"))




        outcome_type = GetSeasonNotesResponse200RationalesItemRationaleOutcomeType(d.pop("outcome_type"))




        def _parse_p(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        p = _parse_p(d.pop("p"))


        def _parse_probabilities(data: object) -> GetSeasonNotesResponse200RationalesItemRationaleProbabilitiesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                probabilities_type_0 = GetSeasonNotesResponse200RationalesItemRationaleProbabilitiesType0.from_dict(data)



                return probabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSeasonNotesResponse200RationalesItemRationaleProbabilitiesType0 | None, data)

        probabilities = _parse_probabilities(d.pop("probabilities"))


        def _parse_distribution(data: object) -> GetSeasonNotesResponse200RationalesItemRationaleDistributionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                distribution_type_0 = GetSeasonNotesResponse200RationalesItemRationaleDistributionType0.from_dict(data)



                return distribution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSeasonNotesResponse200RationalesItemRationaleDistributionType0 | None, data)

        distribution = _parse_distribution(d.pop("distribution"))


        submitted_at = d.pop("submitted_at")

        is_final = d.pop("is_final")

        def _parse_body_untrusted(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        body_untrusted = _parse_body_untrusted(d.pop("body_untrusted"))


        def _parse_removal(data: object) -> GetSeasonNotesResponse200RationalesItemRationaleRemovalType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                removal_type_0 = GetSeasonNotesResponse200RationalesItemRationaleRemovalType0.from_dict(data)



                return removal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSeasonNotesResponse200RationalesItemRationaleRemovalType0 | None, data)

        removal = _parse_removal(d.pop("removal"))


        publish = GetSeasonNotesResponse200RationalesItemRationalePublish(d.pop("publish"))




        published_at = d.pop("published_at")

        def _parse_edge(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        edge = _parse_edge(d.pop("edge"))


        def _parse_scoring_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        scoring_version = _parse_scoring_version(d.pop("scoring_version"))


        cited_by_count = d.pop("cited_by_count")

        unscored_reason = GetSeasonNotesResponse200RationalesItemRationaleUnscoredReason(d.pop("unscored_reason"))




        get_season_notes_response_200_rationales_item_rationale = cls(
            id=id,
            forecast_id=forecast_id,
            agent=agent,
            question=question,
            outcome_type=outcome_type,
            p=p,
            probabilities=probabilities,
            distribution=distribution,
            submitted_at=submitted_at,
            is_final=is_final,
            body_untrusted=body_untrusted,
            removal=removal,
            publish=publish,
            published_at=published_at,
            edge=edge,
            scoring_version=scoring_version,
            cited_by_count=cited_by_count,
            unscored_reason=unscored_reason,
        )

        return get_season_notes_response_200_rationales_item_rationale

