from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.file_report_body_category import FileReportBodyCategory
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.file_report_body_target_type_0 import FileReportBodyTargetType0
  from ..models.file_report_body_target_type_1 import FileReportBodyTargetType1





T = TypeVar("T", bound="FileReportBody")



@_attrs_define
class FileReportBody:
    """ 
        Attributes:
            target (FileReportBodyTargetType0 | FileReportBodyTargetType1):
            category (FileReportBodyCategory):
            details (str | Unset):
     """

    target: FileReportBodyTargetType0 | FileReportBodyTargetType1
    category: FileReportBodyCategory
    details: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.file_report_body_target_type_0 import FileReportBodyTargetType0 # noqa: PLC0415
        from ..models.file_report_body_target_type_1 import FileReportBodyTargetType1 # noqa: PLC0415
        target: dict[str, Any]
        if isinstance(self.target, FileReportBodyTargetType0):
            target = self.target.to_dict()
        else:
            target = self.target.to_dict()


        category = self.category.value

        details = self.details


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "target": target,
            "category": category,
        })
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_report_body_target_type_0 import FileReportBodyTargetType0 # noqa: PLC0415
        from ..models.file_report_body_target_type_1 import FileReportBodyTargetType1 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_target(data: object) -> FileReportBodyTargetType0 | FileReportBodyTargetType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_type_0 = FileReportBodyTargetType0.from_dict(data)



                return target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            target_type_1 = FileReportBodyTargetType1.from_dict(data)



            return target_type_1

        target = _parse_target(d.pop("target"))


        category = FileReportBodyCategory(d.pop("category"))




        details = d.pop("details", UNSET)

        file_report_body = cls(
            target=target,
            category=category,
            details=details,
        )

        return file_report_body

