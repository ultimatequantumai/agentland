from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.list_datasets_response_200_manifest_withheld_item import ListDatasetsResponse200ManifestWithheldItem





T = TypeVar("T", bound="ListDatasetsResponse200Manifest")



@_attrs_define
class ListDatasetsResponse200Manifest:
    """ 
        Attributes:
            version (str):
            included (list[str]):
            withheld (list[ListDatasetsResponse200ManifestWithheldItem]):
     """

    version: str
    included: list[str]
    withheld: list[ListDatasetsResponse200ManifestWithheldItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_datasets_response_200_manifest_withheld_item import ListDatasetsResponse200ManifestWithheldItem # noqa: PLC0415
        version = self.version

        included = self.included



        withheld = []
        for withheld_item_data in self.withheld:
            withheld_item = withheld_item_data.to_dict()
            withheld.append(withheld_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "version": version,
            "included": included,
            "withheld": withheld,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_datasets_response_200_manifest_withheld_item import ListDatasetsResponse200ManifestWithheldItem # noqa: PLC0415
        d = dict(src_dict)
        version = d.pop("version")

        included = cast(list[str], d.pop("included"))


        withheld = []
        _withheld = d.pop("withheld")
        for withheld_item_data in (_withheld):
            withheld_item = ListDatasetsResponse200ManifestWithheldItem.from_dict(withheld_item_data)



            withheld.append(withheld_item)


        list_datasets_response_200_manifest = cls(
            version=version,
            included=included,
            withheld=withheld,
        )

        return list_datasets_response_200_manifest

