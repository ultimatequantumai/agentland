from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rotate_signing_key_response_201_type_1_status import RotateSigningKeyResponse201Type1Status
from typing import cast

if TYPE_CHECKING:
  from ..models.rotate_signing_key_response_201_type_1_challenge import RotateSigningKeyResponse201Type1Challenge





T = TypeVar("T", bound="RotateSigningKeyResponse201Type1")



@_attrs_define
class RotateSigningKeyResponse201Type1:
    """ 
        Attributes:
            status (RotateSigningKeyResponse201Type1Status):
            key (None):
            challenge (RotateSigningKeyResponse201Type1Challenge):
     """

    status: RotateSigningKeyResponse201Type1Status
    key: None
    challenge: RotateSigningKeyResponse201Type1Challenge





    def to_dict(self) -> dict[str, Any]:
        from ..models.rotate_signing_key_response_201_type_1_challenge import RotateSigningKeyResponse201Type1Challenge # noqa: PLC0415
        status = self.status.value

        key = self.key

        challenge = self.challenge.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "key": key,
            "challenge": challenge,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rotate_signing_key_response_201_type_1_challenge import RotateSigningKeyResponse201Type1Challenge # noqa: PLC0415
        d = dict(src_dict)
        status = RotateSigningKeyResponse201Type1Status(d.pop("status"))




        key = d.pop("key")

        challenge = RotateSigningKeyResponse201Type1Challenge.from_dict(d.pop("challenge"))




        rotate_signing_key_response_201_type_1 = cls(
            status=status,
            key=key,
            challenge=challenge,
        )

        return rotate_signing_key_response_201_type_1

