from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetApiAuthAccountInfoResponse200Account")



@_attrs_define
class GetApiAuthAccountInfoResponse200Account:
    """ 
        Attributes:
            id (str):
            provider_id (str):
            account_id (str):
     """

    id: str
    provider_id: str
    account_id: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        provider_id = self.provider_id

        account_id = self.account_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "providerId": provider_id,
            "accountId": account_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        provider_id = d.pop("providerId")

        account_id = d.pop("accountId")

        get_api_auth_account_info_response_200_account = cls(
            id=id,
            provider_id=provider_id,
            account_id=account_id,
        )

        return get_api_auth_account_info_response_200_account

