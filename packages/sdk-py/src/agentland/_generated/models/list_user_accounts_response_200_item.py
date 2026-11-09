from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime






T = TypeVar("T", bound="ListUserAccountsResponse200Item")



@_attrs_define
class ListUserAccountsResponse200Item:
    """ 
        Attributes:
            id (str):
            provider_id (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            account_id (str):
            user_id (str):
            scopes (list[str]):
     """

    id: str
    provider_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    account_id: str
    user_id: str
    scopes: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        provider_id = self.provider_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        account_id = self.account_id

        user_id = self.user_id

        scopes = self.scopes




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "providerId": provider_id,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "accountId": account_id,
            "userId": user_id,
            "scopes": scopes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        provider_id = d.pop("providerId")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))




        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))




        account_id = d.pop("accountId")

        user_id = d.pop("userId")

        scopes = cast(list[str], d.pop("scopes"))


        list_user_accounts_response_200_item = cls(
            id=id,
            provider_id=provider_id,
            created_at=created_at,
            updated_at=updated_at,
            account_id=account_id,
            user_id=user_id,
            scopes=scopes,
        )


        list_user_accounts_response_200_item.additional_properties = d
        return list_user_accounts_response_200_item

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
