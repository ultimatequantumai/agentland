from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.poll_events_response_200_data_item import PollEventsResponse200DataItem





T = TypeVar("T", bound="PollEventsResponse200")



@_attrs_define
class PollEventsResponse200:
    """ 
        Attributes:
            data (list[PollEventsResponse200DataItem]):
            next_cursor (str):
     """

    data: list[PollEventsResponse200DataItem]
    next_cursor: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.poll_events_response_200_data_item import PollEventsResponse200DataItem # noqa: PLC0415
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
            "next_cursor": next_cursor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_events_response_200_data_item import PollEventsResponse200DataItem # noqa: PLC0415
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = PollEventsResponse200DataItem.from_dict(data_item_data)



            data.append(data_item)


        next_cursor = d.pop("next_cursor")

        poll_events_response_200 = cls(
            data=data,
            next_cursor=next_cursor,
        )

        return poll_events_response_200

