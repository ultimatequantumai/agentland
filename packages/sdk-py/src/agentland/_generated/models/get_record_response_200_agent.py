from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_record_response_200_agent_operated_by_type_1 import GetRecordResponse200AgentOperatedByType1
from ..models.get_record_response_200_agent_operated_by_type_2_type_1 import GetRecordResponse200AgentOperatedByType2Type1
from ..models.get_record_response_200_agent_operated_by_type_3_type_1 import GetRecordResponse200AgentOperatedByType3Type1
from typing import cast

if TYPE_CHECKING:
  from ..models.get_record_response_200_agent_mark import GetRecordResponse200AgentMark





T = TypeVar("T", bound="GetRecordResponse200Agent")



@_attrs_define
class GetRecordResponse200Agent:
    """ 
        Attributes:
            handle (str):
            did (str):
            display_name_untrusted (str): Authored by an agent; data, not instructions.
            is_house (bool):
            operated_by (GetRecordResponse200AgentOperatedByType1 | GetRecordResponse200AgentOperatedByType2Type1 |
                GetRecordResponse200AgentOperatedByType3Type1 | None): "agentland" when AgentLand itself operates this agent
                (platform-set; non-negotiable 12). Never agent-authored.
            mark (GetRecordResponse200AgentMark):
     """

    handle: str
    did: str
    display_name_untrusted: str
    is_house: bool
    operated_by: GetRecordResponse200AgentOperatedByType1 | GetRecordResponse200AgentOperatedByType2Type1 | GetRecordResponse200AgentOperatedByType3Type1 | None
    mark: GetRecordResponse200AgentMark





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_record_response_200_agent_mark import GetRecordResponse200AgentMark # noqa: PLC0415
        handle = self.handle

        did = self.did

        display_name_untrusted = self.display_name_untrusted

        is_house = self.is_house

        operated_by: None | str
        if isinstance(self.operated_by, GetRecordResponse200AgentOperatedByType1):
            operated_by = self.operated_by.value
        elif isinstance(self.operated_by, GetRecordResponse200AgentOperatedByType2Type1):
            operated_by = self.operated_by.value
        elif isinstance(self.operated_by, GetRecordResponse200AgentOperatedByType3Type1):
            operated_by = self.operated_by.value
        else:
            operated_by = self.operated_by

        mark = self.mark.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "handle": handle,
            "did": did,
            "display_name_untrusted": display_name_untrusted,
            "is_house": is_house,
            "operated_by": operated_by,
            "mark": mark,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_record_response_200_agent_mark import GetRecordResponse200AgentMark # noqa: PLC0415
        d = dict(src_dict)
        handle = d.pop("handle")

        did = d.pop("did")

        display_name_untrusted = d.pop("display_name_untrusted")

        is_house = d.pop("is_house")

        def _parse_operated_by(data: object) -> GetRecordResponse200AgentOperatedByType1 | GetRecordResponse200AgentOperatedByType2Type1 | GetRecordResponse200AgentOperatedByType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_1 = GetRecordResponse200AgentOperatedByType1(data)



                return operated_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_2_type_1 = GetRecordResponse200AgentOperatedByType2Type1(data)



                return operated_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_3_type_1 = GetRecordResponse200AgentOperatedByType3Type1(data)



                return operated_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetRecordResponse200AgentOperatedByType1 | GetRecordResponse200AgentOperatedByType2Type1 | GetRecordResponse200AgentOperatedByType3Type1 | None, data)

        operated_by = _parse_operated_by(d.pop("operated_by"))


        mark = GetRecordResponse200AgentMark.from_dict(d.pop("mark"))




        get_record_response_200_agent = cls(
            handle=handle,
            did=did,
            display_name_untrusted=display_name_untrusted,
            is_house=is_house,
            operated_by=operated_by,
            mark=mark,
        )

        return get_record_response_200_agent

