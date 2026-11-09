from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.file_report_body_target_type_0_kind import FileReportBodyTargetType0Kind






T = TypeVar("T", bound="FileReportBodyTargetType0")



@_attrs_define
class FileReportBodyTargetType0:
    """ 
        Attributes:
            kind (FileReportBodyTargetType0Kind):
            id (str):
     """

    kind: FileReportBodyTargetType0Kind
    id: str





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
            "id": id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = FileReportBodyTargetType0Kind(d.pop("kind"))




        id = d.pop("id")

        file_report_body_target_type_0 = cls(
            kind=kind,
            id=id,
        )

        return file_report_body_target_type_0

