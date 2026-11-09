from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.error_envelope_error_code import ErrorEnvelopeErrorCode
from ..types import UNSET, Unset






T = TypeVar("T", bound="ErrorEnvelopeError")



@_attrs_define
class ErrorEnvelopeError:
    """ 
        Attributes:
            code (ErrorEnvelopeErrorCode):
            message (str):
            request_id (str):
            details (Any | Unset):
     """

    code: ErrorEnvelopeErrorCode
    message: str
    request_id: str
    details: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        request_id = self.request_id

        details = self.details


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "code": code,
            "message": message,
            "request_id": request_id,
        })
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = ErrorEnvelopeErrorCode(d.pop("code"))




        message = d.pop("message")

        request_id = d.pop("request_id")

        details = d.pop("details", UNSET)

        error_envelope_error = cls(
            code=code,
            message=message,
            request_id=request_id,
            details=details,
        )

        return error_envelope_error

