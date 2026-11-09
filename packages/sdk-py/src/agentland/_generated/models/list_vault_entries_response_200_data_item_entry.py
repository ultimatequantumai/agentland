from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_vault_entries_response_200_data_item_entry_op import ListVaultEntriesResponse200DataItemEntryOp
from typing import cast






T = TypeVar("T", bound="ListVaultEntriesResponse200DataItemEntry")



@_attrs_define
class ListVaultEntriesResponse200DataItemEntry:
    """ 
        Attributes:
            seq (str):
            key (str):
            op (ListVaultEntriesResponse200DataItemEntryOp):
            content_hash (str):
            content_ref (None | str):
            content_type (str):
            tags (list[str]):
            prev_hash (str):
            ts_server (str):
            sig_agent (str):
     """

    seq: str
    key: str
    op: ListVaultEntriesResponse200DataItemEntryOp
    content_hash: str
    content_ref: None | str
    content_type: str
    tags: list[str]
    prev_hash: str
    ts_server: str
    sig_agent: str





    def to_dict(self) -> dict[str, Any]:
        seq = self.seq

        key = self.key

        op = self.op.value

        content_hash = self.content_hash

        content_ref: None | str
        content_ref = self.content_ref

        content_type = self.content_type

        tags = self.tags



        prev_hash = self.prev_hash

        ts_server = self.ts_server

        sig_agent = self.sig_agent


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "seq": seq,
            "key": key,
            "op": op,
            "content_hash": content_hash,
            "content_ref": content_ref,
            "content_type": content_type,
            "tags": tags,
            "prev_hash": prev_hash,
            "ts_server": ts_server,
            "sig_agent": sig_agent,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seq = d.pop("seq")

        key = d.pop("key")

        op = ListVaultEntriesResponse200DataItemEntryOp(d.pop("op"))




        content_hash = d.pop("content_hash")

        def _parse_content_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content_ref = _parse_content_ref(d.pop("content_ref"))


        content_type = d.pop("content_type")

        tags = cast(list[str], d.pop("tags"))


        prev_hash = d.pop("prev_hash")

        ts_server = d.pop("ts_server")

        sig_agent = d.pop("sig_agent")

        list_vault_entries_response_200_data_item_entry = cls(
            seq=seq,
            key=key,
            op=op,
            content_hash=content_hash,
            content_ref=content_ref,
            content_type=content_type,
            tags=tags,
            prev_hash=prev_hash,
            ts_server=ts_server,
            sig_agent=sig_agent,
        )

        return list_vault_entries_response_200_data_item_entry

