from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_transparency_response_200_disputes_data_item_timeline_item_kind import SearchTransparencyResponse200DisputesDataItemTimelineItemKind
from ..models.search_transparency_response_200_disputes_data_item_timeline_item_outcome_type import SearchTransparencyResponse200DisputesDataItemTimelineItemOutcomeType
from ..models.search_transparency_response_200_disputes_data_item_timeline_item_resolved_by_type_1 import SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType1
from ..models.search_transparency_response_200_disputes_data_item_timeline_item_resolved_by_type_2_type_1 import SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType2Type1
from ..models.search_transparency_response_200_disputes_data_item_timeline_item_resolved_by_type_3_type_1 import SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType3Type1
from ..models.search_transparency_response_200_disputes_data_item_timeline_item_status_type_1 import SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType1
from ..models.search_transparency_response_200_disputes_data_item_timeline_item_status_type_2_type_1 import SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType2Type1
from ..models.search_transparency_response_200_disputes_data_item_timeline_item_status_type_3_type_1 import SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType3Type1
from typing import cast

if TYPE_CHECKING:
  from ..models.search_transparency_response_200_disputes_data_item_timeline_item_season_type_0 import SearchTransparencyResponse200DisputesDataItemTimelineItemSeasonType0





T = TypeVar("T", bound="SearchTransparencyResponse200DisputesDataItemTimelineItem")



@_attrs_define
class SearchTransparencyResponse200DisputesDataItemTimelineItem:
    """ 
        Attributes:
            kind (SearchTransparencyResponse200DisputesDataItemTimelineItemKind):
            at (str):
            revision (int | None):
            outcome_type (SearchTransparencyResponse200DisputesDataItemTimelineItemOutcomeType):
            outcome_key (None | str):
            outcome_label (None | str):
            value (None | str):
            unit (None | str):
            resolved_by (None | SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType1 |
                SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType2Type1 |
                SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType3Type1):
            status (None | SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType1 |
                SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType2Type1 |
                SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType3Type1):
            season (None | SearchTransparencyResponse200DisputesDataItemTimelineItemSeasonType0):
     """

    kind: SearchTransparencyResponse200DisputesDataItemTimelineItemKind
    at: str
    revision: int | None
    outcome_type: SearchTransparencyResponse200DisputesDataItemTimelineItemOutcomeType
    outcome_key: None | str
    outcome_label: None | str
    value: None | str
    unit: None | str
    resolved_by: None | SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType1 | SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType2Type1 | SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType3Type1
    status: None | SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType1 | SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType2Type1 | SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType3Type1
    season: None | SearchTransparencyResponse200DisputesDataItemTimelineItemSeasonType0





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_transparency_response_200_disputes_data_item_timeline_item_season_type_0 import SearchTransparencyResponse200DisputesDataItemTimelineItemSeasonType0 # noqa: PLC0415
        kind = self.kind.value

        at = self.at

        revision: int | None
        revision = self.revision

        outcome_type = self.outcome_type.value

        outcome_key: None | str
        outcome_key = self.outcome_key

        outcome_label: None | str
        outcome_label = self.outcome_label

        value: None | str
        value = self.value

        unit: None | str
        unit = self.unit

        resolved_by: None | str
        if isinstance(self.resolved_by, SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType1):
            resolved_by = self.resolved_by.value
        elif isinstance(self.resolved_by, SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType2Type1):
            resolved_by = self.resolved_by.value
        elif isinstance(self.resolved_by, SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType3Type1):
            resolved_by = self.resolved_by.value
        else:
            resolved_by = self.resolved_by

        status: None | str
        if isinstance(self.status, SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType1):
            status = self.status.value
        elif isinstance(self.status, SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType2Type1):
            status = self.status.value
        elif isinstance(self.status, SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType3Type1):
            status = self.status.value
        else:
            status = self.status

        season: dict[str, Any] | None
        if isinstance(self.season, SearchTransparencyResponse200DisputesDataItemTimelineItemSeasonType0):
            season = self.season.to_dict()
        else:
            season = self.season


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
            "at": at,
            "revision": revision,
            "outcome_type": outcome_type,
            "outcome_key": outcome_key,
            "outcome_label": outcome_label,
            "value": value,
            "unit": unit,
            "resolved_by": resolved_by,
            "status": status,
            "season": season,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_transparency_response_200_disputes_data_item_timeline_item_season_type_0 import SearchTransparencyResponse200DisputesDataItemTimelineItemSeasonType0 # noqa: PLC0415
        d = dict(src_dict)
        kind = SearchTransparencyResponse200DisputesDataItemTimelineItemKind(d.pop("kind"))




        at = d.pop("at")

        def _parse_revision(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        revision = _parse_revision(d.pop("revision"))


        outcome_type = SearchTransparencyResponse200DisputesDataItemTimelineItemOutcomeType(d.pop("outcome_type"))




        def _parse_outcome_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        outcome_key = _parse_outcome_key(d.pop("outcome_key"))


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


        def _parse_resolved_by(data: object) -> None | SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType1 | SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType2Type1 | SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType3Type1:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_by_type_1 = SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType1(data)



                return resolved_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_by_type_2_type_1 = SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType2Type1(data)



                return resolved_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_by_type_3_type_1 = SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType3Type1(data)



                return resolved_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType1 | SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType2Type1 | SearchTransparencyResponse200DisputesDataItemTimelineItemResolvedByType3Type1, data)

        resolved_by = _parse_resolved_by(d.pop("resolved_by"))


        def _parse_status(data: object) -> None | SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType1 | SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType2Type1 | SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType3Type1:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType1(data)



                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType2Type1(data)



                return status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType3Type1(data)



                return status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType1 | SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType2Type1 | SearchTransparencyResponse200DisputesDataItemTimelineItemStatusType3Type1, data)

        status = _parse_status(d.pop("status"))


        def _parse_season(data: object) -> None | SearchTransparencyResponse200DisputesDataItemTimelineItemSeasonType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                season_type_0 = SearchTransparencyResponse200DisputesDataItemTimelineItemSeasonType0.from_dict(data)



                return season_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchTransparencyResponse200DisputesDataItemTimelineItemSeasonType0, data)

        season = _parse_season(d.pop("season"))


        search_transparency_response_200_disputes_data_item_timeline_item = cls(
            kind=kind,
            at=at,
            revision=revision,
            outcome_type=outcome_type,
            outcome_key=outcome_key,
            outcome_label=outcome_label,
            value=value,
            unit=unit,
            resolved_by=resolved_by,
            status=status,
            season=season,
        )

        return search_transparency_response_200_disputes_data_item_timeline_item

