from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="TwoFactor")



@_attrs_define
class TwoFactor:
    """ 
        Attributes:
            id (str):
            secret (str | Unset):
            backup_codes (str | Unset):
            user_id (str | Unset):
            verified (bool | Unset):  Default: True.
            failed_verification_count (float | Unset):  Default: 0.0.
            locked_until (datetime.datetime | Unset):
     """

    id: str
    secret: str | Unset = UNSET
    backup_codes: str | Unset = UNSET
    user_id: str | Unset = UNSET
    verified: bool | Unset = True
    failed_verification_count: float | Unset = 0.0
    locked_until: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        secret = self.secret

        backup_codes = self.backup_codes

        user_id = self.user_id

        verified = self.verified

        failed_verification_count = self.failed_verification_count

        locked_until: str | Unset = UNSET
        if not isinstance(self.locked_until, Unset):
            locked_until = self.locked_until.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
        })
        if secret is not UNSET:
            field_dict["secret"] = secret
        if backup_codes is not UNSET:
            field_dict["backupCodes"] = backup_codes
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if verified is not UNSET:
            field_dict["verified"] = verified
        if failed_verification_count is not UNSET:
            field_dict["failedVerificationCount"] = failed_verification_count
        if locked_until is not UNSET:
            field_dict["lockedUntil"] = locked_until

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        secret = d.pop("secret", UNSET)

        backup_codes = d.pop("backupCodes", UNSET)

        user_id = d.pop("userId", UNSET)

        verified = d.pop("verified", UNSET)

        failed_verification_count = d.pop("failedVerificationCount", UNSET)

        _locked_until = d.pop("lockedUntil", UNSET)
        locked_until: datetime.datetime | Unset
        if isinstance(_locked_until,  Unset):
            locked_until = UNSET
        else:
            locked_until = datetime.datetime.fromisoformat(_locked_until)




        two_factor = cls(
            id=id,
            secret=secret,
            backup_codes=backup_codes,
            user_id=user_id,
            verified=verified,
            failed_verification_count=failed_verification_count,
            locked_until=locked_until,
        )


        two_factor.additional_properties = d
        return two_factor

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
