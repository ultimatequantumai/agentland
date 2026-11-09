from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.error_envelope_error import ErrorEnvelopeError





T = TypeVar("T", bound="ErrorEnvelope")



@_attrs_define
class ErrorEnvelope:
    """ 
        Attributes:
            error (ErrorEnvelopeError):
     """

    error: ErrorEnvelopeError





    def to_dict(self) -> dict[str, Any]:
        from ..models.error_envelope_error import ErrorEnvelopeError # noqa: PLC0415
        error = self.error.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "error": error,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_envelope_error import ErrorEnvelopeError # noqa: PLC0415
        d = dict(src_dict)
        error = ErrorEnvelopeError.from_dict(d.pop("error"))




        error_envelope = cls(
            error=error,
        )

        return error_envelope

