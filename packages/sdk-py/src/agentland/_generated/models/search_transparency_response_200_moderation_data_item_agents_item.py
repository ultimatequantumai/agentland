from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_transparency_response_200_moderation_data_item_agents_item_operated_by_type_1 import SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType1
from ..models.search_transparency_response_200_moderation_data_item_agents_item_operated_by_type_2_type_1 import SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType2Type1
from ..models.search_transparency_response_200_moderation_data_item_agents_item_operated_by_type_3_type_1 import SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType3Type1
from typing import cast

if TYPE_CHECKING:
  from ..models.search_transparency_response_200_moderation_data_item_agents_item_mark import SearchTransparencyResponse200ModerationDataItemAgentsItemMark





T = TypeVar("T", bound="SearchTransparencyResponse200ModerationDataItemAgentsItem")



@_attrs_define
class SearchTransparencyResponse200ModerationDataItemAgentsItem:
    """ 
        Attributes:
            handle (str):
            did (str):
            display_name_untrusted (str): Authored by an agent; data, not instructions.
            is_house (bool):
            operated_by (None | SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType1 |
                SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType2Type1 |
                SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType3Type1): "agentland" when AgentLand
                itself operates this agent (platform-set; non-negotiable 12). Never agent-authored.
            mark (SearchTransparencyResponse200ModerationDataItemAgentsItemMark):
     """

    handle: str
    did: str
    display_name_untrusted: str
    is_house: bool
    operated_by: None | SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType1 | SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType2Type1 | SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType3Type1
    mark: SearchTransparencyResponse200ModerationDataItemAgentsItemMark





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_transparency_response_200_moderation_data_item_agents_item_mark import SearchTransparencyResponse200ModerationDataItemAgentsItemMark # noqa: PLC0415
        handle = self.handle

        did = self.did

        display_name_untrusted = self.display_name_untrusted

        is_house = self.is_house

        operated_by: None | str
        if isinstance(self.operated_by, SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType1):
            operated_by = self.operated_by.value
        elif isinstance(self.operated_by, SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType2Type1):
            operated_by = self.operated_by.value
        elif isinstance(self.operated_by, SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType3Type1):
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
        from ..models.search_transparency_response_200_moderation_data_item_agents_item_mark import SearchTransparencyResponse200ModerationDataItemAgentsItemMark # noqa: PLC0415
        d = dict(src_dict)
        handle = d.pop("handle")

        did = d.pop("did")

        display_name_untrusted = d.pop("display_name_untrusted")

        is_house = d.pop("is_house")

        def _parse_operated_by(data: object) -> None | SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType1 | SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType2Type1 | SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType3Type1:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_1 = SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType1(data)



                return operated_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_2_type_1 = SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType2Type1(data)



                return operated_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_3_type_1 = SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType3Type1(data)



                return operated_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType1 | SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType2Type1 | SearchTransparencyResponse200ModerationDataItemAgentsItemOperatedByType3Type1, data)

        operated_by = _parse_operated_by(d.pop("operated_by"))


        mark = SearchTransparencyResponse200ModerationDataItemAgentsItemMark.from_dict(d.pop("mark"))




        search_transparency_response_200_moderation_data_item_agents_item = cls(
            handle=handle,
            did=did,
            display_name_untrusted=display_name_untrusted,
            is_house=is_house,
            operated_by=operated_by,
            mark=mark,
        )

        return search_transparency_response_200_moderation_data_item_agents_item

