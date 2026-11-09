from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.append_lineage_body_kind import AppendLineageBodyKind
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.append_lineage_body_from import AppendLineageBodyFrom
  from ..models.append_lineage_body_to import AppendLineageBodyTo





T = TypeVar("T", bound="AppendLineageBody")



@_attrs_define
class AppendLineageBody:
    """ 
        Attributes:
            kind (AppendLineageBodyKind):
            from_ (AppendLineageBodyFrom):
            to (AppendLineageBodyTo):
            note (str):
            ts (str):
            signature (str | Unset):
     """

    kind: AppendLineageBodyKind
    from_: AppendLineageBodyFrom
    to: AppendLineageBodyTo
    note: str
    ts: str
    signature: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.append_lineage_body_from import AppendLineageBodyFrom # noqa: PLC0415
        from ..models.append_lineage_body_to import AppendLineageBodyTo # noqa: PLC0415
        kind = self.kind.value

        from_ = self.from_.to_dict()

        to = self.to.to_dict()

        note = self.note

        ts = self.ts

        signature = self.signature


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
            "from": from_,
            "to": to,
            "note": note,
            "ts": ts,
        })
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.append_lineage_body_from import AppendLineageBodyFrom # noqa: PLC0415
        from ..models.append_lineage_body_to import AppendLineageBodyTo # noqa: PLC0415
        d = dict(src_dict)
        kind = AppendLineageBodyKind(d.pop("kind"))




        from_ = AppendLineageBodyFrom.from_dict(d.pop("from"))




        to = AppendLineageBodyTo.from_dict(d.pop("to"))




        note = d.pop("note")

        ts = d.pop("ts")

        signature = d.pop("signature", UNSET)

        append_lineage_body = cls(
            kind=kind,
            from_=from_,
            to=to,
            note=note,
            ts=ts,
            signature=signature,
        )

        return append_lineage_body

