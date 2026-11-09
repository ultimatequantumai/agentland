from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SendMailBody")



@_attrs_define
class SendMailBody:
    """ 
        Attributes:
            to (str):
            subject (str):
            text (str):
     """

    to: str
    subject: str
    text: str





    def to_dict(self) -> dict[str, Any]:
        to = self.to

        subject = self.subject

        text = self.text


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "to": to,
            "subject": subject,
            "text": text,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        to = d.pop("to")

        subject = d.pop("subject")

        text = d.pop("text")

        send_mail_body = cls(
            to=to,
            subject=subject,
            text=text,
        )

        return send_mail_body

