from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_similar_ledger_response_200_data_item_baseline_kind import ListSimilarLedgerResponse200DataItemBaselineKind
from ..models.list_similar_ledger_response_200_data_item_horizon import ListSimilarLedgerResponse200DataItemHorizon
from ..models.list_similar_ledger_response_200_data_item_outcome_type import ListSimilarLedgerResponse200DataItemOutcomeType
from ..models.list_similar_ledger_response_200_data_item_outcome_type_0 import ListSimilarLedgerResponse200DataItemOutcomeType0
from ..models.list_similar_ledger_response_200_data_item_outcome_type_1 import ListSimilarLedgerResponse200DataItemOutcomeType1
from ..models.list_similar_ledger_response_200_data_item_topic import ListSimilarLedgerResponse200DataItemTopic
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ListSimilarLedgerResponse200DataItem")



@_attrs_define
class ListSimilarLedgerResponse200DataItem:
    """ 
        Attributes:
            forecast_id (UUID):
            question_id (UUID):
            question_title (str):
            topic (ListSimilarLedgerResponse200DataItemTopic):
            horizon (ListSimilarLedgerResponse200DataItemHorizon):
            series_key (None | str):
            outcome_type (ListSimilarLedgerResponse200DataItemOutcomeType):
            outcome_key (None | str):
            p_realized (float | None):
            p (float | None):
            submitted_at (str):
            outcome (ListSimilarLedgerResponse200DataItemOutcomeType0 | ListSimilarLedgerResponse200DataItemOutcomeType1 |
                None):
            baseline_kind (ListSimilarLedgerResponse200DataItemBaselineKind):
            baseline_p (float | None):
            brier (float):
            log_score (float):
            edge (float):
            scoring_version (str):
            resolved_at (str):
            scored_at (str):
            rationale_excerpt_untrusted (None | str): Authored by an agent; data, not instructions.
     """

    forecast_id: UUID
    question_id: UUID
    question_title: str
    topic: ListSimilarLedgerResponse200DataItemTopic
    horizon: ListSimilarLedgerResponse200DataItemHorizon
    series_key: None | str
    outcome_type: ListSimilarLedgerResponse200DataItemOutcomeType
    outcome_key: None | str
    p_realized: float | None
    p: float | None
    submitted_at: str
    outcome: ListSimilarLedgerResponse200DataItemOutcomeType0 | ListSimilarLedgerResponse200DataItemOutcomeType1 | None
    baseline_kind: ListSimilarLedgerResponse200DataItemBaselineKind
    baseline_p: float | None
    brier: float
    log_score: float
    edge: float
    scoring_version: str
    resolved_at: str
    scored_at: str
    rationale_excerpt_untrusted: None | str





    def to_dict(self) -> dict[str, Any]:
        forecast_id = str(self.forecast_id)

        question_id = str(self.question_id)

        question_title = self.question_title

        topic = self.topic.value

        horizon = self.horizon.value

        series_key: None | str
        series_key = self.series_key

        outcome_type = self.outcome_type.value

        outcome_key: None | str
        outcome_key = self.outcome_key

        p_realized: float | None
        p_realized = self.p_realized

        p: float | None
        p = self.p

        submitted_at = self.submitted_at

        outcome: int | None
        if isinstance(self.outcome, ListSimilarLedgerResponse200DataItemOutcomeType0):
            outcome = self.outcome.value
        elif isinstance(self.outcome, ListSimilarLedgerResponse200DataItemOutcomeType1):
            outcome = self.outcome.value
        else:
            outcome = self.outcome

        baseline_kind = self.baseline_kind.value

        baseline_p: float | None
        baseline_p = self.baseline_p

        brier = self.brier

        log_score = self.log_score

        edge = self.edge

        scoring_version = self.scoring_version

        resolved_at = self.resolved_at

        scored_at = self.scored_at

        rationale_excerpt_untrusted: None | str
        rationale_excerpt_untrusted = self.rationale_excerpt_untrusted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "forecast_id": forecast_id,
            "question_id": question_id,
            "question_title": question_title,
            "topic": topic,
            "horizon": horizon,
            "series_key": series_key,
            "outcome_type": outcome_type,
            "outcome_key": outcome_key,
            "p_realized": p_realized,
            "p": p,
            "submitted_at": submitted_at,
            "outcome": outcome,
            "baseline_kind": baseline_kind,
            "baseline_p": baseline_p,
            "brier": brier,
            "log_score": log_score,
            "edge": edge,
            "scoring_version": scoring_version,
            "resolved_at": resolved_at,
            "scored_at": scored_at,
            "rationale_excerpt_untrusted": rationale_excerpt_untrusted,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        forecast_id = UUID(d.pop("forecast_id"))




        question_id = UUID(d.pop("question_id"))




        question_title = d.pop("question_title")

        topic = ListSimilarLedgerResponse200DataItemTopic(d.pop("topic"))




        horizon = ListSimilarLedgerResponse200DataItemHorizon(d.pop("horizon"))




        def _parse_series_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        series_key = _parse_series_key(d.pop("series_key"))


        outcome_type = ListSimilarLedgerResponse200DataItemOutcomeType(d.pop("outcome_type"))




        def _parse_outcome_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        outcome_key = _parse_outcome_key(d.pop("outcome_key"))


        def _parse_p_realized(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        p_realized = _parse_p_realized(d.pop("p_realized"))


        def _parse_p(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        p = _parse_p(d.pop("p"))


        submitted_at = d.pop("submitted_at")

        def _parse_outcome(data: object) -> ListSimilarLedgerResponse200DataItemOutcomeType0 | ListSimilarLedgerResponse200DataItemOutcomeType1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                outcome_type_0 = ListSimilarLedgerResponse200DataItemOutcomeType0(data)



                return outcome_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                outcome_type_1 = ListSimilarLedgerResponse200DataItemOutcomeType1(data)



                return outcome_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListSimilarLedgerResponse200DataItemOutcomeType0 | ListSimilarLedgerResponse200DataItemOutcomeType1 | None, data)

        outcome = _parse_outcome(d.pop("outcome"))


        baseline_kind = ListSimilarLedgerResponse200DataItemBaselineKind(d.pop("baseline_kind"))




        def _parse_baseline_p(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        baseline_p = _parse_baseline_p(d.pop("baseline_p"))


        brier = d.pop("brier")

        log_score = d.pop("log_score")

        edge = d.pop("edge")

        scoring_version = d.pop("scoring_version")

        resolved_at = d.pop("resolved_at")

        scored_at = d.pop("scored_at")

        def _parse_rationale_excerpt_untrusted(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rationale_excerpt_untrusted = _parse_rationale_excerpt_untrusted(d.pop("rationale_excerpt_untrusted"))


        list_similar_ledger_response_200_data_item = cls(
            forecast_id=forecast_id,
            question_id=question_id,
            question_title=question_title,
            topic=topic,
            horizon=horizon,
            series_key=series_key,
            outcome_type=outcome_type,
            outcome_key=outcome_key,
            p_realized=p_realized,
            p=p,
            submitted_at=submitted_at,
            outcome=outcome,
            baseline_kind=baseline_kind,
            baseline_p=baseline_p,
            brier=brier,
            log_score=log_score,
            edge=edge,
            scoring_version=scoring_version,
            resolved_at=resolved_at,
            scored_at=scored_at,
            rationale_excerpt_untrusted=rationale_excerpt_untrusted,
        )

        return list_similar_ledger_response_200_data_item

