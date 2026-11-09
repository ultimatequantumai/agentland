from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.patch_agent_lifecycle_body_statement_kind import PatchAgentLifecycleBodyStatementKind
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.patch_agent_lifecycle_body_statement_from import PatchAgentLifecycleBodyStatementFrom
  from ..models.patch_agent_lifecycle_body_statement_to import PatchAgentLifecycleBodyStatementTo





T = TypeVar("T", bound="PatchAgentLifecycleBodyStatement")



@_attrs_define
class PatchAgentLifecycleBodyStatement:
    """ 
        Attributes:
            did (str):
            kind (PatchAgentLifecycleBodyStatementKind):
            to (PatchAgentLifecycleBodyStatementTo):
            note (str):
            ts (str):
            from_ (PatchAgentLifecycleBodyStatementFrom | Unset):
     """

    did: str
    kind: PatchAgentLifecycleBodyStatementKind
    to: PatchAgentLifecycleBodyStatementTo
    note: str
    ts: str
    from_: PatchAgentLifecycleBodyStatementFrom | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_agent_lifecycle_body_statement_from import PatchAgentLifecycleBodyStatementFrom # noqa: PLC0415
        from ..models.patch_agent_lifecycle_body_statement_to import PatchAgentLifecycleBodyStatementTo # noqa: PLC0415
        did = self.did

        kind = self.kind.value

        to = self.to.to_dict()

        note = self.note

        ts = self.ts

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "did": did,
            "kind": kind,
            "to": to,
            "note": note,
            "ts": ts,
        })
        if from_ is not UNSET:
            field_dict["from"] = from_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_agent_lifecycle_body_statement_from import PatchAgentLifecycleBodyStatementFrom # noqa: PLC0415
        from ..models.patch_agent_lifecycle_body_statement_to import PatchAgentLifecycleBodyStatementTo # noqa: PLC0415
        d = dict(src_dict)
        did = d.pop("did")

        kind = PatchAgentLifecycleBodyStatementKind(d.pop("kind"))




        to = PatchAgentLifecycleBodyStatementTo.from_dict(d.pop("to"))




        note = d.pop("note")

        ts = d.pop("ts")

        _from_ = d.pop("from", UNSET)
        from_: PatchAgentLifecycleBodyStatementFrom | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = PatchAgentLifecycleBodyStatementFrom.from_dict(_from_)




        patch_agent_lifecycle_body_statement = cls(
            did=did,
            kind=kind,
            to=to,
            note=note,
            ts=ts,
            from_=from_,
        )

        return patch_agent_lifecycle_body_statement

