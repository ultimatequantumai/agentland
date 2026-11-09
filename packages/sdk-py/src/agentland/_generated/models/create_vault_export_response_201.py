from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_vault_export_response_201_status import CreateVaultExportResponse201Status
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="CreateVaultExportResponse201")



@_attrs_define
class CreateVaultExportResponse201:
    """ 
        Attributes:
            id (UUID):
            status (CreateVaultExportResponse201Status):
            created_at (str):
            completed_at (None | str):
            expires_at (str):
            manifest_sha256 (None | str):
            size_bytes (None | str):
            download_url (None | str):
            download_expires_at (None | str):
     """

    id: UUID
    status: CreateVaultExportResponse201Status
    created_at: str
    completed_at: None | str
    expires_at: str
    manifest_sha256: None | str
    size_bytes: None | str
    download_url: None | str
    download_expires_at: None | str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        status = self.status.value

        created_at = self.created_at

        completed_at: None | str
        completed_at = self.completed_at

        expires_at = self.expires_at

        manifest_sha256: None | str
        manifest_sha256 = self.manifest_sha256

        size_bytes: None | str
        size_bytes = self.size_bytes

        download_url: None | str
        download_url = self.download_url

        download_expires_at: None | str
        download_expires_at = self.download_expires_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "status": status,
            "created_at": created_at,
            "completed_at": completed_at,
            "expires_at": expires_at,
            "manifest_sha256": manifest_sha256,
            "size_bytes": size_bytes,
            "download_url": download_url,
            "download_expires_at": download_expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        status = CreateVaultExportResponse201Status(d.pop("status"))




        created_at = d.pop("created_at")

        def _parse_completed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_at = _parse_completed_at(d.pop("completed_at"))


        expires_at = d.pop("expires_at")

        def _parse_manifest_sha256(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        manifest_sha256 = _parse_manifest_sha256(d.pop("manifest_sha256"))


        def _parse_size_bytes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        size_bytes = _parse_size_bytes(d.pop("size_bytes"))


        def _parse_download_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        download_url = _parse_download_url(d.pop("download_url"))


        def _parse_download_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        download_expires_at = _parse_download_expires_at(d.pop("download_expires_at"))


        create_vault_export_response_201 = cls(
            id=id,
            status=status,
            created_at=created_at,
            completed_at=completed_at,
            expires_at=expires_at,
            manifest_sha256=manifest_sha256,
            size_bytes=size_bytes,
            download_url=download_url,
            download_expires_at=download_expires_at,
        )

        return create_vault_export_response_201

