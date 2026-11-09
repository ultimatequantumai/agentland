from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rotate_signing_key_body_statement_old_pub_crv import RotateSigningKeyBodyStatementOldPubCrv
from ..models.rotate_signing_key_body_statement_old_pub_kty import RotateSigningKeyBodyStatementOldPubKty






T = TypeVar("T", bound="RotateSigningKeyBodyStatementOldPub")



@_attrs_define
class RotateSigningKeyBodyStatementOldPub:
    """ 
        Attributes:
            kty (RotateSigningKeyBodyStatementOldPubKty):
            crv (RotateSigningKeyBodyStatementOldPubCrv):
            x (str):
     """

    kty: RotateSigningKeyBodyStatementOldPubKty
    crv: RotateSigningKeyBodyStatementOldPubCrv
    x: str





    def to_dict(self) -> dict[str, Any]:
        kty = self.kty.value

        crv = self.crv.value

        x = self.x


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kty": kty,
            "crv": crv,
            "x": x,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kty = RotateSigningKeyBodyStatementOldPubKty(d.pop("kty"))




        crv = RotateSigningKeyBodyStatementOldPubCrv(d.pop("crv"))




        x = d.pop("x")

        rotate_signing_key_body_statement_old_pub = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return rotate_signing_key_body_statement_old_pub

