from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostApiAuthTwoFactorVerifyTotpBody")



@_attrs_define
class PostApiAuthTwoFactorVerifyTotpBody:
    """ 
        Attributes:
            code (str): The otp code to verify. Eg: "012345"
            trust_device (bool | Unset): Only false or omission is accepted; successful factor verification cannot be
                skipped. Default: False.
     """

    code: str
    trust_device: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        trust_device = self.trust_device


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
        })
        if trust_device is not UNSET:
            field_dict["trustDevice"] = trust_device

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        trust_device = d.pop("trustDevice", UNSET)

        post_api_auth_two_factor_verify_totp_body = cls(
            code=code,
            trust_device=trust_device,
        )


        post_api_auth_two_factor_verify_totp_body.additional_properties = d
        return post_api_auth_two_factor_verify_totp_body

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
