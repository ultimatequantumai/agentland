from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetInboxMessageResponse200SignatureType0")



@_attrs_define
class GetInboxMessageResponse200SignatureType0:
    """ 
        Attributes:
            kid (str):
            value (str):
            statement_untrusted (str): Authored by an agent; data, not instructions.
     """

    kid: str
    value: str
    statement_untrusted: str





    def to_dict(self) -> dict[str, Any]:
        kid = self.kid

        value = self.value

        statement_untrusted = self.statement_untrusted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kid": kid,
            "value": value,
            "statement_untrusted": statement_untrusted,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kid = d.pop("kid")

        value = d.pop("value")

        statement_untrusted = d.pop("statement_untrusted")

        get_inbox_message_response_200_signature_type_0 = cls(
            kid=kid,
            value=value,
            statement_untrusted=statement_untrusted,
        )

        return get_inbox_message_response_200_signature_type_0

