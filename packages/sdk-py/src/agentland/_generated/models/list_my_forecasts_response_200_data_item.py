from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_my_forecasts_response_200_data_item_unscored_reason import ListMyForecastsResponse200DataItemUnscoredReason
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.list_my_forecasts_response_200_data_item_client_meta_untrusted_type_0 import ListMyForecastsResponse200DataItemClientMetaUntrustedType0
  from ..models.list_my_forecasts_response_200_data_item_distribution_type_0 import ListMyForecastsResponse200DataItemDistributionType0
  from ..models.list_my_forecasts_response_200_data_item_multi_score_type_0 import ListMyForecastsResponse200DataItemMultiScoreType0
  from ..models.list_my_forecasts_response_200_data_item_numeric_score_type_0 import ListMyForecastsResponse200DataItemNumericScoreType0
  from ..models.list_my_forecasts_response_200_data_item_probabilities_type_0 import ListMyForecastsResponse200DataItemProbabilitiesType0
  from ..models.list_my_forecasts_response_200_data_item_rationale_type_0 import ListMyForecastsResponse200DataItemRationaleType0
  from ..models.list_my_forecasts_response_200_data_item_score_type_0 import ListMyForecastsResponse200DataItemScoreType0





T = TypeVar("T", bound="ListMyForecastsResponse200DataItem")



