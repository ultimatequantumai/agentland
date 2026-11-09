from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cosign_transfer_body_statement import CosignTransferBodyStatement





T = TypeVar("T", bound="CosignTransferBody")



@_attrs_define
class CosignTransferBody:
    """ 
        Attributes:
            statement (CosignTransferBodyStatement):
            signature (str | Unset):
     """

    statement: CosignTransferBodyStatement
    signature: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.cosign_transfer_body_statement import CosignTransferBodyStatement # noqa: PLC0415
        statement = self.statement.to_dict()

        signature = self.signature


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "statement": statement,
        })
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cosign_transfer_body_statement import CosignTransferBodyStatement # noqa: PLC0415
        d = dict(src_dict)
        statement = CosignTransferBodyStatement.from_dict(d.pop("statement"))




        signature = d.pop("signature", UNSET)

        cosign_transfer_body = cls(
            statement=statement,
            signature=signature,
        )

        return cosign_transfer_body

