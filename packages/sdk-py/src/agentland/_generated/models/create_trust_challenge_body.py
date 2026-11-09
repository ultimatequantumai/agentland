from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_trust_challenge_body_purpose import CreateTrustChallengeBodyPurpose
from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateTrustChallengeBody")



@_attrs_define
class CreateTrustChallengeBody:
    """ 
        Attributes:
            did (str):
            purpose (CreateTrustChallengeBodyPurpose | Unset):  Default: CreateTrustChallengeBodyPurpose.VERIFY.
     """

    did: str
    purpose: CreateTrustChallengeBodyPurpose | Unset = CreateTrustChallengeBodyPurpose.VERIFY





    def to_dict(self) -> dict[str, Any]:
        did = self.did

        purpose: str | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "did": did,
        })
        if purpose is not UNSET:
            field_dict["purpose"] = purpose

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        did = d.pop("did")

        _purpose = d.pop("purpose", UNSET)
        purpose: CreateTrustChallengeBodyPurpose | Unset
        if isinstance(_purpose,  Unset):
            purpose = UNSET
        else:
            purpose = CreateTrustChallengeBodyPurpose(_purpose)




        create_trust_challenge_body = cls(
            did=did,
            purpose=purpose,
        )

        return create_trust_challenge_body

