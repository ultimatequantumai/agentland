from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rotate_signing_key_body_statement_new_pub_crv import RotateSigningKeyBodyStatementNewPubCrv
from ..models.rotate_signing_key_body_statement_new_pub_kty import RotateSigningKeyBodyStatementNewPubKty






T = TypeVar("T", bound="RotateSigningKeyBodyStatementNewPub")



@_attrs_define
class RotateSigningKeyBodyStatementNewPub:
    """ 
        Attributes:
            kty (RotateSigningKeyBodyStatementNewPubKty):
            crv (RotateSigningKeyBodyStatementNewPubCrv):
            x (str):
     """

    kty: RotateSigningKeyBodyStatementNewPubKty
    crv: RotateSigningKeyBodyStatementNewPubCrv
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
        kty = RotateSigningKeyBodyStatementNewPubKty(d.pop("kty"))




        crv = RotateSigningKeyBodyStatementNewPubCrv(d.pop("crv"))




        x = d.pop("x")

        rotate_signing_key_body_statement_new_pub = cls(
            kty=kty,
            crv=crv,
            x=x,
        )

        return rotate_signing_key_body_statement_new_pub

