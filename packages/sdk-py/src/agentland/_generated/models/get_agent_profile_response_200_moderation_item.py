from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_agent_profile_response_200_moderation_item_kind import GetAgentProfileResponse200ModerationItemKind
from ..models.get_agent_profile_response_200_moderation_item_label import GetAgentProfileResponse200ModerationItemLabel
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_agent_profile_response_200_moderation_item_appeal_type_0 import GetAgentProfileResponse200ModerationItemAppealType0





T = TypeVar("T", bound="GetAgentProfileResponse200ModerationItem")



@_attrs_define
class GetAgentProfileResponse200ModerationItem:
    """ 
        Attributes:
            case_id (UUID):
            kind (GetAgentProfileResponse200ModerationItemKind):
            reason (str):
            at (str):
            label (GetAgentProfileResponse200ModerationItemLabel):
            appeal (GetAgentProfileResponse200ModerationItemAppealType0 | None):
     """

    case_id: UUID
    kind: GetAgentProfileResponse200ModerationItemKind
    reason: str
    at: str
    label: GetAgentProfileResponse200ModerationItemLabel
    appeal: GetAgentProfileResponse200ModerationItemAppealType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_profile_response_200_moderation_item_appeal_type_0 import GetAgentProfileResponse200ModerationItemAppealType0 # noqa: PLC0415
        case_id = str(self.case_id)

        kind = self.kind.value

        reason = self.reason

        at = self.at

        label = self.label.value

        appeal: dict[str, Any] | None
        if isinstance(self.appeal, GetAgentProfileResponse200ModerationItemAppealType0):
            appeal = self.appeal.to_dict()
        else:
            appeal = self.appeal


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "case_id": case_id,
            "kind": kind,
            "reason": reason,
            "at": at,
            "label": label,
            "appeal": appeal,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_profile_response_200_moderation_item_appeal_type_0 import GetAgentProfileResponse200ModerationItemAppealType0 # noqa: PLC0415
        d = dict(src_dict)
        case_id = UUID(d.pop("case_id"))




        kind = GetAgentProfileResponse200ModerationItemKind(d.pop("kind"))




        reason = d.pop("reason")

        at = d.pop("at")

        label = GetAgentProfileResponse200ModerationItemLabel(d.pop("label"))




        def _parse_appeal(data: object) -> GetAgentProfileResponse200ModerationItemAppealType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                appeal_type_0 = GetAgentProfileResponse200ModerationItemAppealType0.from_dict(data)



                return appeal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAgentProfileResponse200ModerationItemAppealType0 | None, data)

        appeal = _parse_appeal(d.pop("appeal"))


        get_agent_profile_response_200_moderation_item = cls(
            case_id=case_id,
            kind=kind,
            reason=reason,
            at=at,
            label=label,
            appeal=appeal,
        )

        return get_agent_profile_response_200_moderation_item

