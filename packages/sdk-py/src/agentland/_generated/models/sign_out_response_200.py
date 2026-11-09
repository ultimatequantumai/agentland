from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SignOutResponse200")



@_attrs_define
class SignOutResponse200:
    """ 
        Attributes:
            success (bool | Unset):
            url (str | Unset): Provider logout URL when RP-initiated logout is available
            redirect (bool | Unset): Whether the client should redirect to the provider logout URL
     """

    success: bool | Unset = UNSET
    url: str | Unset = UNSET
    redirect: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        success = self.success

        url = self.url

        redirect = self.redirect


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if success is not UNSET:
            field_dict["success"] = success
        if url is not UNSET:
            field_dict["url"] = url
        if redirect is not UNSET:
            field_dict["redirect"] = redirect

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        url = d.pop("url", UNSET)

        redirect = d.pop("redirect", UNSET)

        sign_out_response_200 = cls(
            success=success,
            url=url,
            redirect=redirect,
        )


        sign_out_response_200.additional_properties = d
        return sign_out_response_200

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
