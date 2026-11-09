from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.list_datasets_response_200_releases_item_tables_item import ListDatasetsResponse200ReleasesItemTablesItem





T = TypeVar("T", bound="ListDatasetsResponse200ReleasesItem")



@_attrs_define
class ListDatasetsResponse200ReleasesItem:
    """ 
        Attributes:
            month (str):
            manifest_version (str):
            tables (list[ListDatasetsResponse200ReleasesItemTablesItem]):
     """

    month: str
    manifest_version: str
    tables: list[ListDatasetsResponse200ReleasesItemTablesItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_datasets_response_200_releases_item_tables_item import ListDatasetsResponse200ReleasesItemTablesItem # noqa: PLC0415
        month = self.month

        manifest_version = self.manifest_version

        tables = []
        for tables_item_data in self.tables:
            tables_item = tables_item_data.to_dict()
            tables.append(tables_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "month": month,
            "manifest_version": manifest_version,
            "tables": tables,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_datasets_response_200_releases_item_tables_item import ListDatasetsResponse200ReleasesItemTablesItem # noqa: PLC0415
        d = dict(src_dict)
        month = d.pop("month")

        manifest_version = d.pop("manifest_version")

        tables = []
        _tables = d.pop("tables")
        for tables_item_data in (_tables):
            tables_item = ListDatasetsResponse200ReleasesItemTablesItem.from_dict(tables_item_data)



            tables.append(tables_item)


        list_datasets_response_200_releases_item = cls(
            month=month,
            manifest_version=manifest_version,
            tables=tables,
        )

        return list_datasets_response_200_releases_item

