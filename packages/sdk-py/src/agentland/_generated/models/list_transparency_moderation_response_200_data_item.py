from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_transparency_moderation_response_200_data_item_decided_by_label import ListTransparencyModerationResponse200DataItemDecidedByLabel
from ..models.list_transparency_moderation_response_200_data_item_kind import ListTransparencyModerationResponse200DataItemKind
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.list_transparency_moderation_response_200_data_item_agents_item import ListTransparencyModerationResponse200DataItemAgentsItem
  from ..models.list_transparency_moderation_response_200_data_item_appeal_type_0 import ListTransparencyModerationResponse200DataItemAppealType0
  from ..models.list_transparency_moderation_response_200_data_item_content_type_0 import ListTransparencyModerationResponse200DataItemContentType0
  from ..models.list_transparency_moderation_response_200_data_item_content_type_1 import ListTransparencyModerationResponse200DataItemContentType1





T = TypeVar("T", bound="ListTransparencyModerationResponse200DataItem")



@_attrs_define
class ListTransparencyModerationResponse200DataItem:
    """ 
        Attributes:
            case_id (UUID):
            action_id (UUID):
            kind (ListTransparencyModerationResponse200DataItemKind):
            reason (str):
            at (str):
            decided_by_label (ListTransparencyModerationResponse200DataItemDecidedByLabel):
            agents (list[ListTransparencyModerationResponse200DataItemAgentsItem]):
            content (ListTransparencyModerationResponse200DataItemContentType0 |
                ListTransparencyModerationResponse200DataItemContentType1 | None):
            appeal (ListTransparencyModerationResponse200DataItemAppealType0 | None):
     """

    case_id: UUID
    action_id: UUID
    kind: ListTransparencyModerationResponse200DataItemKind
    reason: str
    at: str
    decided_by_label: ListTransparencyModerationResponse200DataItemDecidedByLabel
    agents: list[ListTransparencyModerationResponse200DataItemAgentsItem]
    content: ListTransparencyModerationResponse200DataItemContentType0 | ListTransparencyModerationResponse200DataItemContentType1 | None
    appeal: ListTransparencyModerationResponse200DataItemAppealType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_transparency_moderation_response_200_data_item_agents_item import ListTransparencyModerationResponse200DataItemAgentsItem # noqa: PLC0415
        from ..models.list_transparency_moderation_response_200_data_item_appeal_type_0 import ListTransparencyModerationResponse200DataItemAppealType0 # noqa: PLC0415
        from ..models.list_transparency_moderation_response_200_data_item_content_type_0 import ListTransparencyModerationResponse200DataItemContentType0 # noqa: PLC0415
        from ..models.list_transparency_moderation_response_200_data_item_content_type_1 import ListTransparencyModerationResponse200DataItemContentType1 # noqa: PLC0415
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
        if isinstance(self.content, ListTransparencyModerationResponse200DataItemContentType0):
            content = self.content.to_dict()
        elif isinstance(self.content, ListTransparencyModerationResponse200DataItemContentType1):
            content = self.content.to_dict()
        else:
            content = self.content

        appeal: dict[str, Any] | None
        if isinstance(self.appeal, ListTransparencyModerationResponse200DataItemAppealType0):
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
        from ..models.list_transparency_moderation_response_200_data_item_agents_item import ListTransparencyModerationResponse200DataItemAgentsItem # noqa: PLC0415
        from ..models.list_transparency_moderation_response_200_data_item_appeal_type_0 import ListTransparencyModerationResponse200DataItemAppealType0 # noqa: PLC0415
        from ..models.list_transparency_moderation_response_200_data_item_content_type_0 import ListTransparencyModerationResponse200DataItemContentType0 # noqa: PLC0415
        from ..models.list_transparency_moderation_response_200_data_item_content_type_1 import ListTransparencyModerationResponse200DataItemContentType1 # noqa: PLC0415
        d = dict(src_dict)
        case_id = UUID(d.pop("case_id"))




        action_id = UUID(d.pop("action_id"))




        kind = ListTransparencyModerationResponse200DataItemKind(d.pop("kind"))




        reason = d.pop("reason")

        at = d.pop("at")

        decided_by_label = ListTransparencyModerationResponse200DataItemDecidedByLabel(d.pop("decided_by_label"))




        agents = []
        _agents = d.pop("agents")
        for agents_item_data in (_agents):
            agents_item = ListTransparencyModerationResponse200DataItemAgentsItem.from_dict(agents_item_data)



            agents.append(agents_item)


        def _parse_content(data: object) -> ListTransparencyModerationResponse200DataItemContentType0 | ListTransparencyModerationResponse200DataItemContentType1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = ListTransparencyModerationResponse200DataItemContentType0.from_dict(data)



                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = ListTransparencyModerationResponse200DataItemContentType1.from_dict(data)



                return content_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListTransparencyModerationResponse200DataItemContentType0 | ListTransparencyModerationResponse200DataItemContentType1 | None, data)

        content = _parse_content(d.pop("content"))


        def _parse_appeal(data: object) -> ListTransparencyModerationResponse200DataItemAppealType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                appeal_type_0 = ListTransparencyModerationResponse200DataItemAppealType0.from_dict(data)



                return appeal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListTransparencyModerationResponse200DataItemAppealType0 | None, data)

        appeal = _parse_appeal(d.pop("appeal"))


        list_transparency_moderation_response_200_data_item = cls(
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

        return list_transparency_moderation_response_200_data_item

