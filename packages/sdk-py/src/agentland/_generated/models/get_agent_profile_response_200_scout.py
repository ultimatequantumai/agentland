from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetAgentProfileResponse200Scout")



@_attrs_define
class GetAgentProfileResponse200Scout:
    """ 
        Attributes:
            qualified_count (int):
     """

    qualified_count: int





    def to_dict(self) -> dict[str, Any]:
        qualified_count = self.qualified_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "qualified_count": qualified_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        qualified_count = d.pop("qualified_count")

        get_agent_profile_response_200_scout = cls(
            qualified_count=qualified_count,
        )

        return get_agent_profile_response_200_scout

