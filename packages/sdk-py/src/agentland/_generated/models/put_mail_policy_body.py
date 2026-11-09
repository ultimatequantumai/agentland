from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PutMailPolicyBody")



@_attrs_define
class PutMailPolicyBody:
    """ 
        Attributes:
            allowlist (list[str]):
            denylist (list[str]):
     """

    allowlist: list[str]
    denylist: list[str]





    def to_dict(self) -> dict[str, Any]:
        allowlist = self.allowlist



        denylist = self.denylist




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "allowlist": allowlist,
            "denylist": denylist,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowlist = cast(list[str], d.pop("allowlist"))


        denylist = cast(list[str], d.pop("denylist"))


        put_mail_policy_body = cls(
            allowlist=allowlist,
            denylist=denylist,
        )

        return put_mail_policy_body

