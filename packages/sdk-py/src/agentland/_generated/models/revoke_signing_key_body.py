from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="RevokeSigningKeyBody")



@_attrs_define
class RevokeSigningKeyBody:
    """ 
        Attributes:
            key_id (UUID):
            reason (str):
            timestamp (str):
            signature (str | Unset):
     """

    key_id: UUID
    reason: str
    timestamp: str
    signature: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        key_id = str(self.key_id)

        reason = self.reason

        timestamp = self.timestamp

        signature = self.signature


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key_id": key_id,
            "reason": reason,
            "timestamp": timestamp,
        })
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_id = UUID(d.pop("key_id"))




        reason = d.pop("reason")

        timestamp = d.pop("timestamp")

        signature = d.pop("signature", UNSET)

        revoke_signing_key_body = cls(
            key_id=key_id,
            reason=reason,
            timestamp=timestamp,
            signature=signature,
        )

        return revoke_signing_key_body

