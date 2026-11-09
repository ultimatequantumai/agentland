from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="FileReportResponse201")



@_attrs_define
class FileReportResponse201:
    """ 
        Attributes:
            id (UUID):
            received_at (str):
     """

    id: UUID
    received_at: str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        received_at = self.received_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "received_at": received_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        received_at = d.pop("received_at")

        file_report_response_201 = cls(
            id=id,
            received_at=received_at,
        )

        return file_report_response_201

