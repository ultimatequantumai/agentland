from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="SignUpWithEmailAndPasswordResponse200User")



@_attrs_define
class SignUpWithEmailAndPasswordResponse200User:
    """ 
        Attributes:
            id (str): The unique identifier of the user
            email (str): The email address of the user
            name (str): The name of the user
            email_verified (bool): Whether the email has been verified
            created_at (datetime.datetime): When the user was created
            updated_at (datetime.datetime): When the user was last updated
            image (None | str | Unset): The profile image URL of the user
     """

    id: str
    email: str
    name: str
    email_verified: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    image: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        name = self.name

        email_verified = self.email_verified

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        image: None | str | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "email": email,
            "name": name,
            "emailVerified": email_verified,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        name = d.pop("name")

        email_verified = d.pop("emailVerified")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))




        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))




        def _parse_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image = _parse_image(d.pop("image", UNSET))


        sign_up_with_email_and_password_response_200_user = cls(
            id=id,
            email=email,
            name=name,
            email_verified=email_verified,
            created_at=created_at,
            updated_at=updated_at,
            image=image,
        )


        sign_up_with_email_and_password_response_200_user.additional_properties = d
        return sign_up_with_email_and_password_response_200_user

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
