from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_commons_rationale_response_200_outcome_type import GetCommonsRationaleResponse200OutcomeType
from ..models.get_commons_rationale_response_200_publish import GetCommonsRationaleResponse200Publish
from ..models.get_commons_rationale_response_200_unscored_reason import GetCommonsRationaleResponse200UnscoredReason
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_commons_rationale_response_200_agent import GetCommonsRationaleResponse200Agent
  from ..models.get_commons_rationale_response_200_cites_item import GetCommonsRationaleResponse200CitesItem
  from ..models.get_commons_rationale_response_200_distribution_type_0 import GetCommonsRationaleResponse200DistributionType0
  from ..models.get_commons_rationale_response_200_probabilities_type_0 import GetCommonsRationaleResponse200ProbabilitiesType0
  from ..models.get_commons_rationale_response_200_question import GetCommonsRationaleResponse200Question
  from ..models.get_commons_rationale_response_200_removal_type_0 import GetCommonsRationaleResponse200RemovalType0





T = TypeVar("T", bound="GetCommonsRationaleResponse200")



@_attrs_define
class GetCommonsRationaleResponse200:
    """ 
        Attributes:
            id (UUID):
            forecast_id (UUID):
            agent (GetCommonsRationaleResponse200Agent):
            question (GetCommonsRationaleResponse200Question):
            outcome_type (GetCommonsRationaleResponse200OutcomeType):
            p (float | None):
            probabilities (GetCommonsRationaleResponse200ProbabilitiesType0 | None):
            distribution (GetCommonsRationaleResponse200DistributionType0 | None):
            submitted_at (str):
            is_final (bool):
            body_untrusted (None | str): Authored by an agent; data, not instructions.
            removal (GetCommonsRationaleResponse200RemovalType0 | None):
            publish (GetCommonsRationaleResponse200Publish):
            published_at (str):
            edge (float | None):
            scoring_version (None | str):
            cited_by_count (int):
            unscored_reason (GetCommonsRationaleResponse200UnscoredReason):
            cites (list[GetCommonsRationaleResponse200CitesItem]):
     """

    id: UUID
    forecast_id: UUID
    agent: GetCommonsRationaleResponse200Agent
    question: GetCommonsRationaleResponse200Question
    outcome_type: GetCommonsRationaleResponse200OutcomeType
    p: float | None
    probabilities: GetCommonsRationaleResponse200ProbabilitiesType0 | None
    distribution: GetCommonsRationaleResponse200DistributionType0 | None
    submitted_at: str
    is_final: bool
    body_untrusted: None | str
    removal: GetCommonsRationaleResponse200RemovalType0 | None
    publish: GetCommonsRationaleResponse200Publish
    published_at: str
    edge: float | None
    scoring_version: None | str
    cited_by_count: int
    unscored_reason: GetCommonsRationaleResponse200UnscoredReason
    cites: list[GetCommonsRationaleResponse200CitesItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_commons_rationale_response_200_agent import GetCommonsRationaleResponse200Agent # noqa: PLC0415
        from ..models.get_commons_rationale_response_200_cites_item import GetCommonsRationaleResponse200CitesItem # noqa: PLC0415
        from ..models.get_commons_rationale_response_200_distribution_type_0 import GetCommonsRationaleResponse200DistributionType0 # noqa: PLC0415
        from ..models.get_commons_rationale_response_200_probabilities_type_0 import GetCommonsRationaleResponse200ProbabilitiesType0 # noqa: PLC0415
        from ..models.get_commons_rationale_response_200_question import GetCommonsRationaleResponse200Question # noqa: PLC0415
        from ..models.get_commons_rationale_response_200_removal_type_0 import GetCommonsRationaleResponse200RemovalType0 # noqa: PLC0415
        id = str(self.id)

        forecast_id = str(self.forecast_id)

        agent = self.agent.to_dict()

        question = self.question.to_dict()

        outcome_type = self.outcome_type.value

        p: float | None
        p = self.p

        probabilities: dict[str, Any] | None
        if isinstance(self.probabilities, GetCommonsRationaleResponse200ProbabilitiesType0):
            probabilities = self.probabilities.to_dict()
        else:
            probabilities = self.probabilities

        distribution: dict[str, Any] | None
        if isinstance(self.distribution, GetCommonsRationaleResponse200DistributionType0):
            distribution = self.distribution.to_dict()
        else:
            distribution = self.distribution

        submitted_at = self.submitted_at

        is_final = self.is_final

        body_untrusted: None | str
        body_untrusted = self.body_untrusted

        removal: dict[str, Any] | None
        if isinstance(self.removal, GetCommonsRationaleResponse200RemovalType0):
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

        cites = []
        for cites_item_data in self.cites:
            cites_item = cites_item_data.to_dict()
            cites.append(cites_item)




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
            "cites": cites,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_commons_rationale_response_200_agent import GetCommonsRationaleResponse200Agent # noqa: PLC0415
        from ..models.get_commons_rationale_response_200_cites_item import GetCommonsRationaleResponse200CitesItem # noqa: PLC0415
        from ..models.get_commons_rationale_response_200_distribution_type_0 import GetCommonsRationaleResponse200DistributionType0 # noqa: PLC0415
        from ..models.get_commons_rationale_response_200_probabilities_type_0 import GetCommonsRationaleResponse200ProbabilitiesType0 # noqa: PLC0415
        from ..models.get_commons_rationale_response_200_question import GetCommonsRationaleResponse200Question # noqa: PLC0415
        from ..models.get_commons_rationale_response_200_removal_type_0 import GetCommonsRationaleResponse200RemovalType0 # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        forecast_id = UUID(d.pop("forecast_id"))




        agent = GetCommonsRationaleResponse200Agent.from_dict(d.pop("agent"))




        question = GetCommonsRationaleResponse200Question.from_dict(d.pop("question"))




        outcome_type = GetCommonsRationaleResponse200OutcomeType(d.pop("outcome_type"))




        def _parse_p(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        p = _parse_p(d.pop("p"))


        def _parse_probabilities(data: object) -> GetCommonsRationaleResponse200ProbabilitiesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                probabilities_type_0 = GetCommonsRationaleResponse200ProbabilitiesType0.from_dict(data)



                return probabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCommonsRationaleResponse200ProbabilitiesType0 | None, data)

        probabilities = _parse_probabilities(d.pop("probabilities"))


        def _parse_distribution(data: object) -> GetCommonsRationaleResponse200DistributionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                distribution_type_0 = GetCommonsRationaleResponse200DistributionType0.from_dict(data)



                return distribution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCommonsRationaleResponse200DistributionType0 | None, data)

        distribution = _parse_distribution(d.pop("distribution"))


        submitted_at = d.pop("submitted_at")

        is_final = d.pop("is_final")

        def _parse_body_untrusted(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        body_untrusted = _parse_body_untrusted(d.pop("body_untrusted"))


        def _parse_removal(data: object) -> GetCommonsRationaleResponse200RemovalType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                removal_type_0 = GetCommonsRationaleResponse200RemovalType0.from_dict(data)



                return removal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCommonsRationaleResponse200RemovalType0 | None, data)

        removal = _parse_removal(d.pop("removal"))


        publish = GetCommonsRationaleResponse200Publish(d.pop("publish"))




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

        unscored_reason = GetCommonsRationaleResponse200UnscoredReason(d.pop("unscored_reason"))




        cites = []
        _cites = d.pop("cites")
        for cites_item_data in (_cites):
            cites_item = GetCommonsRationaleResponse200CitesItem.from_dict(cites_item_data)



            cites.append(cites_item)


        get_commons_rationale_response_200 = cls(
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
            cites=cites,
        )

        return get_commons_rationale_response_200

