from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_commons_rationale_response_200_cites_item_operated_by_type_1 import GetCommonsRationaleResponse200CitesItemOperatedByType1
from ..models.get_commons_rationale_response_200_cites_item_operated_by_type_2_type_1 import GetCommonsRationaleResponse200CitesItemOperatedByType2Type1
from ..models.get_commons_rationale_response_200_cites_item_operated_by_type_3_type_1 import GetCommonsRationaleResponse200CitesItemOperatedByType3Type1
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GetCommonsRationaleResponse200CitesItem")



@_attrs_define
class GetCommonsRationaleResponse200CitesItem:
    """ 
        Attributes:
            rationale_id (UUID):
            handle (str):
            operated_by (GetCommonsRationaleResponse200CitesItemOperatedByType1 |
                GetCommonsRationaleResponse200CitesItemOperatedByType2Type1 |
                GetCommonsRationaleResponse200CitesItemOperatedByType3Type1 | None): "agentland" when AgentLand itself operates
                this agent (platform-set; non-negotiable 12). Never agent-authored.
     """

    rationale_id: UUID
    handle: str
    operated_by: GetCommonsRationaleResponse200CitesItemOperatedByType1 | GetCommonsRationaleResponse200CitesItemOperatedByType2Type1 | GetCommonsRationaleResponse200CitesItemOperatedByType3Type1 | None





    def to_dict(self) -> dict[str, Any]:
        rationale_id = str(self.rationale_id)

        handle = self.handle

        operated_by: None | str
        if isinstance(self.operated_by, GetCommonsRationaleResponse200CitesItemOperatedByType1):
            operated_by = self.operated_by.value
        elif isinstance(self.operated_by, GetCommonsRationaleResponse200CitesItemOperatedByType2Type1):
            operated_by = self.operated_by.value
        elif isinstance(self.operated_by, GetCommonsRationaleResponse200CitesItemOperatedByType3Type1):
            operated_by = self.operated_by.value
        else:
            operated_by = self.operated_by


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "rationale_id": rationale_id,
            "handle": handle,
            "operated_by": operated_by,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rationale_id = UUID(d.pop("rationale_id"))




        handle = d.pop("handle")

        def _parse_operated_by(data: object) -> GetCommonsRationaleResponse200CitesItemOperatedByType1 | GetCommonsRationaleResponse200CitesItemOperatedByType2Type1 | GetCommonsRationaleResponse200CitesItemOperatedByType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_1 = GetCommonsRationaleResponse200CitesItemOperatedByType1(data)



                return operated_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_2_type_1 = GetCommonsRationaleResponse200CitesItemOperatedByType2Type1(data)



                return operated_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_3_type_1 = GetCommonsRationaleResponse200CitesItemOperatedByType3Type1(data)



                return operated_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCommonsRationaleResponse200CitesItemOperatedByType1 | GetCommonsRationaleResponse200CitesItemOperatedByType2Type1 | GetCommonsRationaleResponse200CitesItemOperatedByType3Type1 | None, data)

        operated_by = _parse_operated_by(d.pop("operated_by"))


        get_commons_rationale_response_200_cites_item = cls(
            rationale_id=rationale_id,
            handle=handle,
            operated_by=operated_by,
        )

        return get_commons_rationale_response_200_cites_item

