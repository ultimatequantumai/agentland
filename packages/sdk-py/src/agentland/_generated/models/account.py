from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="Account")



@_attrs_define
class Account:
    """ 
        Attributes:
            id (str):
            account_id (str):
            provider_id (str):
            user_id (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            access_token (str | Unset):
            refresh_token (str | Unset):
            id_token (str | Unset):
            access_token_expires_at (datetime.datetime | Unset):
            refresh_token_expires_at (datetime.datetime | Unset):
            scope (str | Unset):
            password (str | Unset):
     """

    id: str
    account_id: str
    provider_id: str
    user_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    access_token: str | Unset = UNSET
    refresh_token: str | Unset = UNSET
    id_token: str | Unset = UNSET
    access_token_expires_at: datetime.datetime | Unset = UNSET
    refresh_token_expires_at: datetime.datetime | Unset = UNSET
    scope: str | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_id = self.account_id

        provider_id = self.provider_id

        user_id = self.user_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        access_token = self.access_token

        refresh_token = self.refresh_token

        id_token = self.id_token

        access_token_expires_at: str | Unset = UNSET
        if not isinstance(self.access_token_expires_at, Unset):
            access_token_expires_at = self.access_token_expires_at.isoformat()

        refresh_token_expires_at: str | Unset = UNSET
        if not isinstance(self.refresh_token_expires_at, Unset):
            refresh_token_expires_at = self.refresh_token_expires_at.isoformat()

        scope = self.scope

        password = self.password


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "accountId": account_id,
            "providerId": provider_id,
            "userId": user_id,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })
        if access_token is not UNSET:
            field_dict["accessToken"] = access_token
        if refresh_token is not UNSET:
            field_dict["refreshToken"] = refresh_token
        if id_token is not UNSET:
            field_dict["idToken"] = id_token
        if access_token_expires_at is not UNSET:
            field_dict["accessTokenExpiresAt"] = access_token_expires_at
        if refresh_token_expires_at is not UNSET:
            field_dict["refreshTokenExpiresAt"] = refresh_token_expires_at
        if scope is not UNSET:
            field_dict["scope"] = scope
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        account_id = d.pop("accountId")

        provider_id = d.pop("providerId")

        user_id = d.pop("userId")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))




        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))




        access_token = d.pop("accessToken", UNSET)

        refresh_token = d.pop("refreshToken", UNSET)

        id_token = d.pop("idToken", UNSET)

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




        scope = d.pop("scope", UNSET)

        password = d.pop("password", UNSET)

        account = cls(
            id=id,
            account_id=account_id,
            provider_id=provider_id,
            user_id=user_id,
            created_at=created_at,
            updated_at=updated_at,
            access_token=access_token,
            refresh_token=refresh_token,
            id_token=id_token,
            access_token_expires_at=access_token_expires_at,
            refresh_token_expires_at=refresh_token_expires_at,
            scope=scope,
            password=password,
        )


        account.additional_properties = d
        return account

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
