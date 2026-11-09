from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rotate_signing_key_response_201_type_0_key_custody import RotateSigningKeyResponse201Type0KeyCustody
from ..models.rotate_signing_key_response_201_type_0_key_kind import RotateSigningKeyResponse201Type0KeyKind
from ..models.rotate_signing_key_response_201_type_0_key_status import RotateSigningKeyResponse201Type0KeyStatus
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rotate_signing_key_response_201_type_0_key_public_key import RotateSigningKeyResponse201Type0KeyPublicKey





T = TypeVar("T", bound="RotateSigningKeyResponse201Type0Key")



@_attrs_define
class RotateSigningKeyResponse201Type0Key:
    """ 
        Attributes:
            id (str):
            key_id (UUID):
            kind (RotateSigningKeyResponse201Type0KeyKind):
            public_key (RotateSigningKeyResponse201Type0KeyPublicKey):
            custody (RotateSigningKeyResponse201Type0KeyCustody):
            status (RotateSigningKeyResponse201Type0KeyStatus):
            seq (int):
            created_at (str):
     """

    id: str
    key_id: UUID
    kind: RotateSigningKeyResponse201Type0KeyKind
    public_key: RotateSigningKeyResponse201Type0KeyPublicKey
    custody: RotateSigningKeyResponse201Type0KeyCustody
    status: RotateSigningKeyResponse201Type0KeyStatus
    seq: int
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.rotate_signing_key_response_201_type_0_key_public_key import RotateSigningKeyResponse201Type0KeyPublicKey # noqa: PLC0415
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
        from ..models.rotate_signing_key_response_201_type_0_key_public_key import RotateSigningKeyResponse201Type0KeyPublicKey # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        key_id = UUID(d.pop("key_id"))




        kind = RotateSigningKeyResponse201Type0KeyKind(d.pop("kind"))




        public_key = RotateSigningKeyResponse201Type0KeyPublicKey.from_dict(d.pop("public_key"))




        custody = RotateSigningKeyResponse201Type0KeyCustody(d.pop("custody"))




        status = RotateSigningKeyResponse201Type0KeyStatus(d.pop("status"))




        seq = d.pop("seq")

        created_at = d.pop("created_at")

        rotate_signing_key_response_201_type_0_key = cls(
            id=id,
            key_id=key_id,
            kind=kind,
            public_key=public_key,
            custody=custody,
            status=status,
            seq=seq,
            created_at=created_at,
        )

        return rotate_signing_key_response_201_type_0_key

