from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_trust_challenge_response_201_purpose import CreateTrustChallengeResponse201Purpose






T = TypeVar("T", bound="CreateTrustChallengeResponse201")



@_attrs_define
class CreateTrustChallengeResponse201:
    """ 
        Attributes:
            did (str):
            purpose (CreateTrustChallengeResponse201Purpose):
            nonce (str):
            expires_at (str):
     """

    did: str
    purpose: CreateTrustChallengeResponse201Purpose
    nonce: str
    expires_at: str





    def to_dict(self) -> dict[str, Any]:
        did = self.did

        purpose = self.purpose.value

        nonce = self.nonce

        expires_at = self.expires_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "did": did,
            "purpose": purpose,
            "nonce": nonce,
            "expires_at": expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        did = d.pop("did")

        purpose = CreateTrustChallengeResponse201Purpose(d.pop("purpose"))




        nonce = d.pop("nonce")

        expires_at = d.pop("expires_at")

        create_trust_challenge_response_201 = cls(
            did=did,
            purpose=purpose,
            nonce=nonce,
            expires_at=expires_at,
        )

        return create_trust_challenge_response_201

