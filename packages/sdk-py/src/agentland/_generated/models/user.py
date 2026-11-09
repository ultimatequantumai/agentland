from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="User")



@_attrs_define
class User:
    """ 
        Attributes:
            id (str):
            name (str):
            email (str):
            email_verified (bool):  Default: False.
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            image (str | Unset):
            two_factor_enabled (bool | Unset):  Default: False.
     """

    id: str
    name: str
    email: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    email_verified: bool = False
    image: str | Unset = UNSET
    two_factor_enabled: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        email = self.email

        email_verified = self.email_verified

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        image = self.image

        two_factor_enabled = self.two_factor_enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "email": email,
            "emailVerified": email_verified,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })
        if image is not UNSET:
            field_dict["image"] = image
        if two_factor_enabled is not UNSET:
            field_dict["twoFactorEnabled"] = two_factor_enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        email = d.pop("email")

        email_verified = d.pop("emailVerified")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))




        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))




        image = d.pop("image", UNSET)

        two_factor_enabled = d.pop("twoFactorEnabled", UNSET)

        user = cls(
            id=id,
            name=name,
            email=email,
            email_verified=email_verified,
            created_at=created_at,
            updated_at=updated_at,
            image=image,
            two_factor_enabled=two_factor_enabled,
        )


        user.additional_properties = d
        return user

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
