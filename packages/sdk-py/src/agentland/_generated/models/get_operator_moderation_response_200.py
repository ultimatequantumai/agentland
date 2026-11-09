from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_operator_moderation_response_200_agent import GetOperatorModerationResponse200Agent
  from ..models.get_operator_moderation_response_200_data_item import GetOperatorModerationResponse200DataItem





T = TypeVar("T", bound="GetOperatorModerationResponse200")



@_attrs_define
class GetOperatorModerationResponse200:
    """ 
        Attributes:
            agent (GetOperatorModerationResponse200Agent):
            data (list[GetOperatorModerationResponse200DataItem]):
     """

    agent: GetOperatorModerationResponse200Agent
    data: list[GetOperatorModerationResponse200DataItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_operator_moderation_response_200_agent import GetOperatorModerationResponse200Agent # noqa: PLC0415
        from ..models.get_operator_moderation_response_200_data_item import GetOperatorModerationResponse200DataItem # noqa: PLC0415
        agent = self.agent.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "agent": agent,
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_operator_moderation_response_200_agent import GetOperatorModerationResponse200Agent # noqa: PLC0415
        from ..models.get_operator_moderation_response_200_data_item import GetOperatorModerationResponse200DataItem # noqa: PLC0415
        d = dict(src_dict)
        agent = GetOperatorModerationResponse200Agent.from_dict(d.pop("agent"))




        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = GetOperatorModerationResponse200DataItem.from_dict(data_item_data)



            data.append(data_item)


        get_operator_moderation_response_200 = cls(
            agent=agent,
            data=data,
        )

        return get_operator_moderation_response_200

