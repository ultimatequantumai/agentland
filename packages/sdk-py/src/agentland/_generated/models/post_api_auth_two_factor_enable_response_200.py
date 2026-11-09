from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_api_auth_two_factor_enable_response_200_method import PostApiAuthTwoFactorEnableResponse200Method
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostApiAuthTwoFactorEnableResponse200")



@_attrs_define
class PostApiAuthTwoFactorEnableResponse200:
    """ 
        Attributes:
            method (PostApiAuthTwoFactorEnableResponse200Method): The 2FA method that was enabled.
            totp_uri (str | Unset): TOTP URI for authenticator app setup. Only present when method is 'totp'.
            backup_codes (list[str] | Unset): Recovery backup codes. Only present when method is 'totp'.
     """

    method: PostApiAuthTwoFactorEnableResponse200Method
    totp_uri: str | Unset = UNSET
    backup_codes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        totp_uri = self.totp_uri

        backup_codes: list[str] | Unset = UNSET
        if not isinstance(self.backup_codes, Unset):
            backup_codes = self.backup_codes




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "method": method,
        })
        if totp_uri is not UNSET:
            field_dict["totpURI"] = totp_uri
        if backup_codes is not UNSET:
            field_dict["backupCodes"] = backup_codes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = PostApiAuthTwoFactorEnableResponse200Method(d.pop("method"))




        totp_uri = d.pop("totpURI", UNSET)

        backup_codes = cast(list[str], d.pop("backupCodes", UNSET))


        post_api_auth_two_factor_enable_response_200 = cls(
            method=method,
            totp_uri=totp_uri,
            backup_codes=backup_codes,
        )


        post_api_auth_two_factor_enable_response_200.additional_properties = d
        return post_api_auth_two_factor_enable_response_200

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
