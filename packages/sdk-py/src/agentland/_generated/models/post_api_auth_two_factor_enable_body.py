from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_api_auth_two_factor_enable_body_method import PostApiAuthTwoFactorEnableBodyMethod
from ..types import UNSET, Unset






T = TypeVar("T", bound="PostApiAuthTwoFactorEnableBody")



@_attrs_define
class PostApiAuthTwoFactorEnableBody:
    """ 
        Attributes:
            password (str): User password
            method (PostApiAuthTwoFactorEnableBodyMethod | Unset):
            issuer (str | Unset): Custom issuer for the TOTP URI
     """

    password: str
    method: PostApiAuthTwoFactorEnableBodyMethod | Unset = UNSET
    issuer: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        password = self.password

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value


        issuer = self.issuer


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "password": password,
        })
        if method is not UNSET:
            field_dict["method"] = method
        if issuer is not UNSET:
            field_dict["issuer"] = issuer

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password")

        _method = d.pop("method", UNSET)
        method: PostApiAuthTwoFactorEnableBodyMethod | Unset
        if isinstance(_method,  Unset):
            method = UNSET
        else:
            method = PostApiAuthTwoFactorEnableBodyMethod(_method)




        issuer = d.pop("issuer", UNSET)

        post_api_auth_two_factor_enable_body = cls(
            password=password,
            method=method,
            issuer=issuer,
        )


        post_api_auth_two_factor_enable_body.additional_properties = d
        return post_api_auth_two_factor_enable_body

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
