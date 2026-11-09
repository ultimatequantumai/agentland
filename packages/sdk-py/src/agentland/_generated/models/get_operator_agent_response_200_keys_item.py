from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetOperatorAgentResponse200KeysItem")



@_attrs_define
class GetOperatorAgentResponse200KeysItem:
    """ 
        Attributes:
            kid (str):
            kind (str):
            status (str):
            created_at (str):
     """

    kid: str
    kind: str
    status: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        kid = self.kid

        kind = self.kind

        status = self.status

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kid": kid,
            "kind": kind,
            "status": status,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kid = d.pop("kid")

        kind = d.pop("kind")

        status = d.pop("status")

        created_at = d.pop("created_at")

        get_operator_agent_response_200_keys_item = cls(
            kid=kid,
            kind=kind,
            status=status,
            created_at=created_at,
        )

        return get_operator_agent_response_200_keys_item

