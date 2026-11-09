from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_operator_moderation_overview_response_200_data_item_actions_item import GetOperatorModerationOverviewResponse200DataItemActionsItem
  from ..models.get_operator_moderation_overview_response_200_data_item_agent import GetOperatorModerationOverviewResponse200DataItemAgent





T = TypeVar("T", bound="GetOperatorModerationOverviewResponse200DataItem")



@_attrs_define
class GetOperatorModerationOverviewResponse200DataItem:
    """ 
        Attributes:
            agent (GetOperatorModerationOverviewResponse200DataItemAgent):
            actions (list[GetOperatorModerationOverviewResponse200DataItemActionsItem]):
     """

    agent: GetOperatorModerationOverviewResponse200DataItemAgent
    actions: list[GetOperatorModerationOverviewResponse200DataItemActionsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_operator_moderation_overview_response_200_data_item_actions_item import GetOperatorModerationOverviewResponse200DataItemActionsItem # noqa: PLC0415
        from ..models.get_operator_moderation_overview_response_200_data_item_agent import GetOperatorModerationOverviewResponse200DataItemAgent # noqa: PLC0415
        agent = self.agent.to_dict()

        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "agent": agent,
            "actions": actions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_operator_moderation_overview_response_200_data_item_actions_item import GetOperatorModerationOverviewResponse200DataItemActionsItem # noqa: PLC0415
        from ..models.get_operator_moderation_overview_response_200_data_item_agent import GetOperatorModerationOverviewResponse200DataItemAgent # noqa: PLC0415
        d = dict(src_dict)
        agent = GetOperatorModerationOverviewResponse200DataItemAgent.from_dict(d.pop("agent"))




        actions = []
        _actions = d.pop("actions")
        for actions_item_data in (_actions):
            actions_item = GetOperatorModerationOverviewResponse200DataItemActionsItem.from_dict(actions_item_data)



            actions.append(actions_item)


        get_operator_moderation_overview_response_200_data_item = cls(
            agent=agent,
            actions=actions,
        )

        return get_operator_moderation_overview_response_200_data_item

