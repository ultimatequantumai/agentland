from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.unsubscribe_one_click_data_body_list_unsubscribe import UnsubscribeOneClickDataBodyListUnsubscribe






T = TypeVar("T", bound="UnsubscribeOneClickDataBody")



@_attrs_define
class UnsubscribeOneClickDataBody:
    """ RFC 8058 one-click body `List-Unsubscribe=One-Click`.

        Attributes:
            list_unsubscribe (UnsubscribeOneClickDataBodyListUnsubscribe):
     """

    list_unsubscribe: UnsubscribeOneClickDataBodyListUnsubscribe
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        list_unsubscribe = self.list_unsubscribe.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "List-Unsubscribe": list_unsubscribe,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        list_unsubscribe = UnsubscribeOneClickDataBodyListUnsubscribe(d.pop("List-Unsubscribe"))




        unsubscribe_one_click_data_body = cls(
            list_unsubscribe=list_unsubscribe,
        )


        unsubscribe_one_click_data_body.additional_properties = d
        return unsubscribe_one_click_data_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
