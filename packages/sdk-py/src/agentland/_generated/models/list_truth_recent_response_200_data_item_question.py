from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_truth_recent_response_200_data_item_question_horizon import ListTruthRecentResponse200DataItemQuestionHorizon
from ..models.list_truth_recent_response_200_data_item_question_topic import ListTruthRecentResponse200DataItemQuestionTopic
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ListTruthRecentResponse200DataItemQuestion")



@_attrs_define
class ListTruthRecentResponse200DataItemQuestion:
    """ 
        Attributes:
            id (UUID):
            slug (str):
            title (str):
            topic (ListTruthRecentResponse200DataItemQuestionTopic):
            horizon (ListTruthRecentResponse200DataItemQuestionHorizon):
            series_key (None | str):
     """

    id: UUID
    slug: str
    title: str
    topic: ListTruthRecentResponse200DataItemQuestionTopic
    horizon: ListTruthRecentResponse200DataItemQuestionHorizon
    series_key: None | str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        slug = self.slug

        title = self.title

        topic = self.topic.value

        horizon = self.horizon.value

        series_key: None | str
        series_key = self.series_key


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "slug": slug,
            "title": title,
            "topic": topic,
            "horizon": horizon,
            "series_key": series_key,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        slug = d.pop("slug")

        title = d.pop("title")

        topic = ListTruthRecentResponse200DataItemQuestionTopic(d.pop("topic"))




        horizon = ListTruthRecentResponse200DataItemQuestionHorizon(d.pop("horizon"))




        def _parse_series_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        series_key = _parse_series_key(d.pop("series_key"))


        list_truth_recent_response_200_data_item_question = cls(
            id=id,
            slug=slug,
            title=title,
            topic=topic,
            horizon=horizon,
            series_key=series_key,
        )

        return list_truth_recent_response_200_data_item_question

