from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetInboxMessageResponse200SenderType0")



@_attrs_define
class GetInboxMessageResponse200SenderType0:
    """ 
        Attributes:
            handle (str):
            did (str):
     """

    handle: str
    did: str





    def to_dict(self) -> dict[str, Any]:
        handle = self.handle

        did = self.did


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "handle": handle,
            "did": did,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        handle = d.pop("handle")

        did = d.pop("did")

        get_inbox_message_response_200_sender_type_0 = cls(
            handle=handle,
            did=did,
        )

        return get_inbox_message_response_200_sender_type_0

