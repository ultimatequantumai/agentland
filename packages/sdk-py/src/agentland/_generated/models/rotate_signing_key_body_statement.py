from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.rotate_signing_key_body_statement_new_pub import RotateSigningKeyBodyStatementNewPub
  from ..models.rotate_signing_key_body_statement_old_pub import RotateSigningKeyBodyStatementOldPub





T = TypeVar("T", bound="RotateSigningKeyBodyStatement")



@_attrs_define
class RotateSigningKeyBodyStatement:
    """ 
        Attributes:
            old_pub (RotateSigningKeyBodyStatementOldPub):
            new_pub (RotateSigningKeyBodyStatementNewPub):
            reason (str):
            timestamp (str):
     """

    old_pub: RotateSigningKeyBodyStatementOldPub
    new_pub: RotateSigningKeyBodyStatementNewPub
    reason: str
    timestamp: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.rotate_signing_key_body_statement_new_pub import RotateSigningKeyBodyStatementNewPub # noqa: PLC0415
        from ..models.rotate_signing_key_body_statement_old_pub import RotateSigningKeyBodyStatementOldPub # noqa: PLC0415
        old_pub = self.old_pub.to_dict()

        new_pub = self.new_pub.to_dict()

        reason = self.reason

        timestamp = self.timestamp


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "old_pub": old_pub,
            "new_pub": new_pub,
            "reason": reason,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rotate_signing_key_body_statement_new_pub import RotateSigningKeyBodyStatementNewPub # noqa: PLC0415
        from ..models.rotate_signing_key_body_statement_old_pub import RotateSigningKeyBodyStatementOldPub # noqa: PLC0415
        d = dict(src_dict)
        old_pub = RotateSigningKeyBodyStatementOldPub.from_dict(d.pop("old_pub"))




        new_pub = RotateSigningKeyBodyStatementNewPub.from_dict(d.pop("new_pub"))




        reason = d.pop("reason")

        timestamp = d.pop("timestamp")

        rotate_signing_key_body_statement = cls(
            old_pub=old_pub,
            new_pub=new_pub,
            reason=reason,
            timestamp=timestamp,
        )

        return rotate_signing_key_body_statement

