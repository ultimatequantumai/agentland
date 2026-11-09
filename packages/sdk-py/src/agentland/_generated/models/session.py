from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="Session")



@_attrs_define
class Session:
    """ 
        Attributes:
            id (str):
            expires_at (datetime.datetime):
            token (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            user_id (str):
            ip_address (str | Unset):
            user_agent (str | Unset):
     """

    id: str
    expires_at: datetime.datetime
    token: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    user_id: str
    ip_address: str | Unset = UNSET
    user_agent: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        expires_at = self.expires_at.isoformat()

        token = self.token

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        ip_address = self.ip_address

        user_agent = self.user_agent


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "expiresAt": expires_at,
            "token": token,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "userId": user_id,
        })
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        expires_at = datetime.datetime.fromisoformat(d.pop("expiresAt"))




        token = d.pop("token")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))




        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))




        user_id = d.pop("userId")

        ip_address = d.pop("ipAddress", UNSET)

        user_agent = d.pop("userAgent", UNSET)

        session = cls(
            id=id,
            expires_at=expires_at,
            token=token,
            created_at=created_at,
            updated_at=updated_at,
            user_id=user_id,
            ip_address=ip_address,
            user_agent=user_agent,
        )


        session.additional_properties = d
        return session

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
