from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_question_disputes_response_200_data_item_question_outcome_type import ListQuestionDisputesResponse200DataItemQuestionOutcomeType
from ..models.list_question_disputes_response_200_data_item_question_status import ListQuestionDisputesResponse200DataItemQuestionStatus
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ListQuestionDisputesResponse200DataItemQuestion")



@_attrs_define
class ListQuestionDisputesResponse200DataItemQuestion:
    """ 
        Attributes:
            id (UUID):
            slug (str):
            title (str):
            source (str):
            resolution_source_url (str):
            source_market_url (None | str):
            status (ListQuestionDisputesResponse200DataItemQuestionStatus):
            outcome_type (ListQuestionDisputesResponse200DataItemQuestionOutcomeType):
            outcome_key (None | str):
            outcome_label (None | str):
            value (None | str):
            unit (None | str):
            revision (int | None):
     """

    id: UUID
    slug: str
    title: str
    source: str
    resolution_source_url: str
    source_market_url: None | str
    status: ListQuestionDisputesResponse200DataItemQuestionStatus
    outcome_type: ListQuestionDisputesResponse200DataItemQuestionOutcomeType
    outcome_key: None | str
    outcome_label: None | str
    value: None | str
    unit: None | str
    revision: int | None





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        slug = self.slug

        title = self.title

        source = self.source

        resolution_source_url = self.resolution_source_url

        source_market_url: None | str
        source_market_url = self.source_market_url

        status = self.status.value

        outcome_type = self.outcome_type.value

        outcome_key: None | str
        outcome_key = self.outcome_key

        outcome_label: None | str
        outcome_label = self.outcome_label

        value: None | str
        value = self.value

        unit: None | str
        unit = self.unit

        revision: int | None
        revision = self.revision


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "slug": slug,
            "title": title,
            "source": source,
            "resolution_source_url": resolution_source_url,
            "source_market_url": source_market_url,
            "status": status,
            "outcome_type": outcome_type,
            "outcome_key": outcome_key,
            "outcome_label": outcome_label,
            "value": value,
            "unit": unit,
            "revision": revision,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        slug = d.pop("slug")

        title = d.pop("title")

        source = d.pop("source")

        resolution_source_url = d.pop("resolution_source_url")

        def _parse_source_market_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_market_url = _parse_source_market_url(d.pop("source_market_url"))


        status = ListQuestionDisputesResponse200DataItemQuestionStatus(d.pop("status"))




        outcome_type = ListQuestionDisputesResponse200DataItemQuestionOutcomeType(d.pop("outcome_type"))




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


        def _parse_revision(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        revision = _parse_revision(d.pop("revision"))


        list_question_disputes_response_200_data_item_question = cls(
            id=id,
            slug=slug,
            title=title,
            source=source,
            resolution_source_url=resolution_source_url,
            source_market_url=source_market_url,
            status=status,
            outcome_type=outcome_type,
            outcome_key=outcome_key,
            outcome_label=outcome_label,
            value=value,
            unit=unit,
            revision=revision,
        )

        return list_question_disputes_response_200_data_item_question

