from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_agent_profile_response_200_recent_resolved_item_rationale_type_0_removal_type_0_label import GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0Label
from uuid import UUID






T = TypeVar("T", bound="GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0")



@_attrs_define
class GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0:
    """ 
        Attributes:
            case_id (UUID):
            reason (str):
            removed_at (str):
            label (GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0Label):
     """

    case_id: UUID
    reason: str
    removed_at: str
    label: GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0Label





    def to_dict(self) -> dict[str, Any]:
        case_id = str(self.case_id)

        reason = self.reason

        removed_at = self.removed_at

        label = self.label.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "case_id": case_id,
            "reason": reason,
            "removed_at": removed_at,
            "label": label,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        case_id = UUID(d.pop("case_id"))




        reason = d.pop("reason")

        removed_at = d.pop("removed_at")

        label = GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0Label(d.pop("label"))




        get_agent_profile_response_200_recent_resolved_item_rationale_type_0_removal_type_0 = cls(
            case_id=case_id,
            reason=reason,
            removed_at=removed_at,
            label=label,
        )

        return get_agent_profile_response_200_recent_resolved_item_rationale_type_0_removal_type_0

