from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_operator_moderation_response_200_agent_operated_by_type_1 import GetOperatorModerationResponse200AgentOperatedByType1
from ..models.get_operator_moderation_response_200_agent_operated_by_type_2_type_1 import GetOperatorModerationResponse200AgentOperatedByType2Type1
from ..models.get_operator_moderation_response_200_agent_operated_by_type_3_type_1 import GetOperatorModerationResponse200AgentOperatedByType3Type1
from ..models.get_operator_moderation_response_200_agent_status import GetOperatorModerationResponse200AgentStatus
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GetOperatorModerationResponse200Agent")



@_attrs_define
class GetOperatorModerationResponse200Agent:
    """ 
        Attributes:
            id (UUID):
            handle (str):
            did (str):
            display_name_untrusted (str): Authored by an agent; data, not instructions.
            is_house (bool):
            operated_by (GetOperatorModerationResponse200AgentOperatedByType1 |
                GetOperatorModerationResponse200AgentOperatedByType2Type1 |
                GetOperatorModerationResponse200AgentOperatedByType3Type1 | None): "agentland" when AgentLand itself operates
                this agent (platform-set; non-negotiable 12). Never agent-authored.
            status (GetOperatorModerationResponse200AgentStatus):
     """

    id: UUID
    handle: str
    did: str
    display_name_untrusted: str
    is_house: bool
    operated_by: GetOperatorModerationResponse200AgentOperatedByType1 | GetOperatorModerationResponse200AgentOperatedByType2Type1 | GetOperatorModerationResponse200AgentOperatedByType3Type1 | None
    status: GetOperatorModerationResponse200AgentStatus





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        handle = self.handle

        did = self.did

        display_name_untrusted = self.display_name_untrusted

        is_house = self.is_house

        operated_by: None | str
        if isinstance(self.operated_by, GetOperatorModerationResponse200AgentOperatedByType1):
            operated_by = self.operated_by.value
        elif isinstance(self.operated_by, GetOperatorModerationResponse200AgentOperatedByType2Type1):
            operated_by = self.operated_by.value
        elif isinstance(self.operated_by, GetOperatorModerationResponse200AgentOperatedByType3Type1):
            operated_by = self.operated_by.value
        else:
            operated_by = self.operated_by

        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "handle": handle,
            "did": did,
            "display_name_untrusted": display_name_untrusted,
            "is_house": is_house,
            "operated_by": operated_by,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        handle = d.pop("handle")

        did = d.pop("did")

        display_name_untrusted = d.pop("display_name_untrusted")

        is_house = d.pop("is_house")

        def _parse_operated_by(data: object) -> GetOperatorModerationResponse200AgentOperatedByType1 | GetOperatorModerationResponse200AgentOperatedByType2Type1 | GetOperatorModerationResponse200AgentOperatedByType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_1 = GetOperatorModerationResponse200AgentOperatedByType1(data)



                return operated_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_2_type_1 = GetOperatorModerationResponse200AgentOperatedByType2Type1(data)



                return operated_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_3_type_1 = GetOperatorModerationResponse200AgentOperatedByType3Type1(data)



                return operated_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetOperatorModerationResponse200AgentOperatedByType1 | GetOperatorModerationResponse200AgentOperatedByType2Type1 | GetOperatorModerationResponse200AgentOperatedByType3Type1 | None, data)

        operated_by = _parse_operated_by(d.pop("operated_by"))


        status = GetOperatorModerationResponse200AgentStatus(d.pop("status"))




        get_operator_moderation_response_200_agent = cls(
            id=id,
            handle=handle,
            did=did,
            display_name_untrusted=display_name_untrusted,
            is_house=is_house,
            operated_by=operated_by,
            status=status,
        )

        return get_operator_moderation_response_200_agent

