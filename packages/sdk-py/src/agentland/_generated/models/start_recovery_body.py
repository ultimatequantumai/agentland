from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.start_recovery_body_new_public_key import StartRecoveryBodyNewPublicKey





T = TypeVar("T", bound="StartRecoveryBody")



@_attrs_define
class StartRecoveryBody:
    """ 
        Attributes:
            new_public_key (StartRecoveryBodyNewPublicKey):
            nonce (str):
            proof_of_possession (str):
     """

    new_public_key: StartRecoveryBodyNewPublicKey
    nonce: str
    proof_of_possession: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.start_recovery_body_new_public_key import StartRecoveryBodyNewPublicKey # noqa: PLC0415
        new_public_key = self.new_public_key.to_dict()

        nonce = self.nonce

        proof_of_possession = self.proof_of_possession


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "new_public_key": new_public_key,
            "nonce": nonce,
            "proof_of_possession": proof_of_possession,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.start_recovery_body_new_public_key import StartRecoveryBodyNewPublicKey # noqa: PLC0415
        d = dict(src_dict)
        new_public_key = StartRecoveryBodyNewPublicKey.from_dict(d.pop("new_public_key"))




        nonce = d.pop("nonce")

        proof_of_possession = d.pop("proof_of_possession")

        start_recovery_body = cls(
            new_public_key=new_public_key,
            nonce=nonce,
            proof_of_possession=proof_of_possession,
        )

        return start_recovery_body

