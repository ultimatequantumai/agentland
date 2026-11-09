from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_operator_moderation_overview_response_200_data_item_actions_item_appeal_type_0_status import GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0Status
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0")



@_attrs_define
class GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0:
    """ 
        Attributes:
            id (UUID):
            status (GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0Status):
            filed_at (str):
            due_at (str):
            decided_at (None | str):
            decision_reason (None | str):
     """

    id: UUID
    status: GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0Status
    filed_at: str
    due_at: str
    decided_at: None | str
    decision_reason: None | str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        status = self.status.value

        filed_at = self.filed_at

        due_at = self.due_at

        decided_at: None | str
        decided_at = self.decided_at

        decision_reason: None | str
        decision_reason = self.decision_reason


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "status": status,
            "filed_at": filed_at,
            "due_at": due_at,
            "decided_at": decided_at,
            "decision_reason": decision_reason,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        status = GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0Status(d.pop("status"))




        filed_at = d.pop("filed_at")

        due_at = d.pop("due_at")

        def _parse_decided_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        decided_at = _parse_decided_at(d.pop("decided_at"))


        def _parse_decision_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        decision_reason = _parse_decision_reason(d.pop("decision_reason"))


        get_operator_moderation_overview_response_200_data_item_actions_item_appeal_type_0 = cls(
            id=id,
            status=status,
            filed_at=filed_at,
            due_at=due_at,
            decided_at=decided_at,
            decision_reason=decision_reason,
        )

        return get_operator_moderation_overview_response_200_data_item_actions_item_appeal_type_0

