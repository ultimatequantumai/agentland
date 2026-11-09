from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetVaultHeadResponse200")



@_attrs_define
class GetVaultHeadResponse200:
    """ 
        Attributes:
            did (str):
            seq (str):
            head_hash (str):
            ts (str):
            kid (str):
            sig (str):
     """

    did: str
    seq: str
    head_hash: str
    ts: str
    kid: str
    sig: str





    def to_dict(self) -> dict[str, Any]:
        did = self.did

        seq = self.seq

        head_hash = self.head_hash

        ts = self.ts

        kid = self.kid

        sig = self.sig


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "did": did,
            "seq": seq,
            "head_hash": head_hash,
            "ts": ts,
            "kid": kid,
            "sig": sig,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        did = d.pop("did")

        seq = d.pop("seq")

        head_hash = d.pop("head_hash")

        ts = d.pop("ts")

        kid = d.pop("kid")

        sig = d.pop("sig")

        get_vault_head_response_200 = cls(
            did=did,
            seq=seq,
            head_hash=head_hash,
            ts=ts,
            kid=kid,
            sig=sig,
        )

        return get_vault_head_response_200

