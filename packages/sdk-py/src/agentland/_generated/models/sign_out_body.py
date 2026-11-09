from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SignOutBody")



@_attrs_define
class SignOutBody:
    """ 
        Attributes:
            callback_url (str | Unset): The URL to redirect to after provider logout
            disable_redirect (bool | Unset): Return the provider logout URL without redirecting
            state (str | Unset): State to pass to the provider logout endpoint
     """

    callback_url: str | Unset = UNSET
    disable_redirect: bool | Unset = UNSET
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        callback_url = self.callback_url

        disable_redirect = self.disable_redirect

        state = self.state


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if callback_url is not UNSET:
            field_dict["callbackURL"] = callback_url
        if disable_redirect is not UNSET:
            field_dict["disableRedirect"] = disable_redirect
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        callback_url = d.pop("callbackURL", UNSET)

        disable_redirect = d.pop("disableRedirect", UNSET)

        state = d.pop("state", UNSET)

        sign_out_body = cls(
            callback_url=callback_url,
            disable_redirect=disable_redirect,
            state=state,
        )


        sign_out_body.additional_properties = d
        return sign_out_body

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
