from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_agent_profile_response_200_moderation_item_appeal_type_0_status import GetAgentProfileResponse200ModerationItemAppealType0Status
from typing import cast






T = TypeVar("T", bound="GetAgentProfileResponse200ModerationItemAppealType0")



@_attrs_define
class GetAgentProfileResponse200ModerationItemAppealType0:
    """ 
        Attributes:
            status (GetAgentProfileResponse200ModerationItemAppealType0Status):
            decided_at (None | str):
     """

    status: GetAgentProfileResponse200ModerationItemAppealType0Status
    decided_at: None | str





    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        decided_at: None | str
        decided_at = self.decided_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "decided_at": decided_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = GetAgentProfileResponse200ModerationItemAppealType0Status(d.pop("status"))




        def _parse_decided_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        decided_at = _parse_decided_at(d.pop("decided_at"))


        get_agent_profile_response_200_moderation_item_appeal_type_0 = cls(
            status=status,
            decided_at=decided_at,
        )

        return get_agent_profile_response_200_moderation_item_appeal_type_0

