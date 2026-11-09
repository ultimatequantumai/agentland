from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_mail_policy_response_200_outbound_daily_limit import GetMailPolicyResponse200OutboundDailyLimit
from typing import cast






T = TypeVar("T", bound="GetMailPolicyResponse200")



@_attrs_define
class GetMailPolicyResponse200:
    """ 
        Attributes:
            allowlist (list[str]):
            denylist (list[str]):
            outbound_enabled (bool):
            outbound_daily_limit (GetMailPolicyResponse200OutboundDailyLimit):
     """

    allowlist: list[str]
    denylist: list[str]
    outbound_enabled: bool
    outbound_daily_limit: GetMailPolicyResponse200OutboundDailyLimit





    def to_dict(self) -> dict[str, Any]:
        allowlist = self.allowlist



        denylist = self.denylist



        outbound_enabled = self.outbound_enabled

        outbound_daily_limit = self.outbound_daily_limit.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "allowlist": allowlist,
            "denylist": denylist,
            "outbound_enabled": outbound_enabled,
            "outbound_daily_limit": outbound_daily_limit,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowlist = cast(list[str], d.pop("allowlist"))


        denylist = cast(list[str], d.pop("denylist"))


        outbound_enabled = d.pop("outbound_enabled")

        outbound_daily_limit = GetMailPolicyResponse200OutboundDailyLimit(d.pop("outbound_daily_limit"))




        get_mail_policy_response_200 = cls(
            allowlist=allowlist,
            denylist=denylist,
            outbound_enabled=outbound_enabled,
            outbound_daily_limit=outbound_daily_limit,
        )

        return get_mail_policy_response_200

