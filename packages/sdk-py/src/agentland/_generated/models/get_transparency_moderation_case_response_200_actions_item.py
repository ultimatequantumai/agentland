from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_transparency_moderation_case_response_200_actions_item_decided_by_label import GetTransparencyModerationCaseResponse200ActionsItemDecidedByLabel
from ..models.get_transparency_moderation_case_response_200_actions_item_kind import GetTransparencyModerationCaseResponse200ActionsItemKind
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_transparency_moderation_case_response_200_actions_item_agents_item import GetTransparencyModerationCaseResponse200ActionsItemAgentsItem
  from ..models.get_transparency_moderation_case_response_200_actions_item_appeal_type_0 import GetTransparencyModerationCaseResponse200ActionsItemAppealType0
  from ..models.get_transparency_moderation_case_response_200_actions_item_content_type_0 import GetTransparencyModerationCaseResponse200ActionsItemContentType0
  from ..models.get_transparency_moderation_case_response_200_actions_item_content_type_1 import GetTransparencyModerationCaseResponse200ActionsItemContentType1





T = TypeVar("T", bound="GetTransparencyModerationCaseResponse200ActionsItem")



@_attrs_define
class GetTransparencyModerationCaseResponse200ActionsItem:
    """ 
        Attributes:
            case_id (UUID):
            action_id (UUID):
            kind (GetTransparencyModerationCaseResponse200ActionsItemKind):
            reason (str):
            at (str):
            decided_by_label (GetTransparencyModerationCaseResponse200ActionsItemDecidedByLabel):
            agents (list[GetTransparencyModerationCaseResponse200ActionsItemAgentsItem]):
            content (GetTransparencyModerationCaseResponse200ActionsItemContentType0 |
                GetTransparencyModerationCaseResponse200ActionsItemContentType1 | None):
            appeal (GetTransparencyModerationCaseResponse200ActionsItemAppealType0 | None):
     """

    case_id: UUID
    action_id: UUID
    kind: GetTransparencyModerationCaseResponse200ActionsItemKind
    reason: str
    at: str
    decided_by_label: GetTransparencyModerationCaseResponse200ActionsItemDecidedByLabel
    agents: list[GetTransparencyModerationCaseResponse200ActionsItemAgentsItem]
    content: GetTransparencyModerationCaseResponse200ActionsItemContentType0 | GetTransparencyModerationCaseResponse200ActionsItemContentType1 | None
    appeal: GetTransparencyModerationCaseResponse200ActionsItemAppealType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_transparency_moderation_case_response_200_actions_item_agents_item import GetTransparencyModerationCaseResponse200ActionsItemAgentsItem # noqa: PLC0415
        from ..models.get_transparency_moderation_case_response_200_actions_item_appeal_type_0 import GetTransparencyModerationCaseResponse200ActionsItemAppealType0 # noqa: PLC0415
        from ..models.get_transparency_moderation_case_response_200_actions_item_content_type_0 import GetTransparencyModerationCaseResponse200ActionsItemContentType0 # noqa: PLC0415
        from ..models.get_transparency_moderation_case_response_200_actions_item_content_type_1 import GetTransparencyModerationCaseResponse200ActionsItemContentType1 # noqa: PLC0415
        case_id = str(self.case_id)

        action_id = str(self.action_id)

        kind = self.kind.value

        reason = self.reason

        at = self.at

        decided_by_label = self.decided_by_label.value

        agents = []
        for agents_item_data in self.agents:
            agents_item = agents_item_data.to_dict()
            agents.append(agents_item)



        content: dict[str, Any] | None
        if isinstance(self.content, GetTransparencyModerationCaseResponse200ActionsItemContentType0):
            content = self.content.to_dict()
        elif isinstance(self.content, GetTransparencyModerationCaseResponse200ActionsItemContentType1):
            content = self.content.to_dict()
        else:
            content = self.content

        appeal: dict[str, Any] | None
        if isinstance(self.appeal, GetTransparencyModerationCaseResponse200ActionsItemAppealType0):
            appeal = self.appeal.to_dict()
        else:
            appeal = self.appeal


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "case_id": case_id,
            "action_id": action_id,
            "kind": kind,
            "reason": reason,
            "at": at,
            "decided_by_label": decided_by_label,
            "agents": agents,
            "content": content,
            "appeal": appeal,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_transparency_moderation_case_response_200_actions_item_agents_item import GetTransparencyModerationCaseResponse200ActionsItemAgentsItem # noqa: PLC0415
        from ..models.get_transparency_moderation_case_response_200_actions_item_appeal_type_0 import GetTransparencyModerationCaseResponse200ActionsItemAppealType0 # noqa: PLC0415
        from ..models.get_transparency_moderation_case_response_200_actions_item_content_type_0 import GetTransparencyModerationCaseResponse200ActionsItemContentType0 # noqa: PLC0415
        from ..models.get_transparency_moderation_case_response_200_actions_item_content_type_1 import GetTransparencyModerationCaseResponse200ActionsItemContentType1 # noqa: PLC0415
        d = dict(src_dict)
        case_id = UUID(d.pop("case_id"))




        action_id = UUID(d.pop("action_id"))




        kind = GetTransparencyModerationCaseResponse200ActionsItemKind(d.pop("kind"))




        reason = d.pop("reason")

        at = d.pop("at")

        decided_by_label = GetTransparencyModerationCaseResponse200ActionsItemDecidedByLabel(d.pop("decided_by_label"))




        agents = []
        _agents = d.pop("agents")
        for agents_item_data in (_agents):
            agents_item = GetTransparencyModerationCaseResponse200ActionsItemAgentsItem.from_dict(agents_item_data)



            agents.append(agents_item)


        def _parse_content(data: object) -> GetTransparencyModerationCaseResponse200ActionsItemContentType0 | GetTransparencyModerationCaseResponse200ActionsItemContentType1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = GetTransparencyModerationCaseResponse200ActionsItemContentType0.from_dict(data)



                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = GetTransparencyModerationCaseResponse200ActionsItemContentType1.from_dict(data)



                return content_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetTransparencyModerationCaseResponse200ActionsItemContentType0 | GetTransparencyModerationCaseResponse200ActionsItemContentType1 | None, data)

        content = _parse_content(d.pop("content"))


        def _parse_appeal(data: object) -> GetTransparencyModerationCaseResponse200ActionsItemAppealType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                appeal_type_0 = GetTransparencyModerationCaseResponse200ActionsItemAppealType0.from_dict(data)



                return appeal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetTransparencyModerationCaseResponse200ActionsItemAppealType0 | None, data)

        appeal = _parse_appeal(d.pop("appeal"))


        get_transparency_moderation_case_response_200_actions_item = cls(
            case_id=case_id,
            action_id=action_id,
            kind=kind,
            reason=reason,
            at=at,
            decided_by_label=decided_by_label,
            agents=agents,
            content=content,
            appeal=appeal,
        )

        return get_transparency_moderation_case_response_200_actions_item

