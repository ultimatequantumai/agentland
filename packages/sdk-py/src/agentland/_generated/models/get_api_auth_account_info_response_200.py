from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_api_auth_account_info_response_200_account import GetApiAuthAccountInfoResponse200Account
  from ..models.get_api_auth_account_info_response_200_data import GetApiAuthAccountInfoResponse200Data
  from ..models.get_api_auth_account_info_response_200_user import GetApiAuthAccountInfoResponse200User





T = TypeVar("T", bound="GetApiAuthAccountInfoResponse200")



@_attrs_define
class GetApiAuthAccountInfoResponse200:
    """ 
        Attributes:
            user (GetApiAuthAccountInfoResponse200User):
            account (GetApiAuthAccountInfoResponse200Account):
            data (GetApiAuthAccountInfoResponse200Data):
     """

    user: GetApiAuthAccountInfoResponse200User
    account: GetApiAuthAccountInfoResponse200Account
    data: GetApiAuthAccountInfoResponse200Data





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_api_auth_account_info_response_200_account import GetApiAuthAccountInfoResponse200Account # noqa: PLC0415
        from ..models.get_api_auth_account_info_response_200_data import GetApiAuthAccountInfoResponse200Data # noqa: PLC0415
        from ..models.get_api_auth_account_info_response_200_user import GetApiAuthAccountInfoResponse200User # noqa: PLC0415
        user = self.user.to_dict()

        account = self.account.to_dict()

        data = self.data.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "user": user,
            "account": account,
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_auth_account_info_response_200_account import GetApiAuthAccountInfoResponse200Account # noqa: PLC0415
        from ..models.get_api_auth_account_info_response_200_data import GetApiAuthAccountInfoResponse200Data # noqa: PLC0415
        from ..models.get_api_auth_account_info_response_200_user import GetApiAuthAccountInfoResponse200User # noqa: PLC0415
        d = dict(src_dict)
        user = GetApiAuthAccountInfoResponse200User.from_dict(d.pop("user"))




        account = GetApiAuthAccountInfoResponse200Account.from_dict(d.pop("account"))




        data = GetApiAuthAccountInfoResponse200Data.from_dict(d.pop("data"))




        get_api_auth_account_info_response_200 = cls(
            user=user,
            account=account,
            data=data,
        )

        return get_api_auth_account_info_response_200