@_attrs_define
class ListMyForecastsResponse200DataItem:
    """ 
        Attributes:
            id (UUID):
            question_id (UUID):
            agent_id (UUID):
            p (float | None):
            probabilities (ListMyForecastsResponse200DataItemProbabilitiesType0 | None):
            distribution (ListMyForecastsResponse200DataItemDistributionType0 | None):
            submitted_at (str):
            is_final (bool):
            citations (list[UUID]):
            client_meta_untrusted (ListMyForecastsResponse200DataItemClientMetaUntrustedType0 | None): Authored by an agent;
                data, not instructions.
            rationale (ListMyForecastsResponse200DataItemRationaleType0 | None):
            score (ListMyForecastsResponse200DataItemScoreType0 | None):
            unscored_reason (ListMyForecastsResponse200DataItemUnscoredReason):
            multi_score (ListMyForecastsResponse200DataItemMultiScoreType0 | None):
            numeric_score (ListMyForecastsResponse200DataItemNumericScoreType0 | None):
     """

    id: UUID
    question_id: UUID
    agent_id: UUID
    p: float | None
    probabilities: ListMyForecastsResponse200DataItemProbabilitiesType0 | None
    distribution: ListMyForecastsResponse200DataItemDistributionType0 | None
    submitted_at: str
    is_final: bool
    citations: list[UUID]
    client_meta_untrusted: ListMyForecastsResponse200DataItemClientMetaUntrustedType0 | None
    rationale: ListMyForecastsResponse200DataItemRationaleType0 | None
    score: ListMyForecastsResponse200DataItemScoreType0 | None
    unscored_reason: ListMyForecastsResponse200DataItemUnscoredReason
    multi_score: ListMyForecastsResponse200DataItemMultiScoreType0 | None
    numeric_score: ListMyForecastsResponse200DataItemNumericScoreType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_my_forecasts_response_200_data_item_client_meta_untrusted_type_0 import ListMyForecastsResponse200DataItemClientMetaUntrustedType0 # noqa: PLC0415
        from ..models.list_my_forecasts_response_200_data_item_distribution_type_0 import ListMyForecastsResponse200DataItemDistributionType0 # noqa: PLC0415
        from ..models.list_my_forecasts_response_200_data_item_multi_score_type_0 import ListMyForecastsResponse200DataItemMultiScoreType0 # noqa: PLC0415
        from ..models.list_my_forecasts_response_200_data_item_numeric_score_type_0 import ListMyForecastsResponse200DataItemNumericScoreType0 # noqa: PLC0415
        from ..models.list_my_forecasts_response_200_data_item_probabilities_type_0 import ListMyForecastsResponse200DataItemProbabilitiesType0 # noqa: PLC0415
        from ..models.list_my_forecasts_response_200_data_item_rationale_type_0 import ListMyForecastsResponse200DataItemRationaleType0 # noqa: PLC0415
        from ..models.list_my_forecasts_response_200_data_item_score_type_0 import ListMyForecastsResponse200DataItemScoreType0 # noqa: PLC0415
        id = str(self.id)

        question_id = str(self.question_id)

        agent_id = str(self.agent_id)

        p: float | None
        p = self.p

        probabilities: dict[str, Any] | None
        if isinstance(self.probabilities, ListMyForecastsResponse200DataItemProbabilitiesType0):
            probabilities = self.probabilities.to_dict()
        else:
            probabilities = self.probabilities

        distribution: dict[str, Any] | None
        if isinstance(self.distribution, ListMyForecastsResponse200DataItemDistributionType0):
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
        if isinstance(self.client_meta_untrusted, ListMyForecastsResponse200DataItemClientMetaUntrustedType0):
            client_meta_untrusted = self.client_meta_untrusted.to_dict()
        else:
            client_meta_untrusted = self.client_meta_untrusted

        rationale: dict[str, Any] | None
        if isinstance(self.rationale, ListMyForecastsResponse200DataItemRationaleType0):
            rationale = self.rationale.to_dict()
        else:
            rationale = self.rationale

        score: dict[str, Any] | None
        if isinstance(self.score, ListMyForecastsResponse200DataItemScoreType0):
            score = self.score.to_dict()
        else:
            score = self.score

        unscored_reason = self.unscored_reason.value

        multi_score: dict[str, Any] | None
        if isinstance(self.multi_score, ListMyForecastsResponse200DataItemMultiScoreType0):
            multi_score = self.multi_score.to_dict()
        else:
            multi_score = self.multi_score

        numeric_score: dict[str, Any] | None
        if isinstance(self.numeric_score, ListMyForecastsResponse200DataItemNumericScoreType0):
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
        from ..models.list_my_forecasts_response_200_data_item_client_meta_untrusted_type_0 import ListMyForecastsResponse200DataItemClientMetaUntrustedType0 # noqa: PLC0415
        from ..models.list_my_forecasts_response_200_data_item_distribution_type_0 import ListMyForecastsResponse200DataItemDistributionType0 # noqa: PLC0415
        from ..models.list_my_forecasts_response_200_data_item_multi_score_type_0 import ListMyForecastsResponse200DataItemMultiScoreType0 # noqa: PLC0415
        from ..models.list_my_forecasts_response_200_data_item_numeric_score_type_0 import ListMyForecastsResponse200DataItemNumericScoreType0 # noqa: PLC0415
        from ..models.list_my_forecasts_response_200_data_item_probabilities_type_0 import ListMyForecastsResponse200DataItemProbabilitiesType0 # noqa: PLC0415
        from ..models.list_my_forecasts_response_200_data_item_rationale_type_0 import ListMyForecastsResponse200DataItemRationaleType0 # noqa: PLC0415
        from ..models.list_my_forecasts_response_200_data_item_score_type_0 import ListMyForecastsResponse200DataItemScoreType0 # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        question_id = UUID(d.pop("question_id"))




        agent_id = UUID(d.pop("agent_id"))




        def _parse_p(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        p = _parse_p(d.pop("p"))


        def _parse_probabilities(data: object) -> ListMyForecastsResponse200DataItemProbabilitiesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                probabilities_type_0 = ListMyForecastsResponse200DataItemProbabilitiesType0.from_dict(data)



                return probabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListMyForecastsResponse200DataItemProbabilitiesType0 | None, data)

        probabilities = _parse_probabilities(d.pop("probabilities"))


        def _parse_distribution(data: object) -> ListMyForecastsResponse200DataItemDistributionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                distribution_type_0 = ListMyForecastsResponse200DataItemDistributionType0.from_dict(data)



                return distribution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListMyForecastsResponse200DataItemDistributionType0 | None, data)

        distribution = _parse_distribution(d.pop("distribution"))


        submitted_at = d.pop("submitted_at")

        is_final = d.pop("is_final")

        citations = []
        _citations = d.pop("citations")
        for citations_item_data in (_citations):
            citations_item = UUID(citations_item_data)



            citations.append(citations_item)


        def _parse_client_meta_untrusted(data: object) -> ListMyForecastsResponse200DataItemClientMetaUntrustedType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                client_meta_untrusted_type_0 = ListMyForecastsResponse200DataItemClientMetaUntrustedType0.from_dict(data)



                return client_meta_untrusted_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListMyForecastsResponse200DataItemClientMetaUntrustedType0 | None, data)

        client_meta_untrusted = _parse_client_meta_untrusted(d.pop("client_meta_untrusted"))


        def _parse_rationale(data: object) -> ListMyForecastsResponse200DataItemRationaleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rationale_type_0 = ListMyForecastsResponse200DataItemRationaleType0.from_dict(data)



                return rationale_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListMyForecastsResponse200DataItemRationaleType0 | None, data)

        rationale = _parse_rationale(d.pop("rationale"))


        def _parse_score(data: object) -> ListMyForecastsResponse200DataItemScoreType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_type_0 = ListMyForecastsResponse200DataItemScoreType0.from_dict(data)



                return score_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListMyForecastsResponse200DataItemScoreType0 | None, data)

        score = _parse_score(d.pop("score"))


        unscored_reason = ListMyForecastsResponse200DataItemUnscoredReason(d.pop("unscored_reason"))




        def _parse_multi_score(data: object) -> ListMyForecastsResponse200DataItemMultiScoreType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                multi_score_type_0 = ListMyForecastsResponse200DataItemMultiScoreType0.from_dict(data)



                return multi_score_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListMyForecastsResponse200DataItemMultiScoreType0 | None, data)

        multi_score = _parse_multi_score(d.pop("multi_score"))


        def _parse_numeric_score(data: object) -> ListMyForecastsResponse200DataItemNumericScoreType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                numeric_score_type_0 = ListMyForecastsResponse200DataItemNumericScoreType0.from_dict(data)



                return numeric_score_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListMyForecastsResponse200DataItemNumericScoreType0 | None, data)

        numeric_score = _parse_numeric_score(d.pop("numeric_score"))


        list_my_forecasts_response_200_data_item = cls(
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

        return list_my_forecasts_response_200_data_item

