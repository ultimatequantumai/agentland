from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.list_agent_resolved_response_200_calibration_type_0 import ListAgentResolvedResponse200CalibrationType0
  from ..models.list_agent_resolved_response_200_data_item import ListAgentResolvedResponse200DataItem





T = TypeVar("T", bound="ListAgentResolvedResponse200")



@_attrs_define
class ListAgentResolvedResponse200:
    """ 
        Attributes:
            data (list[ListAgentResolvedResponse200DataItem]):
            next_cursor (None | str):
            calibration (ListAgentResolvedResponse200CalibrationType0 | None):
     """

    data: list[ListAgentResolvedResponse200DataItem]
    next_cursor: None | str
    calibration: ListAgentResolvedResponse200CalibrationType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_agent_resolved_response_200_calibration_type_0 import ListAgentResolvedResponse200CalibrationType0 # noqa: PLC0415
        from ..models.list_agent_resolved_response_200_data_item import ListAgentResolvedResponse200DataItem # noqa: PLC0415
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        next_cursor: None | str
        next_cursor = self.next_cursor

        calibration: dict[str, Any] | None
        if isinstance(self.calibration, ListAgentResolvedResponse200CalibrationType0):
            calibration = self.calibration.to_dict()
        else:
            calibration = self.calibration


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
            "next_cursor": next_cursor,
            "calibration": calibration,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_agent_resolved_response_200_calibration_type_0 import ListAgentResolvedResponse200CalibrationType0 # noqa: PLC0415
        from ..models.list_agent_resolved_response_200_data_item import ListAgentResolvedResponse200DataItem # noqa: PLC0415
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = ListAgentResolvedResponse200DataItem.from_dict(data_item_data)



            data.append(data_item)


        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))


        def _parse_calibration(data: object) -> ListAgentResolvedResponse200CalibrationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                calibration_type_0 = ListAgentResolvedResponse200CalibrationType0.from_dict(data)



                return calibration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListAgentResolvedResponse200CalibrationType0 | None, data)

        calibration = _parse_calibration(d.pop("calibration"))


        list_agent_resolved_response_200 = cls(
            data=data,
            next_cursor=next_cursor,
            calibration=calibration,
        )

        return list_agent_resolved_response_200

