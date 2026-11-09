from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.search_transparency_response_200_disputes_data_item import SearchTransparencyResponse200DisputesDataItem





T = TypeVar("T", bound="SearchTransparencyResponse200Disputes")



@_attrs_define
class SearchTransparencyResponse200Disputes:
    """ 
        Attributes:
            total (int):
            data (list[SearchTransparencyResponse200DisputesDataItem]):
     """

    total: int
    data: list[SearchTransparencyResponse200DisputesDataItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_transparency_response_200_disputes_data_item import SearchTransparencyResponse200DisputesDataItem # noqa: PLC0415
        total = self.total

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "total": total,
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_transparency_response_200_disputes_data_item import SearchTransparencyResponse200DisputesDataItem # noqa: PLC0415
        d = dict(src_dict)
        total = d.pop("total")

        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = SearchTransparencyResponse200DisputesDataItem.from_dict(data_item_data)



            data.append(data_item)


        search_transparency_response_200_disputes = cls(
            total=total,
            data=data,
        )

        return search_transparency_response_200_disputes

