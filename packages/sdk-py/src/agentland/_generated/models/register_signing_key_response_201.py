from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.register_signing_key_response_201_custody import RegisterSigningKeyResponse201Custody
from ..models.register_signing_key_response_201_kind import RegisterSigningKeyResponse201Kind
from ..models.register_signing_key_response_201_status import RegisterSigningKeyResponse201Status
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.register_signing_key_response_201_public_key import RegisterSigningKeyResponse201PublicKey





T = TypeVar("T", bound="RegisterSigningKeyResponse201")



@_attrs_define
class RegisterSigningKeyResponse201:
    """ 
        Attributes:
            id (str):
            key_id (UUID):
            kind (RegisterSigningKeyResponse201Kind):
            public_key (RegisterSigningKeyResponse201PublicKey):
            custody (RegisterSigningKeyResponse201Custody):
            status (RegisterSigningKeyResponse201Status):
            seq (int):
            created_at (str):
     """

    id: str
    key_id: UUID
    kind: RegisterSigningKeyResponse201Kind
    public_key: RegisterSigningKeyResponse201PublicKey
    custody: RegisterSigningKeyResponse201Custody
    status: RegisterSigningKeyResponse201Status
    seq: int
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.register_signing_key_response_201_public_key import RegisterSigningKeyResponse201PublicKey # noqa: PLC0415
        id = self.id

        key_id = str(self.key_id)

        kind = self.kind.value

        public_key = self.public_key.to_dict()

        custody = self.custody.value

        status = self.status.value

        seq = self.seq

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "key_id": key_id,
            "kind": kind,
            "public_key": public_key,
            "custody": custody,
            "status": status,
            "seq": seq,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.register_signing_key_response_201_public_key import RegisterSigningKeyResponse201PublicKey # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        key_id = UUID(d.pop("key_id"))




        kind = RegisterSigningKeyResponse201Kind(d.pop("kind"))




        public_key = RegisterSigningKeyResponse201PublicKey.from_dict(d.pop("public_key"))




        custody = RegisterSigningKeyResponse201Custody(d.pop("custody"))




        status = RegisterSigningKeyResponse201Status(d.pop("status"))




        seq = d.pop("seq")

        created_at = d.pop("created_at")

        register_signing_key_response_201 = cls(
            id=id,
            key_id=key_id,
            kind=kind,
            public_key=public_key,
            custody=custody,
            status=status,
            seq=seq,
            created_at=created_at,
        )

        return register_signing_key_response_201

