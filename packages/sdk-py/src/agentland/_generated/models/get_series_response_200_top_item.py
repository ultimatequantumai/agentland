from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_series_response_200_top_item_agent import GetSeriesResponse200TopItemAgent
  from ..models.get_series_response_200_top_item_points_item import GetSeriesResponse200TopItemPointsItem





T = TypeVar("T", bound="GetSeriesResponse200TopItem")



@_attrs_define
class GetSeriesResponse200TopItem:
    """ 
        Attributes:
            agent (GetSeriesResponse200TopItemAgent):
            running_edge (float):
            points (list[GetSeriesResponse200TopItemPointsItem]):
     """

    agent: GetSeriesResponse200TopItemAgent
    running_edge: float
    points: list[GetSeriesResponse200TopItemPointsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_series_response_200_top_item_agent import GetSeriesResponse200TopItemAgent # noqa: PLC0415
        from ..models.get_series_response_200_top_item_points_item import GetSeriesResponse200TopItemPointsItem # noqa: PLC0415
        agent = self.agent.to_dict()

        running_edge = self.running_edge

        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "agent": agent,
            "running_edge": running_edge,
            "points": points,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_series_response_200_top_item_agent import GetSeriesResponse200TopItemAgent # noqa: PLC0415
        from ..models.get_series_response_200_top_item_points_item import GetSeriesResponse200TopItemPointsItem # noqa: PLC0415
        d = dict(src_dict)
        agent = GetSeriesResponse200TopItemAgent.from_dict(d.pop("agent"))




        running_edge = d.pop("running_edge")

        points = []
        _points = d.pop("points")
        for points_item_data in (_points):
            points_item = GetSeriesResponse200TopItemPointsItem.from_dict(points_item_data)



            points.append(points_item)


        get_series_response_200_top_item = cls(
            agent=agent,
            running_edge=running_edge,
            points=points,
        )

        return get_series_response_200_top_item

