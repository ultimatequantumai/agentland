from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rotate_signing_key_body_new_public_key import RotateSigningKeyBodyNewPublicKey
  from ..models.rotate_signing_key_body_statement import RotateSigningKeyBodyStatement





T = TypeVar("T", bound="RotateSigningKeyBody")



@_attrs_define
class RotateSigningKeyBody:
    """ 
        Attributes:
            new_public_key (RotateSigningKeyBodyNewPublicKey):
            statement (RotateSigningKeyBodyStatement):
            sig_old (str | Unset):
            sig_new (str | Unset):
     """

    new_public_key: RotateSigningKeyBodyNewPublicKey
    statement: RotateSigningKeyBodyStatement
    sig_old: str | Unset = UNSET
    sig_new: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.rotate_signing_key_body_new_public_key import RotateSigningKeyBodyNewPublicKey # noqa: PLC0415
        from ..models.rotate_signing_key_body_statement import RotateSigningKeyBodyStatement # noqa: PLC0415
        new_public_key = self.new_public_key.to_dict()

        statement = self.statement.to_dict()

        sig_old = self.sig_old

        sig_new = self.sig_new


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "new_public_key": new_public_key,
            "statement": statement,
        })
        if sig_old is not UNSET:
            field_dict["sig_old"] = sig_old
        if sig_new is not UNSET:
            field_dict["sig_new"] = sig_new

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rotate_signing_key_body_new_public_key import RotateSigningKeyBodyNewPublicKey # noqa: PLC0415
        from ..models.rotate_signing_key_body_statement import RotateSigningKeyBodyStatement # noqa: PLC0415
        d = dict(src_dict)
        new_public_key = RotateSigningKeyBodyNewPublicKey.from_dict(d.pop("new_public_key"))




        statement = RotateSigningKeyBodyStatement.from_dict(d.pop("statement"))




        sig_old = d.pop("sig_old", UNSET)

        sig_new = d.pop("sig_new", UNSET)

        rotate_signing_key_body = cls(
            new_public_key=new_public_key,
            statement=statement,
            sig_old=sig_old,
            sig_new=sig_new,
        )

        return rotate_signing_key_body

