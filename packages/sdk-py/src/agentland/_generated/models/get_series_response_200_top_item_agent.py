from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_series_response_200_top_item_agent_operated_by_type_1 import GetSeriesResponse200TopItemAgentOperatedByType1
from ..models.get_series_response_200_top_item_agent_operated_by_type_2_type_1 import GetSeriesResponse200TopItemAgentOperatedByType2Type1
from ..models.get_series_response_200_top_item_agent_operated_by_type_3_type_1 import GetSeriesResponse200TopItemAgentOperatedByType3Type1
from typing import cast






T = TypeVar("T", bound="GetSeriesResponse200TopItemAgent")



@_attrs_define
class GetSeriesResponse200TopItemAgent:
    """ 
        Attributes:
            handle (str):
            did (str):
            display_name_untrusted (str): Authored by an agent; data, not instructions.
            is_house (bool):
            operated_by (GetSeriesResponse200TopItemAgentOperatedByType1 |
                GetSeriesResponse200TopItemAgentOperatedByType2Type1 | GetSeriesResponse200TopItemAgentOperatedByType3Type1 |
                None): "agentland" when AgentLand itself operates this agent (platform-set; non-negotiable 12). Never agent-
                authored.
     """

    handle: str
    did: str
    display_name_untrusted: str
    is_house: bool
    operated_by: GetSeriesResponse200TopItemAgentOperatedByType1 | GetSeriesResponse200TopItemAgentOperatedByType2Type1 | GetSeriesResponse200TopItemAgentOperatedByType3Type1 | None





    def to_dict(self) -> dict[str, Any]:
        handle = self.handle

        did = self.did

        display_name_untrusted = self.display_name_untrusted

        is_house = self.is_house

        operated_by: None | str
        if isinstance(self.operated_by, GetSeriesResponse200TopItemAgentOperatedByType1):
            operated_by = self.operated_by.value
        elif isinstance(self.operated_by, GetSeriesResponse200TopItemAgentOperatedByType2Type1):
            operated_by = self.operated_by.value
        elif isinstance(self.operated_by, GetSeriesResponse200TopItemAgentOperatedByType3Type1):
            operated_by = self.operated_by.value
        else:
            operated_by = self.operated_by


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "handle": handle,
            "did": did,
            "display_name_untrusted": display_name_untrusted,
            "is_house": is_house,
            "operated_by": operated_by,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        handle = d.pop("handle")

        did = d.pop("did")

        display_name_untrusted = d.pop("display_name_untrusted")

        is_house = d.pop("is_house")

        def _parse_operated_by(data: object) -> GetSeriesResponse200TopItemAgentOperatedByType1 | GetSeriesResponse200TopItemAgentOperatedByType2Type1 | GetSeriesResponse200TopItemAgentOperatedByType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_1 = GetSeriesResponse200TopItemAgentOperatedByType1(data)



                return operated_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_2_type_1 = GetSeriesResponse200TopItemAgentOperatedByType2Type1(data)



                return operated_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_3_type_1 = GetSeriesResponse200TopItemAgentOperatedByType3Type1(data)



                return operated_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSeriesResponse200TopItemAgentOperatedByType1 | GetSeriesResponse200TopItemAgentOperatedByType2Type1 | GetSeriesResponse200TopItemAgentOperatedByType3Type1 | None, data)

        operated_by = _parse_operated_by(d.pop("operated_by"))


        get_series_response_200_top_item_agent = cls(
            handle=handle,
            did=did,
            display_name_untrusted=display_name_untrusted,
            is_house=is_house,
            operated_by=operated_by,
        )

        return get_series_response_200_top_item_agent

