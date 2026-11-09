from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_datasets_response_200_releases_item_tables_item_table import ListDatasetsResponse200ReleasesItemTablesItemTable






T = TypeVar("T", bound="ListDatasetsResponse200ReleasesItemTablesItem")



@_attrs_define
class ListDatasetsResponse200ReleasesItemTablesItem:
    """ 
        Attributes:
            table (ListDatasetsResponse200ReleasesItemTablesItemTable):
            rows (int):
            size_bytes (int):
            sha256 (str):
     """

    table: ListDatasetsResponse200ReleasesItemTablesItemTable
    rows: int
    size_bytes: int
    sha256: str





    def to_dict(self) -> dict[str, Any]:
        table = self.table.value

        rows = self.rows

        size_bytes = self.size_bytes

        sha256 = self.sha256


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "table": table,
            "rows": rows,
            "size_bytes": size_bytes,
            "sha256": sha256,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        table = ListDatasetsResponse200ReleasesItemTablesItemTable(d.pop("table"))




        rows = d.pop("rows")

        size_bytes = d.pop("size_bytes")

        sha256 = d.pop("sha256")

        list_datasets_response_200_releases_item_tables_item = cls(
            table=table,
            rows=rows,
            size_bytes=size_bytes,
            sha256=sha256,
        )

        return list_datasets_response_200_releases_item_tables_item

