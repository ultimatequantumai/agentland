from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_daily_response_200_resolved_item_outcome_type import GetDailyResponse200ResolvedItemOutcomeType
from ..models.get_daily_response_200_resolved_item_void_reason_type_1 import GetDailyResponse200ResolvedItemVoidReasonType1
from ..models.get_daily_response_200_resolved_item_void_reason_type_2_type_1 import GetDailyResponse200ResolvedItemVoidReasonType2Type1
from ..models.get_daily_response_200_resolved_item_void_reason_type_3_type_1 import GetDailyResponse200ResolvedItemVoidReasonType3Type1
from typing import cast

if TYPE_CHECKING:
  from ..models.get_daily_response_200_resolved_item_best_type_0 import GetDailyResponse200ResolvedItemBestType0
  from ..models.get_daily_response_200_resolved_item_question import GetDailyResponse200ResolvedItemQuestion
  from ..models.get_daily_response_200_resolved_item_worst_type_0 import GetDailyResponse200ResolvedItemWorstType0





T = TypeVar("T", bound="GetDailyResponse200ResolvedItem")



@_attrs_define
class GetDailyResponse200ResolvedItem:
    """ 
        Attributes:
            question (GetDailyResponse200ResolvedItemQuestion):
            outcome (None | str):
            outcome_type (GetDailyResponse200ResolvedItemOutcomeType):
            outcome_label (None | str):
            value (None | str):
            unit (None | str):
            void_reason (GetDailyResponse200ResolvedItemVoidReasonType1 |
                GetDailyResponse200ResolvedItemVoidReasonType2Type1 | GetDailyResponse200ResolvedItemVoidReasonType3Type1 |
                None):
            resolved_at (str):
            revision (int | None):
            correction_href (None | str):
            market_p_at_close (float | None):
            best (GetDailyResponse200ResolvedItemBestType0 | None):
            worst (GetDailyResponse200ResolvedItemWorstType0 | None):
            scored_count (int):
            published_reasoning_count (int):
            series_key (None | str):
     """

    question: GetDailyResponse200ResolvedItemQuestion
    outcome: None | str
    outcome_type: GetDailyResponse200ResolvedItemOutcomeType
    outcome_label: None | str
    value: None | str
    unit: None | str
    void_reason: GetDailyResponse200ResolvedItemVoidReasonType1 | GetDailyResponse200ResolvedItemVoidReasonType2Type1 | GetDailyResponse200ResolvedItemVoidReasonType3Type1 | None
    resolved_at: str
    revision: int | None
    correction_href: None | str
    market_p_at_close: float | None
    best: GetDailyResponse200ResolvedItemBestType0 | None
    worst: GetDailyResponse200ResolvedItemWorstType0 | None
    scored_count: int
    published_reasoning_count: int
    series_key: None | str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_daily_response_200_resolved_item_best_type_0 import GetDailyResponse200ResolvedItemBestType0 # noqa: PLC0415
        from ..models.get_daily_response_200_resolved_item_question import GetDailyResponse200ResolvedItemQuestion # noqa: PLC0415
        from ..models.get_daily_response_200_resolved_item_worst_type_0 import GetDailyResponse200ResolvedItemWorstType0 # noqa: PLC0415
        question = self.question.to_dict()

        outcome: None | str
        outcome = self.outcome

        outcome_type = self.outcome_type.value

        outcome_label: None | str
        outcome_label = self.outcome_label

        value: None | str
        value = self.value

        unit: None | str
        unit = self.unit

        void_reason: None | str
        if isinstance(self.void_reason, GetDailyResponse200ResolvedItemVoidReasonType1):
            void_reason = self.void_reason.value
        elif isinstance(self.void_reason, GetDailyResponse200ResolvedItemVoidReasonType2Type1):
            void_reason = self.void_reason.value
        elif isinstance(self.void_reason, GetDailyResponse200ResolvedItemVoidReasonType3Type1):
            void_reason = self.void_reason.value
        else:
            void_reason = self.void_reason

        resolved_at = self.resolved_at

        revision: int | None
        revision = self.revision

        correction_href: None | str
        correction_href = self.correction_href

        market_p_at_close: float | None
        market_p_at_close = self.market_p_at_close

        best: dict[str, Any] | None
        if isinstance(self.best, GetDailyResponse200ResolvedItemBestType0):
            best = self.best.to_dict()
        else:
            best = self.best

        worst: dict[str, Any] | None
        if isinstance(self.worst, GetDailyResponse200ResolvedItemWorstType0):
            worst = self.worst.to_dict()
        else:
            worst = self.worst

        scored_count = self.scored_count

        published_reasoning_count = self.published_reasoning_count

        series_key: None | str
        series_key = self.series_key


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "question": question,
            "outcome": outcome,
            "outcome_type": outcome_type,
            "outcome_label": outcome_label,
            "value": value,
            "unit": unit,
            "void_reason": void_reason,
            "resolved_at": resolved_at,
            "revision": revision,
            "correction_href": correction_href,
            "market_p_at_close": market_p_at_close,
            "best": best,
            "worst": worst,
            "scored_count": scored_count,
            "published_reasoning_count": published_reasoning_count,
            "series_key": series_key,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_daily_response_200_resolved_item_best_type_0 import GetDailyResponse200ResolvedItemBestType0 # noqa: PLC0415
        from ..models.get_daily_response_200_resolved_item_question import GetDailyResponse200ResolvedItemQuestion # noqa: PLC0415
        from ..models.get_daily_response_200_resolved_item_worst_type_0 import GetDailyResponse200ResolvedItemWorstType0 # noqa: PLC0415
        d = dict(src_dict)
        question = GetDailyResponse200ResolvedItemQuestion.from_dict(d.pop("question"))




        def _parse_outcome(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        outcome = _parse_outcome(d.pop("outcome"))


        outcome_type = GetDailyResponse200ResolvedItemOutcomeType(d.pop("outcome_type"))




        def _parse_outcome_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        outcome_label = _parse_outcome_label(d.pop("outcome_label"))


        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))


        def _parse_unit(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        unit = _parse_unit(d.pop("unit"))


        def _parse_void_reason(data: object) -> GetDailyResponse200ResolvedItemVoidReasonType1 | GetDailyResponse200ResolvedItemVoidReasonType2Type1 | GetDailyResponse200ResolvedItemVoidReasonType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                void_reason_type_1 = GetDailyResponse200ResolvedItemVoidReasonType1(data)



                return void_reason_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                void_reason_type_2_type_1 = GetDailyResponse200ResolvedItemVoidReasonType2Type1(data)



                return void_reason_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                void_reason_type_3_type_1 = GetDailyResponse200ResolvedItemVoidReasonType3Type1(data)



                return void_reason_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetDailyResponse200ResolvedItemVoidReasonType1 | GetDailyResponse200ResolvedItemVoidReasonType2Type1 | GetDailyResponse200ResolvedItemVoidReasonType3Type1 | None, data)

        void_reason = _parse_void_reason(d.pop("void_reason"))


        resolved_at = d.pop("resolved_at")

        def _parse_revision(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        revision = _parse_revision(d.pop("revision"))


        def _parse_correction_href(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        correction_href = _parse_correction_href(d.pop("correction_href"))


        def _parse_market_p_at_close(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        market_p_at_close = _parse_market_p_at_close(d.pop("market_p_at_close"))


        def _parse_best(data: object) -> GetDailyResponse200ResolvedItemBestType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                best_type_0 = GetDailyResponse200ResolvedItemBestType0.from_dict(data)



                return best_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetDailyResponse200ResolvedItemBestType0 | None, data)

        best = _parse_best(d.pop("best"))


        def _parse_worst(data: object) -> GetDailyResponse200ResolvedItemWorstType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                worst_type_0 = GetDailyResponse200ResolvedItemWorstType0.from_dict(data)



                return worst_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetDailyResponse200ResolvedItemWorstType0 | None, data)

        worst = _parse_worst(d.pop("worst"))


        scored_count = d.pop("scored_count")

        published_reasoning_count = d.pop("published_reasoning_count")

        def _parse_series_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        series_key = _parse_series_key(d.pop("series_key"))


        get_daily_response_200_resolved_item = cls(
            question=question,
            outcome=outcome,
            outcome_type=outcome_type,
            outcome_label=outcome_label,
            value=value,
            unit=unit,
            void_reason=void_reason,
            resolved_at=resolved_at,
            revision=revision,
            correction_href=correction_href,
            market_p_at_close=market_p_at_close,
            best=best,
            worst=worst,
            scored_count=scored_count,
            published_reasoning_count=published_reasoning_count,
            series_key=series_key,
        )

        return get_daily_response_200_resolved_item

