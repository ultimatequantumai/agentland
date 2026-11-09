from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_daily_response_200_resolved_item_question_horizon import GetDailyResponse200ResolvedItemQuestionHorizon
from ..models.get_daily_response_200_resolved_item_question_topic import GetDailyResponse200ResolvedItemQuestionTopic
from typing import cast






T = TypeVar("T", bound="GetDailyResponse200ResolvedItemQuestion")



@_attrs_define
class GetDailyResponse200ResolvedItemQuestion:
    """ 
        Attributes:
            slug (str):
            title (str):
            horizon (GetDailyResponse200ResolvedItemQuestionHorizon):
            topic (GetDailyResponse200ResolvedItemQuestionTopic):
            source (str):
            resolution_source_url (str):
            market_url (None | str):
     """

    slug: str
    title: str
    horizon: GetDailyResponse200ResolvedItemQuestionHorizon
    topic: GetDailyResponse200ResolvedItemQuestionTopic
    source: str
    resolution_source_url: str
    market_url: None | str





    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        title = self.title

        horizon = self.horizon.value

        topic = self.topic.value

        source = self.source

        resolution_source_url = self.resolution_source_url

        market_url: None | str
        market_url = self.market_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "slug": slug,
            "title": title,
            "horizon": horizon,
            "topic": topic,
            "source": source,
            "resolution_source_url": resolution_source_url,
            "market_url": market_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        title = d.pop("title")

        horizon = GetDailyResponse200ResolvedItemQuestionHorizon(d.pop("horizon"))




        topic = GetDailyResponse200ResolvedItemQuestionTopic(d.pop("topic"))




        source = d.pop("source")

        resolution_source_url = d.pop("resolution_source_url")

        def _parse_market_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        market_url = _parse_market_url(d.pop("market_url"))


        get_daily_response_200_resolved_item_question = cls(
            slug=slug,
            title=title,
            horizon=horizon,
            topic=topic,
            source=source,
            resolution_source_url=resolution_source_url,
            market_url=market_url,
        )

        return get_daily_response_200_resolved_item_question

