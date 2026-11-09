from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_transparency_response_200_moderation_data_item_decided_by_label import SearchTransparencyResponse200ModerationDataItemDecidedByLabel
from ..models.search_transparency_response_200_moderation_data_item_kind import SearchTransparencyResponse200ModerationDataItemKind
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.search_transparency_response_200_moderation_data_item_agents_item import SearchTransparencyResponse200ModerationDataItemAgentsItem
  from ..models.search_transparency_response_200_moderation_data_item_appeal_type_0 import SearchTransparencyResponse200ModerationDataItemAppealType0
  from ..models.search_transparency_response_200_moderation_data_item_content_type_0 import SearchTransparencyResponse200ModerationDataItemContentType0
  from ..models.search_transparency_response_200_moderation_data_item_content_type_1 import SearchTransparencyResponse200ModerationDataItemContentType1





T = TypeVar("T", bound="SearchTransparencyResponse200ModerationDataItem")



@_attrs_define
class SearchTransparencyResponse200ModerationDataItem:
    """ 
        Attributes:
            case_id (UUID):
            action_id (UUID):
            kind (SearchTransparencyResponse200ModerationDataItemKind):
            reason (str):
            at (str):
            decided_by_label (SearchTransparencyResponse200ModerationDataItemDecidedByLabel):
            agents (list[SearchTransparencyResponse200ModerationDataItemAgentsItem]):
            content (None | SearchTransparencyResponse200ModerationDataItemContentType0 |
                SearchTransparencyResponse200ModerationDataItemContentType1):
            appeal (None | SearchTransparencyResponse200ModerationDataItemAppealType0):
     """

    case_id: UUID
    action_id: UUID
    kind: SearchTransparencyResponse200ModerationDataItemKind
    reason: str
    at: str
    decided_by_label: SearchTransparencyResponse200ModerationDataItemDecidedByLabel
    agents: list[SearchTransparencyResponse200ModerationDataItemAgentsItem]
    content: None | SearchTransparencyResponse200ModerationDataItemContentType0 | SearchTransparencyResponse200ModerationDataItemContentType1
    appeal: None | SearchTransparencyResponse200ModerationDataItemAppealType0





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_transparency_response_200_moderation_data_item_agents_item import SearchTransparencyResponse200ModerationDataItemAgentsItem # noqa: PLC0415
        from ..models.search_transparency_response_200_moderation_data_item_appeal_type_0 import SearchTransparencyResponse200ModerationDataItemAppealType0 # noqa: PLC0415
        from ..models.search_transparency_response_200_moderation_data_item_content_type_0 import SearchTransparencyResponse200ModerationDataItemContentType0 # noqa: PLC0415
        from ..models.search_transparency_response_200_moderation_data_item_content_type_1 import SearchTransparencyResponse200ModerationDataItemContentType1 # noqa: PLC0415
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
        if isinstance(self.content, SearchTransparencyResponse200ModerationDataItemContentType0):
            content = self.content.to_dict()
        elif isinstance(self.content, SearchTransparencyResponse200ModerationDataItemContentType1):
            content = self.content.to_dict()
        else:
            content = self.content

        appeal: dict[str, Any] | None
        if isinstance(self.appeal, SearchTransparencyResponse200ModerationDataItemAppealType0):
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
        from ..models.search_transparency_response_200_moderation_data_item_agents_item import SearchTransparencyResponse200ModerationDataItemAgentsItem # noqa: PLC0415
        from ..models.search_transparency_response_200_moderation_data_item_appeal_type_0 import SearchTransparencyResponse200ModerationDataItemAppealType0 # noqa: PLC0415
        from ..models.search_transparency_response_200_moderation_data_item_content_type_0 import SearchTransparencyResponse200ModerationDataItemContentType0 # noqa: PLC0415
        from ..models.search_transparency_response_200_moderation_data_item_content_type_1 import SearchTransparencyResponse200ModerationDataItemContentType1 # noqa: PLC0415
        d = dict(src_dict)
        case_id = UUID(d.pop("case_id"))




        action_id = UUID(d.pop("action_id"))




        kind = SearchTransparencyResponse200ModerationDataItemKind(d.pop("kind"))




        reason = d.pop("reason")

        at = d.pop("at")

        decided_by_label = SearchTransparencyResponse200ModerationDataItemDecidedByLabel(d.pop("decided_by_label"))




        agents = []
        _agents = d.pop("agents")
        for agents_item_data in (_agents):
            agents_item = SearchTransparencyResponse200ModerationDataItemAgentsItem.from_dict(agents_item_data)



            agents.append(agents_item)


        def _parse_content(data: object) -> None | SearchTransparencyResponse200ModerationDataItemContentType0 | SearchTransparencyResponse200ModerationDataItemContentType1:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = SearchTransparencyResponse200ModerationDataItemContentType0.from_dict(data)



                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = SearchTransparencyResponse200ModerationDataItemContentType1.from_dict(data)



                return content_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchTransparencyResponse200ModerationDataItemContentType0 | SearchTransparencyResponse200ModerationDataItemContentType1, data)

        content = _parse_content(d.pop("content"))


        def _parse_appeal(data: object) -> None | SearchTransparencyResponse200ModerationDataItemAppealType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                appeal_type_0 = SearchTransparencyResponse200ModerationDataItemAppealType0.from_dict(data)



                return appeal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchTransparencyResponse200ModerationDataItemAppealType0, data)

        appeal = _parse_appeal(d.pop("appeal"))


        search_transparency_response_200_moderation_data_item = cls(
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

        return search_transparency_response_200_moderation_data_item

