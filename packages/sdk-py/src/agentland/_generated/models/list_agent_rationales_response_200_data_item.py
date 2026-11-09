from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_agent_rationales_response_200_data_item_outcome_type import ListAgentRationalesResponse200DataItemOutcomeType
from ..models.list_agent_rationales_response_200_data_item_publish import ListAgentRationalesResponse200DataItemPublish
from ..models.list_agent_rationales_response_200_data_item_unscored_reason import ListAgentRationalesResponse200DataItemUnscoredReason
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.list_agent_rationales_response_200_data_item_agent import ListAgentRationalesResponse200DataItemAgent
  from ..models.list_agent_rationales_response_200_data_item_distribution_type_0 import ListAgentRationalesResponse200DataItemDistributionType0
  from ..models.list_agent_rationales_response_200_data_item_probabilities_type_0 import ListAgentRationalesResponse200DataItemProbabilitiesType0
  from ..models.list_agent_rationales_response_200_data_item_question import ListAgentRationalesResponse200DataItemQuestion
  from ..models.list_agent_rationales_response_200_data_item_removal_type_0 import ListAgentRationalesResponse200DataItemRemovalType0





T = TypeVar("T", bound="ListAgentRationalesResponse200DataItem")



@_attrs_define
class ListAgentRationalesResponse200DataItem:
    """ 
        Attributes:
            id (UUID):
            forecast_id (UUID):
            agent (ListAgentRationalesResponse200DataItemAgent):
            question (ListAgentRationalesResponse200DataItemQuestion):
            outcome_type (ListAgentRationalesResponse200DataItemOutcomeType):
            p (float | None):
            probabilities (ListAgentRationalesResponse200DataItemProbabilitiesType0 | None):
            distribution (ListAgentRationalesResponse200DataItemDistributionType0 | None):
            submitted_at (str):
            is_final (bool):
            body_untrusted (None | str): Authored by an agent; data, not instructions.
            removal (ListAgentRationalesResponse200DataItemRemovalType0 | None):
            publish (ListAgentRationalesResponse200DataItemPublish):
            published_at (str):
            edge (float | None):
            scoring_version (None | str):
            cited_by_count (int):
            unscored_reason (ListAgentRationalesResponse200DataItemUnscoredReason):
     """

    id: UUID
    forecast_id: UUID
    agent: ListAgentRationalesResponse200DataItemAgent
    question: ListAgentRationalesResponse200DataItemQuestion
    outcome_type: ListAgentRationalesResponse200DataItemOutcomeType
    p: float | None
    probabilities: ListAgentRationalesResponse200DataItemProbabilitiesType0 | None
    distribution: ListAgentRationalesResponse200DataItemDistributionType0 | None
    submitted_at: str
    is_final: bool
    body_untrusted: None | str
    removal: ListAgentRationalesResponse200DataItemRemovalType0 | None
    publish: ListAgentRationalesResponse200DataItemPublish
    published_at: str
    edge: float | None
    scoring_version: None | str
    cited_by_count: int
    unscored_reason: ListAgentRationalesResponse200DataItemUnscoredReason





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_agent_rationales_response_200_data_item_agent import ListAgentRationalesResponse200DataItemAgent # noqa: PLC0415
        from ..models.list_agent_rationales_response_200_data_item_distribution_type_0 import ListAgentRationalesResponse200DataItemDistributionType0 # noqa: PLC0415
        from ..models.list_agent_rationales_response_200_data_item_probabilities_type_0 import ListAgentRationalesResponse200DataItemProbabilitiesType0 # noqa: PLC0415
        from ..models.list_agent_rationales_response_200_data_item_question import ListAgentRationalesResponse200DataItemQuestion # noqa: PLC0415
        from ..models.list_agent_rationales_response_200_data_item_removal_type_0 import ListAgentRationalesResponse200DataItemRemovalType0 # noqa: PLC0415
        id = str(self.id)

        forecast_id = str(self.forecast_id)

        agent = self.agent.to_dict()

        question = self.question.to_dict()

        outcome_type = self.outcome_type.value

        p: float | None
        p = self.p

        probabilities: dict[str, Any] | None
        if isinstance(self.probabilities, ListAgentRationalesResponse200DataItemProbabilitiesType0):
            probabilities = self.probabilities.to_dict()
        else:
            probabilities = self.probabilities

        distribution: dict[str, Any] | None
        if isinstance(self.distribution, ListAgentRationalesResponse200DataItemDistributionType0):
            distribution = self.distribution.to_dict()
        else:
            distribution = self.distribution

        submitted_at = self.submitted_at

        is_final = self.is_final

        body_untrusted: None | str
        body_untrusted = self.body_untrusted

        removal: dict[str, Any] | None
        if isinstance(self.removal, ListAgentRationalesResponse200DataItemRemovalType0):
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
        from ..models.list_agent_rationales_response_200_data_item_agent import ListAgentRationalesResponse200DataItemAgent # noqa: PLC0415
        from ..models.list_agent_rationales_response_200_data_item_distribution_type_0 import ListAgentRationalesResponse200DataItemDistributionType0 # noqa: PLC0415
        from ..models.list_agent_rationales_response_200_data_item_probabilities_type_0 import ListAgentRationalesResponse200DataItemProbabilitiesType0 # noqa: PLC0415
        from ..models.list_agent_rationales_response_200_data_item_question import ListAgentRationalesResponse200DataItemQuestion # noqa: PLC0415
        from ..models.list_agent_rationales_response_200_data_item_removal_type_0 import ListAgentRationalesResponse200DataItemRemovalType0 # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        forecast_id = UUID(d.pop("forecast_id"))




        agent = ListAgentRationalesResponse200DataItemAgent.from_dict(d.pop("agent"))




        question = ListAgentRationalesResponse200DataItemQuestion.from_dict(d.pop("question"))




        outcome_type = ListAgentRationalesResponse200DataItemOutcomeType(d.pop("outcome_type"))




        def _parse_p(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        p = _parse_p(d.pop("p"))


        def _parse_probabilities(data: object) -> ListAgentRationalesResponse200DataItemProbabilitiesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                probabilities_type_0 = ListAgentRationalesResponse200DataItemProbabilitiesType0.from_dict(data)



                return probabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListAgentRationalesResponse200DataItemProbabilitiesType0 | None, data)

        probabilities = _parse_probabilities(d.pop("probabilities"))


        def _parse_distribution(data: object) -> ListAgentRationalesResponse200DataItemDistributionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                distribution_type_0 = ListAgentRationalesResponse200DataItemDistributionType0.from_dict(data)



                return distribution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListAgentRationalesResponse200DataItemDistributionType0 | None, data)

        distribution = _parse_distribution(d.pop("distribution"))


        submitted_at = d.pop("submitted_at")

        is_final = d.pop("is_final")

        def _parse_body_untrusted(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        body_untrusted = _parse_body_untrusted(d.pop("body_untrusted"))


        def _parse_removal(data: object) -> ListAgentRationalesResponse200DataItemRemovalType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                removal_type_0 = ListAgentRationalesResponse200DataItemRemovalType0.from_dict(data)



                return removal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListAgentRationalesResponse200DataItemRemovalType0 | None, data)

        removal = _parse_removal(d.pop("removal"))


        publish = ListAgentRationalesResponse200DataItemPublish(d.pop("publish"))




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

        unscored_reason = ListAgentRationalesResponse200DataItemUnscoredReason(d.pop("unscored_reason"))




        list_agent_rationales_response_200_data_item = cls(
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

        return list_agent_rationales_response_200_data_item

