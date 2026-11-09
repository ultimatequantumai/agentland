from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.search_memory_response_200_data_item_type_0 import SearchMemoryResponse200DataItemType0
  from ..models.search_memory_response_200_data_item_type_1 import SearchMemoryResponse200DataItemType1





T = TypeVar("T", bound="SearchMemoryResponse200")



@_attrs_define
class SearchMemoryResponse200:
    """ 
        Attributes:
            data (list[SearchMemoryResponse200DataItemType0 | SearchMemoryResponse200DataItemType1]):
            next_cursor (None | str):
     """

    data: list[SearchMemoryResponse200DataItemType0 | SearchMemoryResponse200DataItemType1]
    next_cursor: None | str





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_memory_response_200_data_item_type_0 import SearchMemoryResponse200DataItemType0 # noqa: PLC0415
        from ..models.search_memory_response_200_data_item_type_1 import SearchMemoryResponse200DataItemType1 # noqa: PLC0415
        data = []
        for data_item_data in self.data:
            data_item: dict[str, Any]
            if isinstance(data_item_data, SearchMemoryResponse200DataItemType0):
                data_item = data_item_data.to_dict()
            else:
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
        from ..models.search_memory_response_200_data_item_type_0 import SearchMemoryResponse200DataItemType0 # noqa: PLC0415
        from ..models.search_memory_response_200_data_item_type_1 import SearchMemoryResponse200DataItemType1 # noqa: PLC0415
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            def _parse_data_item(data: object) -> SearchMemoryResponse200DataItemType0 | SearchMemoryResponse200DataItemType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_0 = SearchMemoryResponse200DataItemType0.from_dict(data)



                    return data_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                data_item_type_1 = SearchMemoryResponse200DataItemType1.from_dict(data)



                return data_item_type_1

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)


        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))


        search_memory_response_200 = cls(
            data=data,
            next_cursor=next_cursor,
        )

        return search_memory_response_200

