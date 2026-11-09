from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_datasets_response_200_license import ListDatasetsResponse200License
from typing import cast

if TYPE_CHECKING:
  from ..models.list_datasets_response_200_manifest import ListDatasetsResponse200Manifest
  from ..models.list_datasets_response_200_releases_item import ListDatasetsResponse200ReleasesItem





T = TypeVar("T", bound="ListDatasetsResponse200")



@_attrs_define
class ListDatasetsResponse200:
    """ 
        Attributes:
            license_ (ListDatasetsResponse200License):
            manifest (ListDatasetsResponse200Manifest):
            releases (list[ListDatasetsResponse200ReleasesItem]):
     """

    license_: ListDatasetsResponse200License
    manifest: ListDatasetsResponse200Manifest
    releases: list[ListDatasetsResponse200ReleasesItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_datasets_response_200_manifest import ListDatasetsResponse200Manifest # noqa: PLC0415
        from ..models.list_datasets_response_200_releases_item import ListDatasetsResponse200ReleasesItem # noqa: PLC0415
        license_ = self.license_.value

        manifest = self.manifest.to_dict()

        releases = []
        for releases_item_data in self.releases:
            releases_item = releases_item_data.to_dict()
            releases.append(releases_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "license": license_,
            "manifest": manifest,
            "releases": releases,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_datasets_response_200_manifest import ListDatasetsResponse200Manifest # noqa: PLC0415
        from ..models.list_datasets_response_200_releases_item import ListDatasetsResponse200ReleasesItem # noqa: PLC0415
        d = dict(src_dict)
        license_ = ListDatasetsResponse200License(d.pop("license"))




        manifest = ListDatasetsResponse200Manifest.from_dict(d.pop("manifest"))




        releases = []
        _releases = d.pop("releases")
        for releases_item_data in (_releases):
            releases_item = ListDatasetsResponse200ReleasesItem.from_dict(releases_item_data)



            releases.append(releases_item)


        list_datasets_response_200 = cls(
            license_=license_,
            manifest=manifest,
            releases=releases,
        )

        return list_datasets_response_200

