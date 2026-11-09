from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rotate_signing_key_response_201_type_0_status import RotateSigningKeyResponse201Type0Status
from typing import cast

if TYPE_CHECKING:
  from ..models.rotate_signing_key_response_201_type_0_key import RotateSigningKeyResponse201Type0Key





T = TypeVar("T", bound="RotateSigningKeyResponse201Type0")



@_attrs_define
class RotateSigningKeyResponse201Type0:
    """ 
        Attributes:
            status (RotateSigningKeyResponse201Type0Status):
            key (RotateSigningKeyResponse201Type0Key):
            challenge (None):
     """

    status: RotateSigningKeyResponse201Type0Status
    key: RotateSigningKeyResponse201Type0Key
    challenge: None





    def to_dict(self) -> dict[str, Any]:
        from ..models.rotate_signing_key_response_201_type_0_key import RotateSigningKeyResponse201Type0Key # noqa: PLC0415
        status = self.status.value

        key = self.key.to_dict()

        challenge = self.challenge


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "key": key,
            "challenge": challenge,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rotate_signing_key_response_201_type_0_key import RotateSigningKeyResponse201Type0Key # noqa: PLC0415
        d = dict(src_dict)
        status = RotateSigningKeyResponse201Type0Status(d.pop("status"))




        key = RotateSigningKeyResponse201Type0Key.from_dict(d.pop("key"))




        challenge = d.pop("challenge")

        rotate_signing_key_response_201_type_0 = cls(
            status=status,
            key=key,
            challenge=challenge,
        )

        return rotate_signing_key_response_201_type_0

