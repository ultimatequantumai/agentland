from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.search_transparency_response_200_moderation_data_item import SearchTransparencyResponse200ModerationDataItem





T = TypeVar("T", bound="SearchTransparencyResponse200Moderation")



@_attrs_define
class SearchTransparencyResponse200Moderation:
    """ 
        Attributes:
            total (int):
            data (list[SearchTransparencyResponse200ModerationDataItem]):
     """

    total: int
    data: list[SearchTransparencyResponse200ModerationDataItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_transparency_response_200_moderation_data_item import SearchTransparencyResponse200ModerationDataItem # noqa: PLC0415
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
        from ..models.search_transparency_response_200_moderation_data_item import SearchTransparencyResponse200ModerationDataItem # noqa: PLC0415
        d = dict(src_dict)
        total = d.pop("total")

        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = SearchTransparencyResponse200ModerationDataItem.from_dict(data_item_data)



            data.append(data_item)


        search_transparency_response_200_moderation = cls(
            total=total,
            data=data,
        )

        return search_transparency_response_200_moderation

