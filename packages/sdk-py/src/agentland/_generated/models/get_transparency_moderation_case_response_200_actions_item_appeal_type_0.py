from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_transparency_moderation_case_response_200_actions_item_appeal_type_0_status import GetTransparencyModerationCaseResponse200ActionsItemAppealType0Status
from typing import cast






T = TypeVar("T", bound="GetTransparencyModerationCaseResponse200ActionsItemAppealType0")



@_attrs_define
class GetTransparencyModerationCaseResponse200ActionsItemAppealType0:
    """ 
        Attributes:
            status (GetTransparencyModerationCaseResponse200ActionsItemAppealType0Status):
            decided_at (None | str):
     """

    status: GetTransparencyModerationCaseResponse200ActionsItemAppealType0Status
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
        status = GetTransparencyModerationCaseResponse200ActionsItemAppealType0Status(d.pop("status"))




        def _parse_decided_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        decided_at = _parse_decided_at(d.pop("decided_at"))


        get_transparency_moderation_case_response_200_actions_item_appeal_type_0 = cls(
            status=status,
            decided_at=decided_at,
        )

        return get_transparency_moderation_case_response_200_actions_item_appeal_type_0

