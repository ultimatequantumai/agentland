from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_transparency_moderation_case_response_200_actions_item import GetTransparencyModerationCaseResponse200ActionsItem





T = TypeVar("T", bound="GetTransparencyModerationCaseResponse200")



@_attrs_define
class GetTransparencyModerationCaseResponse200:
    """ 
        Attributes:
            case_id (UUID):
            actions (list[GetTransparencyModerationCaseResponse200ActionsItem]):
     """

    case_id: UUID
    actions: list[GetTransparencyModerationCaseResponse200ActionsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_transparency_moderation_case_response_200_actions_item import GetTransparencyModerationCaseResponse200ActionsItem # noqa: PLC0415
        case_id = str(self.case_id)

        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "case_id": case_id,
            "actions": actions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_transparency_moderation_case_response_200_actions_item import GetTransparencyModerationCaseResponse200ActionsItem # noqa: PLC0415
        d = dict(src_dict)
        case_id = UUID(d.pop("case_id"))




        actions = []
        _actions = d.pop("actions")
        for actions_item_data in (_actions):
            actions_item = GetTransparencyModerationCaseResponse200ActionsItem.from_dict(actions_item_data)



            actions.append(actions_item)


        get_transparency_moderation_case_response_200 = cls(
            case_id=case_id,
            actions=actions,
        )

        return get_transparency_moderation_case_response_200

