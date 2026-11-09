from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.list_transparency_sources_response_200_data_item import ListTransparencySourcesResponse200DataItem





T = TypeVar("T", bound="ListTransparencySourcesResponse200")



@_attrs_define
class ListTransparencySourcesResponse200:
    """ 
        Attributes:
            data (list[ListTransparencySourcesResponse200DataItem]):
     """

    data: list[ListTransparencySourcesResponse200DataItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_transparency_sources_response_200_data_item import ListTransparencySourcesResponse200DataItem # noqa: PLC0415
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_transparency_sources_response_200_data_item import ListTransparencySourcesResponse200DataItem # noqa: PLC0415
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = ListTransparencySourcesResponse200DataItem.from_dict(data_item_data)



            data.append(data_item)


        list_transparency_sources_response_200 = cls(
            data=data,
        )

        return list_transparency_sources_response_200

