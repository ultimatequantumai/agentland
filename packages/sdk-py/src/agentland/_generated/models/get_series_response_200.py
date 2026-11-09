from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_series_response_200_instances_item import GetSeriesResponse200InstancesItem
  from ..models.get_series_response_200_series import GetSeriesResponse200Series
  from ..models.get_series_response_200_top_item import GetSeriesResponse200TopItem





T = TypeVar("T", bound="GetSeriesResponse200")



@_attrs_define
class GetSeriesResponse200:
    """ 
        Attributes:
            series (GetSeriesResponse200Series):
            instances (list[GetSeriesResponse200InstancesItem]):
            top (list[GetSeriesResponse200TopItem]):
     """

    series: GetSeriesResponse200Series
    instances: list[GetSeriesResponse200InstancesItem]
    top: list[GetSeriesResponse200TopItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_series_response_200_instances_item import GetSeriesResponse200InstancesItem # noqa: PLC0415
        from ..models.get_series_response_200_series import GetSeriesResponse200Series # noqa: PLC0415
        from ..models.get_series_response_200_top_item import GetSeriesResponse200TopItem # noqa: PLC0415
        series = self.series.to_dict()

        instances = []
        for instances_item_data in self.instances:
            instances_item = instances_item_data.to_dict()
            instances.append(instances_item)



        top = []
        for top_item_data in self.top:
            top_item = top_item_data.to_dict()
            top.append(top_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "series": series,
            "instances": instances,
            "top": top,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_series_response_200_instances_item import GetSeriesResponse200InstancesItem # noqa: PLC0415
        from ..models.get_series_response_200_series import GetSeriesResponse200Series # noqa: PLC0415
        from ..models.get_series_response_200_top_item import GetSeriesResponse200TopItem # noqa: PLC0415
        d = dict(src_dict)
        series = GetSeriesResponse200Series.from_dict(d.pop("series"))




        instances = []
        _instances = d.pop("instances")
        for instances_item_data in (_instances):
            instances_item = GetSeriesResponse200InstancesItem.from_dict(instances_item_data)



            instances.append(instances_item)


        top = []
        _top = d.pop("top")
        for top_item_data in (_top):
            top_item = GetSeriesResponse200TopItem.from_dict(top_item_data)



            top.append(top_item)


        get_series_response_200 = cls(
            series=series,
            instances=instances,
            top=top,
        )

        return get_series_response_200

