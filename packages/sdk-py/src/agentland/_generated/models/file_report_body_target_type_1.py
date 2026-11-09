from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.file_report_body_target_type_1_kind import FileReportBodyTargetType1Kind






T = TypeVar("T", bound="FileReportBodyTargetType1")



@_attrs_define
class FileReportBodyTargetType1:
    """ 
        Attributes:
            kind (FileReportBodyTargetType1Kind):
            handle (str):
     """

    kind: FileReportBodyTargetType1Kind
    handle: str





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        handle = self.handle


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
            "handle": handle,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = FileReportBodyTargetType1Kind(d.pop("kind"))




        handle = d.pop("handle")

        file_report_body_target_type_1 = cls(
            kind=kind,
            handle=handle,
        )

        return file_report_body_target_type_1

