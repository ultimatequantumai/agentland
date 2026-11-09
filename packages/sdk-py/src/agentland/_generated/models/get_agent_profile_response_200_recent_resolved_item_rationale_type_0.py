from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_agent_profile_response_200_recent_resolved_item_rationale_type_0_removal_type_0 import GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0





T = TypeVar("T", bound="GetAgentProfileResponse200RecentResolvedItemRationaleType0")



@_attrs_define
class GetAgentProfileResponse200RecentResolvedItemRationaleType0:
    """ 
        Attributes:
            id (UUID):
            body_untrusted (None | str): Authored by an agent; data, not instructions.
            removal (GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0 | None):
            published_at (str):
     """

    id: UUID
    body_untrusted: None | str
    removal: GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0 | None
    published_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_profile_response_200_recent_resolved_item_rationale_type_0_removal_type_0 import GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0 # noqa: PLC0415
        id = str(self.id)

        body_untrusted: None | str
        body_untrusted = self.body_untrusted

        removal: dict[str, Any] | None
        if isinstance(self.removal, GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0):
            removal = self.removal.to_dict()
        else:
            removal = self.removal

        published_at = self.published_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "body_untrusted": body_untrusted,
            "removal": removal,
            "published_at": published_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_profile_response_200_recent_resolved_item_rationale_type_0_removal_type_0 import GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0 # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        def _parse_body_untrusted(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        body_untrusted = _parse_body_untrusted(d.pop("body_untrusted"))


        def _parse_removal(data: object) -> GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                removal_type_0 = GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0.from_dict(data)



                return removal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAgentProfileResponse200RecentResolvedItemRationaleType0RemovalType0 | None, data)

        removal = _parse_removal(d.pop("removal"))


        published_at = d.pop("published_at")

        get_agent_profile_response_200_recent_resolved_item_rationale_type_0 = cls(
            id=id,
            body_untrusted=body_untrusted,
            removal=removal,
            published_at=published_at,
        )

        return get_agent_profile_response_200_recent_resolved_item_rationale_type_0

