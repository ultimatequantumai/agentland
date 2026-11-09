from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_series_response_200_data_item_topic import ListSeriesResponse200DataItemTopic
from typing import cast






T = TypeVar("T", bound="ListSeriesResponse200DataItem")



@_attrs_define
class ListSeriesResponse200DataItem:
    """ 
        Attributes:
            series_key (str):
            source (str):
            cadence (None | str):
            topic (ListSeriesResponse200DataItemTopic):
            next_open_at (None | str):
     """

    series_key: str
    source: str
    cadence: None | str
    topic: ListSeriesResponse200DataItemTopic
    next_open_at: None | str





    def to_dict(self) -> dict[str, Any]:
        series_key = self.series_key

        source = self.source

        cadence: None | str
        cadence = self.cadence

        topic = self.topic.value

        next_open_at: None | str
        next_open_at = self.next_open_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "series_key": series_key,
            "source": source,
            "cadence": cadence,
            "topic": topic,
            "next_open_at": next_open_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        series_key = d.pop("series_key")

        source = d.pop("source")

        def _parse_cadence(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cadence = _parse_cadence(d.pop("cadence"))


        topic = ListSeriesResponse200DataItemTopic(d.pop("topic"))




        def _parse_next_open_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_open_at = _parse_next_open_at(d.pop("next_open_at"))


        list_series_response_200_data_item = cls(
            series_key=series_key,
            source=source,
            cadence=cadence,
            topic=topic,
            next_open_at=next_open_at,
        )

        return list_series_response_200_data_item

