from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="InitiateTransferBody")



@_attrs_define
class InitiateTransferBody:
    """ 
        Attributes:
            to_operator_email (str):
     """

    to_operator_email: str





    def to_dict(self) -> dict[str, Any]:
        to_operator_email = self.to_operator_email


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "to_operator_email": to_operator_email,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        to_operator_email = d.pop("to_operator_email")

        initiate_transfer_body = cls(
            to_operator_email=to_operator_email,
        )

        return initiate_transfer_body

