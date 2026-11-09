from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_operator_moderation_response_200_data_item_kind import GetOperatorModerationResponse200DataItemKind
from ..models.get_operator_moderation_response_200_data_item_offense import GetOperatorModerationResponse200DataItemOffense
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_operator_moderation_response_200_data_item_appeal_type_0 import GetOperatorModerationResponse200DataItemAppealType0





T = TypeVar("T", bound="GetOperatorModerationResponse200DataItem")



@_attrs_define
class GetOperatorModerationResponse200DataItem:
    """ 
        Attributes:
            id (UUID):
            case_id (None | UUID):
            kind (GetOperatorModerationResponse200DataItemKind):
            offense (GetOperatorModerationResponse200DataItemOffense):
            public_reason (None | str):
            created_at (str):
            appeal (GetOperatorModerationResponse200DataItemAppealType0 | None):
     """

    id: UUID
    case_id: None | UUID
    kind: GetOperatorModerationResponse200DataItemKind
    offense: GetOperatorModerationResponse200DataItemOffense
    public_reason: None | str
    created_at: str
    appeal: GetOperatorModerationResponse200DataItemAppealType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_operator_moderation_response_200_data_item_appeal_type_0 import GetOperatorModerationResponse200DataItemAppealType0 # noqa: PLC0415
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
        if isinstance(self.appeal, GetOperatorModerationResponse200DataItemAppealType0):
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
        from ..models.get_operator_moderation_response_200_data_item_appeal_type_0 import GetOperatorModerationResponse200DataItemAppealType0 # noqa: PLC0415
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


        kind = GetOperatorModerationResponse200DataItemKind(d.pop("kind"))




        offense = GetOperatorModerationResponse200DataItemOffense(d.pop("offense"))




        def _parse_public_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        public_reason = _parse_public_reason(d.pop("public_reason"))


        created_at = d.pop("created_at")

        def _parse_appeal(data: object) -> GetOperatorModerationResponse200DataItemAppealType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                appeal_type_0 = GetOperatorModerationResponse200DataItemAppealType0.from_dict(data)



                return appeal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetOperatorModerationResponse200DataItemAppealType0 | None, data)

        appeal = _parse_appeal(d.pop("appeal"))


        get_operator_moderation_response_200_data_item = cls(
            id=id,
            case_id=case_id,
            kind=kind,
            offense=offense,
            public_reason=public_reason,
            created_at=created_at,
            appeal=appeal,
        )

        return get_operator_moderation_response_200_data_item

