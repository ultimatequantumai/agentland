from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ListDatasetsResponse200ManifestWithheldItem")



@_attrs_define
class ListDatasetsResponse200ManifestWithheldItem:
    """ 
        Attributes:
            source (str):
            reason (str):
     """

    source: str
    reason: str





    def to_dict(self) -> dict[str, Any]:
        source = self.source

        reason = self.reason


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "source": source,
            "reason": reason,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        reason = d.pop("reason")

        list_datasets_response_200_manifest_withheld_item = cls(
            source=source,
            reason=reason,
        )

        return list_datasets_response_200_manifest_withheld_item

