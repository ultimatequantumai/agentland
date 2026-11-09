from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.change_password_response_200_user import ChangePasswordResponse200User





T = TypeVar("T", bound="ChangePasswordResponse200")



@_attrs_define
class ChangePasswordResponse200:
    """ 
        Attributes:
            user (ChangePasswordResponse200User):
            token (None | str | Unset): New session token if other sessions were revoked
     """

    user: ChangePasswordResponse200User
    token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.change_password_response_200_user import ChangePasswordResponse200User # noqa: PLC0415
        user = self.user.to_dict()

        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "user": user,
        })
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change_password_response_200_user import ChangePasswordResponse200User # noqa: PLC0415
        d = dict(src_dict)
        user = ChangePasswordResponse200User.from_dict(d.pop("user"))




        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))


        change_password_response_200 = cls(
            user=user,
            token=token,
        )


        change_password_response_200.additional_properties = d
        return change_password_response_200

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
