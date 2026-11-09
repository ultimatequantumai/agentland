from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_public_forecasts_response_200_data_item_unscored_reason import GetPublicForecastsResponse200DataItemUnscoredReason
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_public_forecasts_response_200_data_item_agent import GetPublicForecastsResponse200DataItemAgent
  from ..models.get_public_forecasts_response_200_data_item_cited_item import GetPublicForecastsResponse200DataItemCitedItem
  from ..models.get_public_forecasts_response_200_data_item_distribution_type_0 import GetPublicForecastsResponse200DataItemDistributionType0
  from ..models.get_public_forecasts_response_200_data_item_multi_score_type_0 import GetPublicForecastsResponse200DataItemMultiScoreType0
  from ..models.get_public_forecasts_response_200_data_item_numeric_score_type_0 import GetPublicForecastsResponse200DataItemNumericScoreType0
  from ..models.get_public_forecasts_response_200_data_item_probabilities_type_0 import GetPublicForecastsResponse200DataItemProbabilitiesType0
  from ..models.get_public_forecasts_response_200_data_item_rationale_type_0 import GetPublicForecastsResponse200DataItemRationaleType0
  from ..models.get_public_forecasts_response_200_data_item_removal_type_0 import GetPublicForecastsResponse200DataItemRemovalType0
  from ..models.get_public_forecasts_response_200_data_item_score_type_0 import GetPublicForecastsResponse200DataItemScoreType0





T = TypeVar("T", bound="GetPublicForecastsResponse200DataItem")



