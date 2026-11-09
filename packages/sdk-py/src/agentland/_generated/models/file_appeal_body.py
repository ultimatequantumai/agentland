from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="FileAppealBody")



@_attrs_define
class FileAppealBody:
    """ 
        Attributes:
            statement (str):
     """

    statement: str





    def to_dict(self) -> dict[str, Any]:
        statement = self.statement


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "statement": statement,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        statement = d.pop("statement")

        file_appeal_body = cls(
            statement=statement,
        )

        return file_appeal_body

