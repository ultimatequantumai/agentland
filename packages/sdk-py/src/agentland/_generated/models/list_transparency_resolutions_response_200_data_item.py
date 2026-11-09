from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_transparency_resolutions_response_200_data_item_kind import ListTransparencyResolutionsResponse200DataItemKind
from ..models.list_transparency_resolutions_response_200_data_item_outcome_type import ListTransparencyResolutionsResponse200DataItemOutcomeType
from ..models.list_transparency_resolutions_response_200_data_item_resolved_by_type_1 import ListTransparencyResolutionsResponse200DataItemResolvedByType1
from ..models.list_transparency_resolutions_response_200_data_item_resolved_by_type_2_type_1 import ListTransparencyResolutionsResponse200DataItemResolvedByType2Type1
from ..models.list_transparency_resolutions_response_200_data_item_resolved_by_type_3_type_1 import ListTransparencyResolutionsResponse200DataItemResolvedByType3Type1
from ..models.list_transparency_resolutions_response_200_data_item_void_by_type_1 import ListTransparencyResolutionsResponse200DataItemVoidByType1
from ..models.list_transparency_resolutions_response_200_data_item_void_by_type_2_type_1 import ListTransparencyResolutionsResponse200DataItemVoidByType2Type1
from ..models.list_transparency_resolutions_response_200_data_item_void_by_type_3_type_1 import ListTransparencyResolutionsResponse200DataItemVoidByType3Type1
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.list_transparency_resolutions_response_200_data_item_question import ListTransparencyResolutionsResponse200DataItemQuestion





T = TypeVar("T", bound="ListTransparencyResolutionsResponse200DataItem")



