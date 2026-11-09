from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="PostApiAuthRefreshTokenResponse200")



@_attrs_define
class PostApiAuthRefreshTokenResponse200:
    """ 
        Attributes:
            token_type (str | Unset):
            id_token (str | Unset):
            access_token (str | Unset):
            refresh_token (str | Unset):
            access_token_expires_at (datetime.datetime | Unset):
            refresh_token_expires_at (datetime.datetime | Unset):
     """

    token_type: str | Unset = UNSET
    id_token: str | Unset = UNSET
    access_token: str | Unset = UNSET
    refresh_token: str | Unset = UNSET
    access_token_expires_at: datetime.datetime | Unset = UNSET
    refresh_token_expires_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        token_type = self.token_type

        id_token = self.id_token

        access_token = self.access_token

        refresh_token = self.refresh_token

        access_token_expires_at: str | Unset = UNSET
        if not isinstance(self.access_token_expires_at, Unset):
            access_token_expires_at = self.access_token_expires_at.isoformat()

        refresh_token_expires_at: str | Unset = UNSET
        if not isinstance(self.refresh_token_expires_at, Unset):
            refresh_token_expires_at = self.refresh_token_expires_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if token_type is not UNSET:
            field_dict["tokenType"] = token_type
        if id_token is not UNSET:
            field_dict["idToken"] = id_token
        if access_token is not UNSET:
            field_dict["accessToken"] = access_token
        if refresh_token is not UNSET:
            field_dict["refreshToken"] = refresh_token
        if access_token_expires_at is not UNSET:
            field_dict["accessTokenExpiresAt"] = access_token_expires_at
        if refresh_token_expires_at is not UNSET:
            field_dict["refreshTokenExpiresAt"] = refresh_token_expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token_type = d.pop("tokenType", UNSET)

        id_token = d.pop("idToken", UNSET)

        access_token = d.pop("accessToken", UNSET)

        refresh_token = d.pop("refreshToken", UNSET)

        _access_token_expires_at = d.pop("accessTokenExpiresAt", UNSET)
        access_token_expires_at: datetime.datetime | Unset
        if isinstance(_access_token_expires_at,  Unset):
            access_token_expires_at = UNSET
        else:
            access_token_expires_at = datetime.datetime.fromisoformat(_access_token_expires_at)




        _refresh_token_expires_at = d.pop("refreshTokenExpiresAt", UNSET)
        refresh_token_expires_at: datetime.datetime | Unset
        if isinstance(_refresh_token_expires_at,  Unset):
            refresh_token_expires_at = UNSET
        else:
            refresh_token_expires_at = datetime.datetime.fromisoformat(_refresh_token_expires_at)




        post_api_auth_refresh_token_response_200 = cls(
            token_type=token_type,
            id_token=id_token,
            access_token=access_token,
            refresh_token=refresh_token,
            access_token_expires_at=access_token_expires_at,
            refresh_token_expires_at=refresh_token_expires_at,
        )


        post_api_auth_refresh_token_response_200.additional_properties = d
        return post_api_auth_refresh_token_response_200

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
