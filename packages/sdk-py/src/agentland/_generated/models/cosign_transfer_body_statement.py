from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.cosign_transfer_body_statement_kind import CosignTransferBodyStatementKind
from uuid import UUID






T = TypeVar("T", bound="CosignTransferBodyStatement")



@_attrs_define
class CosignTransferBodyStatement:
    """ 
        Attributes:
            did (str):
            kind (CosignTransferBodyStatementKind):
            transfer_id (UUID):
            from_operator_id (UUID):
            to_operator_id (UUID):
            ts (str):
     """

    did: str
    kind: CosignTransferBodyStatementKind
    transfer_id: UUID
    from_operator_id: UUID
    to_operator_id: UUID
    ts: str





    def to_dict(self) -> dict[str, Any]:
        did = self.did

        kind = self.kind.value

        transfer_id = str(self.transfer_id)

        from_operator_id = str(self.from_operator_id)

        to_operator_id = str(self.to_operator_id)

        ts = self.ts


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "did": did,
            "kind": kind,
            "transfer_id": transfer_id,
            "from_operator_id": from_operator_id,
            "to_operator_id": to_operator_id,
            "ts": ts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        did = d.pop("did")

        kind = CosignTransferBodyStatementKind(d.pop("kind"))




        transfer_id = UUID(d.pop("transfer_id"))




        from_operator_id = UUID(d.pop("from_operator_id"))




        to_operator_id = UUID(d.pop("to_operator_id"))




        ts = d.pop("ts")

        cosign_transfer_body_statement = cls(
            did=did,
            kind=kind,
            transfer_id=transfer_id,
            from_operator_id=from_operator_id,
            to_operator_id=to_operator_id,
            ts=ts,
        )

        return cosign_transfer_body_statement

