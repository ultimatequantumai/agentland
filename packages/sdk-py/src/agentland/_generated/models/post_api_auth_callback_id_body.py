from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostApiAuthCallbackIdBody")



@_attrs_define
class PostApiAuthCallbackIdBody:
    """ 
        Attributes:
            code (str | Unset):
            error (str | Unset):
            device_id (str | Unset):
            error_description (str | Unset):
            state (str | Unset):
            user (str | Unset):
            iss (str | Unset):
     """

    code: str | Unset = UNSET
    error: str | Unset = UNSET
    device_id: str | Unset = UNSET
    error_description: str | Unset = UNSET
    state: str | Unset = UNSET
    user: str | Unset = UNSET
    iss: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        error = self.error

        device_id = self.device_id

        error_description = self.error_description

        state = self.state

        user = self.user

        iss = self.iss


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if error is not UNSET:
            field_dict["error"] = error
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if error_description is not UNSET:
            field_dict["error_description"] = error_description
        if state is not UNSET:
            field_dict["state"] = state
        if user is not UNSET:
            field_dict["user"] = user
        if iss is not UNSET:
            field_dict["iss"] = iss

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        error = d.pop("error", UNSET)

        device_id = d.pop("device_id", UNSET)

        error_description = d.pop("error_description", UNSET)

        state = d.pop("state", UNSET)

        user = d.pop("user", UNSET)

        iss = d.pop("iss", UNSET)

        post_api_auth_callback_id_body = cls(
            code=code,
            error=error,
            device_id=device_id,
            error_description=error_description,
            state=state,
            user=user,
            iss=iss,
        )


        post_api_auth_callback_id_body.additional_properties = d
        return post_api_auth_callback_id_body

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
