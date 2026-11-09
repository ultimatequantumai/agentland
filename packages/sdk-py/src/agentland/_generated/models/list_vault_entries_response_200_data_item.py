from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.list_vault_entries_response_200_data_item_entry import ListVaultEntriesResponse200DataItemEntry





T = TypeVar("T", bound="ListVaultEntriesResponse200DataItem")



@_attrs_define
class ListVaultEntriesResponse200DataItem:
    """ 
        Attributes:
            entry (ListVaultEntriesResponse200DataItemEntry):
            hash_ (str):
            signing_key_id (UUID):
            purged (bool):
     """

    entry: ListVaultEntriesResponse200DataItemEntry
    hash_: str
    signing_key_id: UUID
    purged: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_vault_entries_response_200_data_item_entry import ListVaultEntriesResponse200DataItemEntry # noqa: PLC0415
        entry = self.entry.to_dict()

        hash_ = self.hash_

        signing_key_id = str(self.signing_key_id)

        purged = self.purged


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "entry": entry,
            "hash": hash_,
            "signing_key_id": signing_key_id,
            "purged": purged,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_vault_entries_response_200_data_item_entry import ListVaultEntriesResponse200DataItemEntry # noqa: PLC0415
        d = dict(src_dict)
        entry = ListVaultEntriesResponse200DataItemEntry.from_dict(d.pop("entry"))




        hash_ = d.pop("hash")

        signing_key_id = UUID(d.pop("signing_key_id"))




        purged = d.pop("purged")

        list_vault_entries_response_200_data_item = cls(
            entry=entry,
            hash_=hash_,
            signing_key_id=signing_key_id,
            purged=purged,
        )

        return list_vault_entries_response_200_data_item

