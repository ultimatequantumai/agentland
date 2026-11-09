from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="Passkey")



@_attrs_define
class Passkey:
    """ 
        Attributes:
            id (str):
            public_key (str):
            user_id (str):
            credential_id (str):
            counter (float):
            device_type (str):
            backed_up (bool):
            name (str | Unset):
            transports (str | Unset):
            created_at (datetime.datetime | Unset):
            aaguid (str | Unset):
     """

    id: str
    public_key: str
    user_id: str
    credential_id: str
    counter: float
    device_type: str
    backed_up: bool
    name: str | Unset = UNSET
    transports: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    aaguid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        public_key = self.public_key

        user_id = self.user_id

        credential_id = self.credential_id

        counter = self.counter

        device_type = self.device_type

        backed_up = self.backed_up

        name = self.name

        transports = self.transports

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        aaguid = self.aaguid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "publicKey": public_key,
            "userId": user_id,
            "credentialID": credential_id,
            "counter": counter,
            "deviceType": device_type,
            "backedUp": backed_up,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if transports is not UNSET:
            field_dict["transports"] = transports
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if aaguid is not UNSET:
            field_dict["aaguid"] = aaguid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        public_key = d.pop("publicKey")

        user_id = d.pop("userId")

        credential_id = d.pop("credentialID")

        counter = d.pop("counter")

        device_type = d.pop("deviceType")

        backed_up = d.pop("backedUp")

        name = d.pop("name", UNSET)

        transports = d.pop("transports", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        aaguid = d.pop("aaguid", UNSET)

        passkey = cls(
            id=id,
            public_key=public_key,
            user_id=user_id,
            credential_id=credential_id,
            counter=counter,
            device_type=device_type,
            backed_up=backed_up,
            name=name,
            transports=transports,
            created_at=created_at,
            aaguid=aaguid,
        )


        passkey.additional_properties = d
        return passkey

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