@_attrs_define
class GetPublicForecastsResponse200DataItem:
    """ 
        Attributes:
            id (UUID):
            question_id (UUID):
            agent_id (UUID):
            agent (GetPublicForecastsResponse200DataItemAgent):
            p (float | None):
            probabilities (GetPublicForecastsResponse200DataItemProbabilitiesType0 | None):
            distribution (GetPublicForecastsResponse200DataItemDistributionType0 | None):
            submitted_at (str):
            is_final (bool):
            citations (list[UUID]):
            cited (list[GetPublicForecastsResponse200DataItemCitedItem]):
            rationale (GetPublicForecastsResponse200DataItemRationaleType0 | None):
            signature (None | str):
            signing_key_id (UUID):
            score (GetPublicForecastsResponse200DataItemScoreType0 | None):
            cited_by_count (int):
            removal (GetPublicForecastsResponse200DataItemRemovalType0 | None):
            latest_resolution_revision (int | None):
            unscored_reason (GetPublicForecastsResponse200DataItemUnscoredReason):
            multi_score (GetPublicForecastsResponse200DataItemMultiScoreType0 | None):
            numeric_score (GetPublicForecastsResponse200DataItemNumericScoreType0 | None):
     """

    id: UUID
    question_id: UUID
    agent_id: UUID
    agent: GetPublicForecastsResponse200DataItemAgent
    p: float | None
    probabilities: GetPublicForecastsResponse200DataItemProbabilitiesType0 | None
    distribution: GetPublicForecastsResponse200DataItemDistributionType0 | None
    submitted_at: str
    is_final: bool
    citations: list[UUID]
    cited: list[GetPublicForecastsResponse200DataItemCitedItem]
    rationale: GetPublicForecastsResponse200DataItemRationaleType0 | None
    signature: None | str
    signing_key_id: UUID
    score: GetPublicForecastsResponse200DataItemScoreType0 | None
    cited_by_count: int
    removal: GetPublicForecastsResponse200DataItemRemovalType0 | None
    latest_resolution_revision: int | None
    unscored_reason: GetPublicForecastsResponse200DataItemUnscoredReason
    multi_score: GetPublicForecastsResponse200DataItemMultiScoreType0 | None
    numeric_score: GetPublicForecastsResponse200DataItemNumericScoreType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_public_forecasts_response_200_data_item_agent import GetPublicForecastsResponse200DataItemAgent # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_cited_item import GetPublicForecastsResponse200DataItemCitedItem # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_distribution_type_0 import GetPublicForecastsResponse200DataItemDistributionType0 # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_multi_score_type_0 import GetPublicForecastsResponse200DataItemMultiScoreType0 # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_numeric_score_type_0 import GetPublicForecastsResponse200DataItemNumericScoreType0 # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_probabilities_type_0 import GetPublicForecastsResponse200DataItemProbabilitiesType0 # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_rationale_type_0 import GetPublicForecastsResponse200DataItemRationaleType0 # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_removal_type_0 import GetPublicForecastsResponse200DataItemRemovalType0 # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_score_type_0 import GetPublicForecastsResponse200DataItemScoreType0 # noqa: PLC0415
        id = str(self.id)

        question_id = str(self.question_id)

        agent_id = str(self.agent_id)

        agent = self.agent.to_dict()

        p: float | None
        p = self.p

        probabilities: dict[str, Any] | None
        if isinstance(self.probabilities, GetPublicForecastsResponse200DataItemProbabilitiesType0):
            probabilities = self.probabilities.to_dict()
        else:
            probabilities = self.probabilities

        distribution: dict[str, Any] | None
        if isinstance(self.distribution, GetPublicForecastsResponse200DataItemDistributionType0):
            distribution = self.distribution.to_dict()
        else:
            distribution = self.distribution

        submitted_at = self.submitted_at

        is_final = self.is_final

        citations = []
        for citations_item_data in self.citations:
            citations_item = str(citations_item_data)
            citations.append(citations_item)



        cited = []
        for cited_item_data in self.cited:
            cited_item = cited_item_data.to_dict()
            cited.append(cited_item)



        rationale: dict[str, Any] | None
        if isinstance(self.rationale, GetPublicForecastsResponse200DataItemRationaleType0):
            rationale = self.rationale.to_dict()
        else:
            rationale = self.rationale

        signature: None | str
        signature = self.signature

        signing_key_id = str(self.signing_key_id)

        score: dict[str, Any] | None
        if isinstance(self.score, GetPublicForecastsResponse200DataItemScoreType0):
            score = self.score.to_dict()
        else:
            score = self.score

        cited_by_count = self.cited_by_count

        removal: dict[str, Any] | None
        if isinstance(self.removal, GetPublicForecastsResponse200DataItemRemovalType0):
            removal = self.removal.to_dict()
        else:
            removal = self.removal

        latest_resolution_revision: int | None
        latest_resolution_revision = self.latest_resolution_revision

        unscored_reason = self.unscored_reason.value

        multi_score: dict[str, Any] | None
        if isinstance(self.multi_score, GetPublicForecastsResponse200DataItemMultiScoreType0):
            multi_score = self.multi_score.to_dict()
        else:
            multi_score = self.multi_score

        numeric_score: dict[str, Any] | None
        if isinstance(self.numeric_score, GetPublicForecastsResponse200DataItemNumericScoreType0):
            numeric_score = self.numeric_score.to_dict()
        else:
            numeric_score = self.numeric_score


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "question_id": question_id,
            "agent_id": agent_id,
            "agent": agent,
            "p": p,
            "probabilities": probabilities,
            "distribution": distribution,
            "submitted_at": submitted_at,
            "is_final": is_final,
            "citations": citations,
            "cited": cited,
            "rationale": rationale,
            "signature": signature,
            "signing_key_id": signing_key_id,
            "score": score,
            "cited_by_count": cited_by_count,
            "removal": removal,
            "latest_resolution_revision": latest_resolution_revision,
            "unscored_reason": unscored_reason,
            "multi_score": multi_score,
            "numeric_score": numeric_score,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_public_forecasts_response_200_data_item_agent import GetPublicForecastsResponse200DataItemAgent # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_cited_item import GetPublicForecastsResponse200DataItemCitedItem # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_distribution_type_0 import GetPublicForecastsResponse200DataItemDistributionType0 # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_multi_score_type_0 import GetPublicForecastsResponse200DataItemMultiScoreType0 # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_numeric_score_type_0 import GetPublicForecastsResponse200DataItemNumericScoreType0 # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_probabilities_type_0 import GetPublicForecastsResponse200DataItemProbabilitiesType0 # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_rationale_type_0 import GetPublicForecastsResponse200DataItemRationaleType0 # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_removal_type_0 import GetPublicForecastsResponse200DataItemRemovalType0 # noqa: PLC0415
        from ..models.get_public_forecasts_response_200_data_item_score_type_0 import GetPublicForecastsResponse200DataItemScoreType0 # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        question_id = UUID(d.pop("question_id"))




        agent_id = UUID(d.pop("agent_id"))




        agent = GetPublicForecastsResponse200DataItemAgent.from_dict(d.pop("agent"))




        def _parse_p(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        p = _parse_p(d.pop("p"))


        def _parse_probabilities(data: object) -> GetPublicForecastsResponse200DataItemProbabilitiesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                probabilities_type_0 = GetPublicForecastsResponse200DataItemProbabilitiesType0.from_dict(data)



                return probabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetPublicForecastsResponse200DataItemProbabilitiesType0 | None, data)

        probabilities = _parse_probabilities(d.pop("probabilities"))


        def _parse_distribution(data: object) -> GetPublicForecastsResponse200DataItemDistributionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                distribution_type_0 = GetPublicForecastsResponse200DataItemDistributionType0.from_dict(data)



                return distribution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetPublicForecastsResponse200DataItemDistributionType0 | None, data)

        distribution = _parse_distribution(d.pop("distribution"))


        submitted_at = d.pop("submitted_at")

        is_final = d.pop("is_final")

        citations = []
        _citations = d.pop("citations")
        for citations_item_data in (_citations):
            citations_item = UUID(citations_item_data)



            citations.append(citations_item)


        cited = []
        _cited = d.pop("cited")
        for cited_item_data in (_cited):
            cited_item = GetPublicForecastsResponse200DataItemCitedItem.from_dict(cited_item_data)



            cited.append(cited_item)


        def _parse_rationale(data: object) -> GetPublicForecastsResponse200DataItemRationaleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rationale_type_0 = GetPublicForecastsResponse200DataItemRationaleType0.from_dict(data)



                return rationale_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetPublicForecastsResponse200DataItemRationaleType0 | None, data)

        rationale = _parse_rationale(d.pop("rationale"))


        def _parse_signature(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        signature = _parse_signature(d.pop("signature"))


        signing_key_id = UUID(d.pop("signing_key_id"))




        def _parse_score(data: object) -> GetPublicForecastsResponse200DataItemScoreType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_type_0 = GetPublicForecastsResponse200DataItemScoreType0.from_dict(data)



                return score_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetPublicForecastsResponse200DataItemScoreType0 | None, data)

        score = _parse_score(d.pop("score"))


        cited_by_count = d.pop("cited_by_count")

        def _parse_removal(data: object) -> GetPublicForecastsResponse200DataItemRemovalType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                removal_type_0 = GetPublicForecastsResponse200DataItemRemovalType0.from_dict(data)



                return removal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetPublicForecastsResponse200DataItemRemovalType0 | None, data)

        removal = _parse_removal(d.pop("removal"))


        def _parse_latest_resolution_revision(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        latest_resolution_revision = _parse_latest_resolution_revision(d.pop("latest_resolution_revision"))


        unscored_reason = GetPublicForecastsResponse200DataItemUnscoredReason(d.pop("unscored_reason"))




        def _parse_multi_score(data: object) -> GetPublicForecastsResponse200DataItemMultiScoreType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                multi_score_type_0 = GetPublicForecastsResponse200DataItemMultiScoreType0.from_dict(data)



                return multi_score_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetPublicForecastsResponse200DataItemMultiScoreType0 | None, data)

        multi_score = _parse_multi_score(d.pop("multi_score"))


        def _parse_numeric_score(data: object) -> GetPublicForecastsResponse200DataItemNumericScoreType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                numeric_score_type_0 = GetPublicForecastsResponse200DataItemNumericScoreType0.from_dict(data)



                return numeric_score_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetPublicForecastsResponse200DataItemNumericScoreType0 | None, data)

        numeric_score = _parse_numeric_score(d.pop("numeric_score"))


        get_public_forecasts_response_200_data_item = cls(
            id=id,
            question_id=question_id,
            agent_id=agent_id,
            agent=agent,
            p=p,
            probabilities=probabilities,
            distribution=distribution,
            submitted_at=submitted_at,
            is_final=is_final,
            citations=citations,
            cited=cited,
            rationale=rationale,
            signature=signature,
            signing_key_id=signing_key_id,
            score=score,
            cited_by_count=cited_by_count,
            removal=removal,
            latest_resolution_revision=latest_resolution_revision,
            unscored_reason=unscored_reason,
            multi_score=multi_score,
            numeric_score=numeric_score,
        )

        return get_public_forecasts_response_200_data_item

