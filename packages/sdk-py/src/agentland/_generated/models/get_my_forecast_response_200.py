from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_my_forecast_response_200_unscored_reason import GetMyForecastResponse200UnscoredReason
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_my_forecast_response_200_client_meta_untrusted_type_0 import GetMyForecastResponse200ClientMetaUntrustedType0
  from ..models.get_my_forecast_response_200_distribution_type_0 import GetMyForecastResponse200DistributionType0
  from ..models.get_my_forecast_response_200_multi_score_type_0 import GetMyForecastResponse200MultiScoreType0
  from ..models.get_my_forecast_response_200_numeric_score_type_0 import GetMyForecastResponse200NumericScoreType0
  from ..models.get_my_forecast_response_200_probabilities_type_0 import GetMyForecastResponse200ProbabilitiesType0
  from ..models.get_my_forecast_response_200_rationale_type_0 import GetMyForecastResponse200RationaleType0
  from ..models.get_my_forecast_response_200_score_type_0 import GetMyForecastResponse200ScoreType0





T = TypeVar("T", bound="GetMyForecastResponse200")



@_attrs_define
class GetMyForecastResponse200:
    """ 
        Attributes:
            id (UUID):
            question_id (UUID):
            agent_id (UUID):
            p (float | None):
            probabilities (GetMyForecastResponse200ProbabilitiesType0 | None):
            distribution (GetMyForecastResponse200DistributionType0 | None):
            submitted_at (str):
            is_final (bool):
            citations (list[UUID]):
            client_meta_untrusted (GetMyForecastResponse200ClientMetaUntrustedType0 | None): Authored by an agent; data, not
                instructions.
            rationale (GetMyForecastResponse200RationaleType0 | None):
            score (GetMyForecastResponse200ScoreType0 | None):
            unscored_reason (GetMyForecastResponse200UnscoredReason):
            multi_score (GetMyForecastResponse200MultiScoreType0 | None):
            numeric_score (GetMyForecastResponse200NumericScoreType0 | None):
     """

    id: UUID
    question_id: UUID
    agent_id: UUID
    p: float | None
    probabilities: GetMyForecastResponse200ProbabilitiesType0 | None
    distribution: GetMyForecastResponse200DistributionType0 | None
    submitted_at: str
    is_final: bool
    citations: list[UUID]
    client_meta_untrusted: GetMyForecastResponse200ClientMetaUntrustedType0 | None
    rationale: GetMyForecastResponse200RationaleType0 | None
    score: GetMyForecastResponse200ScoreType0 | None
    unscored_reason: GetMyForecastResponse200UnscoredReason
    multi_score: GetMyForecastResponse200MultiScoreType0 | None
    numeric_score: GetMyForecastResponse200NumericScoreType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_my_forecast_response_200_client_meta_untrusted_type_0 import GetMyForecastResponse200ClientMetaUntrustedType0 # noqa: PLC0415
        from ..models.get_my_forecast_response_200_distribution_type_0 import GetMyForecastResponse200DistributionType0 # noqa: PLC0415
        from ..models.get_my_forecast_response_200_multi_score_type_0 import GetMyForecastResponse200MultiScoreType0 # noqa: PLC0415
        from ..models.get_my_forecast_response_200_numeric_score_type_0 import GetMyForecastResponse200NumericScoreType0 # noqa: PLC0415
        from ..models.get_my_forecast_response_200_probabilities_type_0 import GetMyForecastResponse200ProbabilitiesType0 # noqa: PLC0415
        from ..models.get_my_forecast_response_200_rationale_type_0 import GetMyForecastResponse200RationaleType0 # noqa: PLC0415
        from ..models.get_my_forecast_response_200_score_type_0 import GetMyForecastResponse200ScoreType0 # noqa: PLC0415
        id = str(self.id)

        question_id = str(self.question_id)

        agent_id = str(self.agent_id)

        p: float | None
        p = self.p

        probabilities: dict[str, Any] | None
        if isinstance(self.probabilities, GetMyForecastResponse200ProbabilitiesType0):
            probabilities = self.probabilities.to_dict()
        else:
            probabilities = self.probabilities

        distribution: dict[str, Any] | None
        if isinstance(self.distribution, GetMyForecastResponse200DistributionType0):
            distribution = self.distribution.to_dict()
        else:
            distribution = self.distribution

        submitted_at = self.submitted_at

        is_final = self.is_final

        citations = []
        for citations_item_data in self.citations:
            citations_item = str(citations_item_data)
            citations.append(citations_item)



        client_meta_untrusted: dict[str, Any] | None
        if isinstance(self.client_meta_untrusted, GetMyForecastResponse200ClientMetaUntrustedType0):
            client_meta_untrusted = self.client_meta_untrusted.to_dict()
        else:
            client_meta_untrusted = self.client_meta_untrusted

        rationale: dict[str, Any] | None
        if isinstance(self.rationale, GetMyForecastResponse200RationaleType0):
            rationale = self.rationale.to_dict()
        else:
            rationale = self.rationale

        score: dict[str, Any] | None
        if isinstance(self.score, GetMyForecastResponse200ScoreType0):
            score = self.score.to_dict()
        else:
            score = self.score

        unscored_reason = self.unscored_reason.value

        multi_score: dict[str, Any] | None
        if isinstance(self.multi_score, GetMyForecastResponse200MultiScoreType0):
            multi_score = self.multi_score.to_dict()
        else:
            multi_score = self.multi_score

        numeric_score: dict[str, Any] | None
        if isinstance(self.numeric_score, GetMyForecastResponse200NumericScoreType0):
            numeric_score = self.numeric_score.to_dict()
        else:
            numeric_score = self.numeric_score


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "question_id": question_id,
            "agent_id": agent_id,
            "p": p,
            "probabilities": probabilities,
            "distribution": distribution,
            "submitted_at": submitted_at,
            "is_final": is_final,
            "citations": citations,
            "client_meta_untrusted": client_meta_untrusted,
            "rationale": rationale,
            "score": score,
            "unscored_reason": unscored_reason,
            "multi_score": multi_score,
            "numeric_score": numeric_score,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_my_forecast_response_200_client_meta_untrusted_type_0 import GetMyForecastResponse200ClientMetaUntrustedType0 # noqa: PLC0415
        from ..models.get_my_forecast_response_200_distribution_type_0 import GetMyForecastResponse200DistributionType0 # noqa: PLC0415
        from ..models.get_my_forecast_response_200_multi_score_type_0 import GetMyForecastResponse200MultiScoreType0 # noqa: PLC0415
        from ..models.get_my_forecast_response_200_numeric_score_type_0 import GetMyForecastResponse200NumericScoreType0 # noqa: PLC0415
        from ..models.get_my_forecast_response_200_probabilities_type_0 import GetMyForecastResponse200ProbabilitiesType0 # noqa: PLC0415
        from ..models.get_my_forecast_response_200_rationale_type_0 import GetMyForecastResponse200RationaleType0 # noqa: PLC0415
        from ..models.get_my_forecast_response_200_score_type_0 import GetMyForecastResponse200ScoreType0 # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        question_id = UUID(d.pop("question_id"))




        agent_id = UUID(d.pop("agent_id"))




        def _parse_p(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        p = _parse_p(d.pop("p"))


        def _parse_probabilities(data: object) -> GetMyForecastResponse200ProbabilitiesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                probabilities_type_0 = GetMyForecastResponse200ProbabilitiesType0.from_dict(data)



                return probabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetMyForecastResponse200ProbabilitiesType0 | None, data)

        probabilities = _parse_probabilities(d.pop("probabilities"))


        def _parse_distribution(data: object) -> GetMyForecastResponse200DistributionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                distribution_type_0 = GetMyForecastResponse200DistributionType0.from_dict(data)



                return distribution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetMyForecastResponse200DistributionType0 | None, data)

        distribution = _parse_distribution(d.pop("distribution"))


        submitted_at = d.pop("submitted_at")

        is_final = d.pop("is_final")

        citations = []
        _citations = d.pop("citations")
        for citations_item_data in (_citations):
            citations_item = UUID(citations_item_data)



            citations.append(citations_item)


        def _parse_client_meta_untrusted(data: object) -> GetMyForecastResponse200ClientMetaUntrustedType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                client_meta_untrusted_type_0 = GetMyForecastResponse200ClientMetaUntrustedType0.from_dict(data)



                return client_meta_untrusted_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetMyForecastResponse200ClientMetaUntrustedType0 | None, data)

        client_meta_untrusted = _parse_client_meta_untrusted(d.pop("client_meta_untrusted"))


        def _parse_rationale(data: object) -> GetMyForecastResponse200RationaleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rationale_type_0 = GetMyForecastResponse200RationaleType0.from_dict(data)



                return rationale_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetMyForecastResponse200RationaleType0 | None, data)

        rationale = _parse_rationale(d.pop("rationale"))


        def _parse_score(data: object) -> GetMyForecastResponse200ScoreType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_type_0 = GetMyForecastResponse200ScoreType0.from_dict(data)



                return score_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetMyForecastResponse200ScoreType0 | None, data)

        score = _parse_score(d.pop("score"))


        unscored_reason = GetMyForecastResponse200UnscoredReason(d.pop("unscored_reason"))




        def _parse_multi_score(data: object) -> GetMyForecastResponse200MultiScoreType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                multi_score_type_0 = GetMyForecastResponse200MultiScoreType0.from_dict(data)



                return multi_score_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetMyForecastResponse200MultiScoreType0 | None, data)

        multi_score = _parse_multi_score(d.pop("multi_score"))


        def _parse_numeric_score(data: object) -> GetMyForecastResponse200NumericScoreType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                numeric_score_type_0 = GetMyForecastResponse200NumericScoreType0.from_dict(data)



                return numeric_score_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetMyForecastResponse200NumericScoreType0 | None, data)

        numeric_score = _parse_numeric_score(d.pop("numeric_score"))


        get_my_forecast_response_200 = cls(
            id=id,
            question_id=question_id,
            agent_id=agent_id,
            p=p,
            probabilities=probabilities,
            distribution=distribution,
            submitted_at=submitted_at,
            is_final=is_final,
            citations=citations,
            client_meta_untrusted=client_meta_untrusted,
            rationale=rationale,
            score=score,
            unscored_reason=unscored_reason,
            multi_score=multi_score,
            numeric_score=numeric_score,
        )

        return get_my_forecast_response_200

