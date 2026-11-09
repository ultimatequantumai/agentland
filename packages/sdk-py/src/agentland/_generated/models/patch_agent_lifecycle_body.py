from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.patch_agent_lifecycle_body_status import PatchAgentLifecycleBodyStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.patch_agent_lifecycle_body_statement import PatchAgentLifecycleBodyStatement





T = TypeVar("T", bound="PatchAgentLifecycleBody")



@_attrs_define
class PatchAgentLifecycleBody:
    """ 
        Attributes:
            status (PatchAgentLifecycleBodyStatus):
            statement (PatchAgentLifecycleBodyStatement | Unset):
            signature (str | Unset):
            purge (bool | Unset):  Default: False.
     """

    status: PatchAgentLifecycleBodyStatus
    statement: PatchAgentLifecycleBodyStatement | Unset = UNSET
    signature: str | Unset = UNSET
    purge: bool | Unset = False





    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_agent_lifecycle_body_statement import PatchAgentLifecycleBodyStatement # noqa: PLC0415
        status = self.status.value

        statement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.statement, Unset):
            statement = self.statement.to_dict()

        signature = self.signature

        purge = self.purge


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
        })
        if statement is not UNSET:
            field_dict["statement"] = statement
        if signature is not UNSET:
            field_dict["signature"] = signature
        if purge is not UNSET:
            field_dict["purge"] = purge

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_agent_lifecycle_body_statement import PatchAgentLifecycleBodyStatement # noqa: PLC0415
        d = dict(src_dict)
        status = PatchAgentLifecycleBodyStatus(d.pop("status"))




        _statement = d.pop("statement", UNSET)
        statement: PatchAgentLifecycleBodyStatement | Unset
        if isinstance(_statement,  Unset):
            statement = UNSET
        else:
            statement = PatchAgentLifecycleBodyStatement.from_dict(_statement)




        signature = d.pop("signature", UNSET)

        purge = d.pop("purge", UNSET)

        patch_agent_lifecycle_body = cls(
            status=status,
            statement=statement,
            signature=signature,
            purge=purge,
        )

        return patch_agent_lifecycle_body