@_attrs_define
class ListTransparencyResolutionsResponse200DataItem:
    """ 
        Attributes:
            kind (ListTransparencyResolutionsResponse200DataItemKind):
            question (ListTransparencyResolutionsResponse200DataItemQuestion):
            revision (int | None):
            outcome_type (ListTransparencyResolutionsResponse200DataItemOutcomeType):
            outcome_key (None | str):
            outcome_label (None | str):
            value (None | str):
            unit (None | str):
            resolved_by (ListTransparencyResolutionsResponse200DataItemResolvedByType1 |
                ListTransparencyResolutionsResponse200DataItemResolvedByType2Type1 |
                ListTransparencyResolutionsResponse200DataItemResolvedByType3Type1 | None):
            resolution_known_at (None | str):
            at (str):
            void_by (ListTransparencyResolutionsResponse200DataItemVoidByType1 |
                ListTransparencyResolutionsResponse200DataItemVoidByType2Type1 |
                ListTransparencyResolutionsResponse200DataItemVoidByType3Type1 | None):
            resolution_source_url (str):
            source_market_url (None | str):
            dispute_ids (list[UUID]):
     """

    kind: ListTransparencyResolutionsResponse200DataItemKind
    question: ListTransparencyResolutionsResponse200DataItemQuestion
    revision: int | None
    outcome_type: ListTransparencyResolutionsResponse200DataItemOutcomeType
    outcome_key: None | str
    outcome_label: None | str
    value: None | str
    unit: None | str
    resolved_by: ListTransparencyResolutionsResponse200DataItemResolvedByType1 | ListTransparencyResolutionsResponse200DataItemResolvedByType2Type1 | ListTransparencyResolutionsResponse200DataItemResolvedByType3Type1 | None
    resolution_known_at: None | str
    at: str
    void_by: ListTransparencyResolutionsResponse200DataItemVoidByType1 | ListTransparencyResolutionsResponse200DataItemVoidByType2Type1 | ListTransparencyResolutionsResponse200DataItemVoidByType3Type1 | None
    resolution_source_url: str
    source_market_url: None | str
    dispute_ids: list[UUID]





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_transparency_resolutions_response_200_data_item_question import ListTransparencyResolutionsResponse200DataItemQuestion # noqa: PLC0415
        kind = self.kind.value

        question = self.question.to_dict()

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
        if isinstance(self.resolved_by, ListTransparencyResolutionsResponse200DataItemResolvedByType1):
            resolved_by = self.resolved_by.value
        elif isinstance(self.resolved_by, ListTransparencyResolutionsResponse200DataItemResolvedByType2Type1):
            resolved_by = self.resolved_by.value
        elif isinstance(self.resolved_by, ListTransparencyResolutionsResponse200DataItemResolvedByType3Type1):
            resolved_by = self.resolved_by.value
        else:
            resolved_by = self.resolved_by

        resolution_known_at: None | str
        resolution_known_at = self.resolution_known_at

        at = self.at

        void_by: None | str
        if isinstance(self.void_by, ListTransparencyResolutionsResponse200DataItemVoidByType1):
            void_by = self.void_by.value
        elif isinstance(self.void_by, ListTransparencyResolutionsResponse200DataItemVoidByType2Type1):
            void_by = self.void_by.value
        elif isinstance(self.void_by, ListTransparencyResolutionsResponse200DataItemVoidByType3Type1):
            void_by = self.void_by.value
        else:
            void_by = self.void_by

        resolution_source_url = self.resolution_source_url

        source_market_url: None | str
        source_market_url = self.source_market_url

        dispute_ids = []
        for dispute_ids_item_data in self.dispute_ids:
            dispute_ids_item = str(dispute_ids_item_data)
            dispute_ids.append(dispute_ids_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
            "question": question,
            "revision": revision,
            "outcome_type": outcome_type,
            "outcome_key": outcome_key,
            "outcome_label": outcome_label,
            "value": value,
            "unit": unit,
            "resolved_by": resolved_by,
            "resolution_known_at": resolution_known_at,
            "at": at,
            "void_by": void_by,
            "resolution_source_url": resolution_source_url,
            "source_market_url": source_market_url,
            "dispute_ids": dispute_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_transparency_resolutions_response_200_data_item_question import ListTransparencyResolutionsResponse200DataItemQuestion # noqa: PLC0415
        d = dict(src_dict)
        kind = ListTransparencyResolutionsResponse200DataItemKind(d.pop("kind"))




        question = ListTransparencyResolutionsResponse200DataItemQuestion.from_dict(d.pop("question"))




        def _parse_revision(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        revision = _parse_revision(d.pop("revision"))


        outcome_type = ListTransparencyResolutionsResponse200DataItemOutcomeType(d.pop("outcome_type"))




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


        def _parse_resolved_by(data: object) -> ListTransparencyResolutionsResponse200DataItemResolvedByType1 | ListTransparencyResolutionsResponse200DataItemResolvedByType2Type1 | ListTransparencyResolutionsResponse200DataItemResolvedByType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_by_type_1 = ListTransparencyResolutionsResponse200DataItemResolvedByType1(data)



                return resolved_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_by_type_2_type_1 = ListTransparencyResolutionsResponse200DataItemResolvedByType2Type1(data)



                return resolved_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_by_type_3_type_1 = ListTransparencyResolutionsResponse200DataItemResolvedByType3Type1(data)



                return resolved_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListTransparencyResolutionsResponse200DataItemResolvedByType1 | ListTransparencyResolutionsResponse200DataItemResolvedByType2Type1 | ListTransparencyResolutionsResponse200DataItemResolvedByType3Type1 | None, data)

        resolved_by = _parse_resolved_by(d.pop("resolved_by"))


        def _parse_resolution_known_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolution_known_at = _parse_resolution_known_at(d.pop("resolution_known_at"))


        at = d.pop("at")

        def _parse_void_by(data: object) -> ListTransparencyResolutionsResponse200DataItemVoidByType1 | ListTransparencyResolutionsResponse200DataItemVoidByType2Type1 | ListTransparencyResolutionsResponse200DataItemVoidByType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                void_by_type_1 = ListTransparencyResolutionsResponse200DataItemVoidByType1(data)



                return void_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                void_by_type_2_type_1 = ListTransparencyResolutionsResponse200DataItemVoidByType2Type1(data)



                return void_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                void_by_type_3_type_1 = ListTransparencyResolutionsResponse200DataItemVoidByType3Type1(data)



                return void_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListTransparencyResolutionsResponse200DataItemVoidByType1 | ListTransparencyResolutionsResponse200DataItemVoidByType2Type1 | ListTransparencyResolutionsResponse200DataItemVoidByType3Type1 | None, data)

        void_by = _parse_void_by(d.pop("void_by"))


        resolution_source_url = d.pop("resolution_source_url")

        def _parse_source_market_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_market_url = _parse_source_market_url(d.pop("source_market_url"))


        dispute_ids = []
        _dispute_ids = d.pop("dispute_ids")
        for dispute_ids_item_data in (_dispute_ids):
            dispute_ids_item = UUID(dispute_ids_item_data)



            dispute_ids.append(dispute_ids_item)


        list_transparency_resolutions_response_200_data_item = cls(
            kind=kind,
            question=question,
            revision=revision,
            outcome_type=outcome_type,
            outcome_key=outcome_key,
            outcome_label=outcome_label,
            value=value,
            unit=unit,
            resolved_by=resolved_by,
            resolution_known_at=resolution_known_at,
            at=at,
            void_by=void_by,
            resolution_source_url=resolution_source_url,
            source_market_url=source_market_url,
            dispute_ids=dispute_ids,
        )

        return list_transparency_resolutions_response_200_data_item

