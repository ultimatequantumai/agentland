from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_operator_moderation_overview_response_200_data_item_actions_item_kind import GetOperatorModerationOverviewResponse200DataItemActionsItemKind
from ..models.get_operator_moderation_overview_response_200_data_item_actions_item_offense import GetOperatorModerationOverviewResponse200DataItemActionsItemOffense
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_operator_moderation_overview_response_200_data_item_actions_item_appeal_type_0 import GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0





T = TypeVar("T", bound="GetOperatorModerationOverviewResponse200DataItemActionsItem")



@_attrs_define
class GetOperatorModerationOverviewResponse200DataItemActionsItem:
    """ 
        Attributes:
            id (UUID):
            case_id (None | UUID):
            kind (GetOperatorModerationOverviewResponse200DataItemActionsItemKind):
            offense (GetOperatorModerationOverviewResponse200DataItemActionsItemOffense):
            public_reason (None | str):
            created_at (str):
            appeal (GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0 | None):
     """

    id: UUID
    case_id: None | UUID
    kind: GetOperatorModerationOverviewResponse200DataItemActionsItemKind
    offense: GetOperatorModerationOverviewResponse200DataItemActionsItemOffense
    public_reason: None | str
    created_at: str
    appeal: GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_operator_moderation_overview_response_200_data_item_actions_item_appeal_type_0 import GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0 # noqa: PLC0415
        id = str(self.id)

        case_id: None | str
        if isinstance(self.case_id, UUID):
            case_id = str(self.case_id)
        else:
            case_id = self.case_id

        kind = self.kind.value

        offense = self.offense.value

        public_reason: None | str
        public_reason = self.public_reason

        created_at = self.created_at

        appeal: dict[str, Any] | None
        if isinstance(self.appeal, GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0):
            appeal = self.appeal.to_dict()
        else:
            appeal = self.appeal


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "case_id": case_id,
            "kind": kind,
            "offense": offense,
            "public_reason": public_reason,
            "created_at": created_at,
            "appeal": appeal,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_operator_moderation_overview_response_200_data_item_actions_item_appeal_type_0 import GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0 # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        def _parse_case_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                case_id_type_0 = UUID(data)



                return case_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        case_id = _parse_case_id(d.pop("case_id"))


        kind = GetOperatorModerationOverviewResponse200DataItemActionsItemKind(d.pop("kind"))




        offense = GetOperatorModerationOverviewResponse200DataItemActionsItemOffense(d.pop("offense"))




        def _parse_public_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        public_reason = _parse_public_reason(d.pop("public_reason"))


        created_at = d.pop("created_at")

        def _parse_appeal(data: object) -> GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                appeal_type_0 = GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0.from_dict(data)



                return appeal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0 | None, data)

        appeal = _parse_appeal(d.pop("appeal"))


        get_operator_moderation_overview_response_200_data_item_actions_item = cls(
            id=id,
            case_id=case_id,
            kind=kind,
            offense=offense,
            public_reason=public_reason,
            created_at=created_at,
            appeal=appeal,
        )

        return get_operator_moderation_overview_response_200_data_item_actions_item

