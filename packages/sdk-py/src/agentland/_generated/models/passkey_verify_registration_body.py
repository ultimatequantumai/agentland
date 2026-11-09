from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PasskeyVerifyRegistrationBody")



@_attrs_define
class PasskeyVerifyRegistrationBody:
    """ 
        Attributes:
            response (Any):
            name (str | Unset): Name of the passkey
            create_session (bool | Unset): Create a session after registering the passkey
     """

    response: Any
    name: str | Unset = UNSET
    create_session: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        response = self.response

        name = self.name

        create_session = self.create_session


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "response": response,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if create_session is not UNSET:
            field_dict["createSession"] = create_session

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        response = d.pop("response")

        name = d.pop("name", UNSET)

        create_session = d.pop("createSession", UNSET)

        passkey_verify_registration_body = cls(
            response=response,
            name=name,
            create_session=create_session,
        )


        passkey_verify_registration_body.additional_properties = d
        return passkey_verify_registration_body

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
