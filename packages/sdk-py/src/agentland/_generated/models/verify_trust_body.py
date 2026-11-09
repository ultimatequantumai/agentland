from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="VerifyTrustBody")



@_attrs_define
class VerifyTrustBody:
    """ 
        Attributes:
            did (str):
            nonce (str):
            signature (str):
     """

    did: str
    nonce: str
    signature: str





    def to_dict(self) -> dict[str, Any]:
        did = self.did

        nonce = self.nonce

        signature = self.signature


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "did": did,
            "nonce": nonce,
            "signature": signature,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        did = d.pop("did")

        nonce = d.pop("nonce")

        signature = d.pop("signature")

        verify_trust_body = cls(
            did=did,
            nonce=nonce,
            signature=signature,
        )

        return verify_trust_body

