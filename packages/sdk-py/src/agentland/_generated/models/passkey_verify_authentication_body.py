from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.passkey_verify_authentication_body_response import PasskeyVerifyAuthenticationBodyResponse





T = TypeVar("T", bound="PasskeyVerifyAuthenticationBody")



@_attrs_define
class PasskeyVerifyAuthenticationBody:
    """ 
        Attributes:
            response (PasskeyVerifyAuthenticationBodyResponse):
     """

    response: PasskeyVerifyAuthenticationBodyResponse
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.passkey_verify_authentication_body_response import PasskeyVerifyAuthenticationBodyResponse # noqa: PLC0415
        response = self.response.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "response": response,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.passkey_verify_authentication_body_response import PasskeyVerifyAuthenticationBodyResponse # noqa: PLC0415
        d = dict(src_dict)
        response = PasskeyVerifyAuthenticationBodyResponse.from_dict(d.pop("response"))




        passkey_verify_authentication_body = cls(
            response=response,
        )


        passkey_verify_authentication_body.additional_properties = d
        return passkey_verify_authentication_body

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
