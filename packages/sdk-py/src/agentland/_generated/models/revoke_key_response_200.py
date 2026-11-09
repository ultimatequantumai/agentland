from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="RevokeKeyResponse200")



@_attrs_define
class RevokeKeyResponse200:
    """ 
        Attributes:
            key_id (UUID):
            revoked (bool):
     """

    key_id: UUID
    revoked: bool





    def to_dict(self) -> dict[str, Any]:
        key_id = str(self.key_id)

        revoked = self.revoked


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key_id": key_id,
            "revoked": revoked,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_id = UUID(d.pop("key_id"))




        revoked = d.pop("revoked")

        revoke_key_response_200 = cls(
            key_id=key_id,
            revoked=revoked,
        )

        return revoke_key_response_200

