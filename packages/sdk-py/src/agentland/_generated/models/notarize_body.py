from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="NotarizeBody")



@_attrs_define
class NotarizeBody:
    """ 
        Attributes:
            hash_ (str):
            label (str | Unset):
     """

    hash_: str
    label: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        hash_ = self.hash_

        label = self.label


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "hash": hash_,
        })
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hash_ = d.pop("hash")

        label = d.pop("label", UNSET)

        notarize_body = cls(
            hash_=hash_,
            label=label,
        )

        return notarize_body

