from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.list_public_memory_response_200_data_item import ListPublicMemoryResponse200DataItem





T = TypeVar("T", bound="ListPublicMemoryResponse200")



@_attrs_define
class ListPublicMemoryResponse200:
    """ 
        Attributes:
            data (list[ListPublicMemoryResponse200DataItem]):
            next_cursor (None | str):
     """

    data: list[ListPublicMemoryResponse200DataItem]
    next_cursor: None | str





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_public_memory_response_200_data_item import ListPublicMemoryResponse200DataItem # noqa: PLC0415
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        next_cursor: None | str
        next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
            "next_cursor": next_cursor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_public_memory_response_200_data_item import ListPublicMemoryResponse200DataItem # noqa: PLC0415
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = ListPublicMemoryResponse200DataItem.from_dict(data_item_data)



            data.append(data_item)


        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))


        list_public_memory_response_200 = cls(
            data=data,
            next_cursor=next_cursor,
        )

        return list_public_memory_response_200

