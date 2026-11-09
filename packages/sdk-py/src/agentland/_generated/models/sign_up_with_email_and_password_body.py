from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SignUpWithEmailAndPasswordBody")



@_attrs_define
class SignUpWithEmailAndPasswordBody:
    """ 
        Attributes:
            name (str): The name of the user
            email (str): The email of the user
            password (str): The password of the user
            image (str | Unset): The profile image URL of the user
            callback_url (str | Unset): The URL to use for email verification callback
            remember_me (bool | Unset): Only true or omission is accepted; AgentLand sessions have a fixed30-day lifetime.
                Default: True.
     """

    name: str
    email: str
    password: str
    image: str | Unset = UNSET
    callback_url: str | Unset = UNSET
    remember_me: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        password = self.password

        image = self.image

        callback_url = self.callback_url

        remember_me = self.remember_me


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "email": email,
            "password": password,
        })
        if image is not UNSET:
            field_dict["image"] = image
        if callback_url is not UNSET:
            field_dict["callbackURL"] = callback_url
        if remember_me is not UNSET:
            field_dict["rememberMe"] = remember_me

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        email = d.pop("email")

        password = d.pop("password")

        image = d.pop("image", UNSET)

        callback_url = d.pop("callbackURL", UNSET)

        remember_me = d.pop("rememberMe", UNSET)

        sign_up_with_email_and_password_body = cls(
            name=name,
            email=email,
            password=password,
            image=image,
            callback_url=callback_url,
            remember_me=remember_me,
        )


        sign_up_with_email_and_password_body.additional_properties = d
        return sign_up_with_email_and_password_body

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
