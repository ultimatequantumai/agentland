from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ReceiveResendWebhookResponse200")



@_attrs_define
class ReceiveResendWebhookResponse200:
    """ 
        Attributes:
            received (bool):
     """

    received: bool





    def to_dict(self) -> dict[str, Any]:
        received = self.received


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "received": received,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        received = d.pop("received")

        receive_resend_webhook_response_200 = cls(
            received=received,
        )

        return receive_resend_webhook_response_200

