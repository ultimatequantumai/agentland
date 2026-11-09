from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_status_response_200_checks_item_name import GetStatusResponse200ChecksItemName
from ..models.get_status_response_200_checks_item_state import GetStatusResponse200ChecksItemState
from typing import cast






T = TypeVar("T", bound="GetStatusResponse200ChecksItem")



@_attrs_define
class GetStatusResponse200ChecksItem:
    """ 
        Attributes:
            name (GetStatusResponse200ChecksItemName):
            state (GetStatusResponse200ChecksItemState):
            checked_at (None | str):
     """

    name: GetStatusResponse200ChecksItemName
    state: GetStatusResponse200ChecksItemState
    checked_at: None | str





    def to_dict(self) -> dict[str, Any]:
        name = self.name.value

        state = self.state.value

        checked_at: None | str
        checked_at = self.checked_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "state": state,
            "checked_at": checked_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = GetStatusResponse200ChecksItemName(d.pop("name"))




        state = GetStatusResponse200ChecksItemState(d.pop("state"))




        def _parse_checked_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        checked_at = _parse_checked_at(d.pop("checked_at"))


        get_status_response_200_checks_item = cls(
            name=name,
            state=state,
            checked_at=checked_at,
        )

        return get_status_response_200_checks_item

