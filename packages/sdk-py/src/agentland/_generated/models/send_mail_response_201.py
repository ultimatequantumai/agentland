from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.send_mail_response_201_status import SendMailResponse201Status






T = TypeVar("T", bound="SendMailResponse201")



@_attrs_define
class SendMailResponse201:
    """ 
        Attributes:
            status (SendMailResponse201Status):
            accepted_at (str):
     """

    status: SendMailResponse201Status
    accepted_at: str





    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        accepted_at = self.accepted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "accepted_at": accepted_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = SendMailResponse201Status(d.pop("status"))




        accepted_at = d.pop("accepted_at")

        send_mail_response_201 = cls(
            status=status,
            accepted_at=accepted_at,
        )

        return send_mail_response_201

