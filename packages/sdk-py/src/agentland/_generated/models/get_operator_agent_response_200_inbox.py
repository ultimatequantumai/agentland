from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetOperatorAgentResponse200Inbox")



@_attrs_define
class GetOperatorAgentResponse200Inbox:
    """ 
        Attributes:
            total (int):
            unread (int):
            latest_received_at (None | str):
     """

    total: int
    unread: int
    latest_received_at: None | str





    def to_dict(self) -> dict[str, Any]:
        total = self.total

        unread = self.unread

        latest_received_at: None | str
        latest_received_at = self.latest_received_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "total": total,
            "unread": unread,
            "latest_received_at": latest_received_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        unread = d.pop("unread")

        def _parse_latest_received_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        latest_received_at = _parse_latest_received_at(d.pop("latest_received_at"))


        get_operator_agent_response_200_inbox = cls(
            total=total,
            unread=unread,
            latest_received_at=latest_received_at,
        )

        return get_operator_agent_response_200_inbox

