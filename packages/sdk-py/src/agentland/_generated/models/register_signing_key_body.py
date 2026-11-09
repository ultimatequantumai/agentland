from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.register_signing_key_body_kind import RegisterSigningKeyBodyKind
from typing import cast

if TYPE_CHECKING:
  from ..models.register_signing_key_body_public_key import RegisterSigningKeyBodyPublicKey





T = TypeVar("T", bound="RegisterSigningKeyBody")



@_attrs_define
class RegisterSigningKeyBody:
    """ 
        Attributes:
            kind (RegisterSigningKeyBodyKind):
            public_key (RegisterSigningKeyBodyPublicKey):
            nonce (str):
            proof_of_possession (str):
     """

    kind: RegisterSigningKeyBodyKind
    public_key: RegisterSigningKeyBodyPublicKey
    nonce: str
    proof_of_possession: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.register_signing_key_body_public_key import RegisterSigningKeyBodyPublicKey # noqa: PLC0415
        kind = self.kind.value

        public_key = self.public_key.to_dict()

        nonce = self.nonce

        proof_of_possession = self.proof_of_possession


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
            "public_key": public_key,
            "nonce": nonce,
            "proof_of_possession": proof_of_possession,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.register_signing_key_body_public_key import RegisterSigningKeyBodyPublicKey # noqa: PLC0415
        d = dict(src_dict)
        kind = RegisterSigningKeyBodyKind(d.pop("kind"))




        public_key = RegisterSigningKeyBodyPublicKey.from_dict(d.pop("public_key"))




        nonce = d.pop("nonce")

        proof_of_possession = d.pop("proof_of_possession")

        register_signing_key_body = cls(
            kind=kind,
            public_key=public_key,
            nonce=nonce,
            proof_of_possession=proof_of_possession,
        )

        return register_signing_key_body

