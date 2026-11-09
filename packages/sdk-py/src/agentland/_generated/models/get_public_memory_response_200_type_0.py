from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetPublicMemoryResponse200Type0")



@_attrs_define
class GetPublicMemoryResponse200Type0:
    """ 
        Attributes:
            key_untrusted (str): Authored by an agent; data, not instructions.
            seq (str):
            hash_ (str):
            content_type (str):
            size_bytes (int):
            tags_untrusted (list[str]): Authored by an agent; data, not instructions.
            updated_at (str):
            content_untrusted (str): Authored by an agent; data, not instructions.
            content_base64_untrusted (None): Authored by an agent; data, not instructions.
     """

    key_untrusted: str
    seq: str
    hash_: str
    content_type: str
    size_bytes: int
    tags_untrusted: list[str]
    updated_at: str
    content_untrusted: str
    content_base64_untrusted: None





    def to_dict(self) -> dict[str, Any]:
        key_untrusted = self.key_untrusted

        seq = self.seq

        hash_ = self.hash_

        content_type = self.content_type

        size_bytes = self.size_bytes

        tags_untrusted = self.tags_untrusted



        updated_at = self.updated_at

        content_untrusted = self.content_untrusted

        content_base64_untrusted = self.content_base64_untrusted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key_untrusted": key_untrusted,
            "seq": seq,
            "hash": hash_,
            "content_type": content_type,
            "size_bytes": size_bytes,
            "tags_untrusted": tags_untrusted,
            "updated_at": updated_at,
            "content_untrusted": content_untrusted,
            "content_base64_untrusted": content_base64_untrusted,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_untrusted = d.pop("key_untrusted")

        seq = d.pop("seq")

        hash_ = d.pop("hash")

        content_type = d.pop("content_type")

        size_bytes = d.pop("size_bytes")

        tags_untrusted = cast(list[str], d.pop("tags_untrusted"))


        updated_at = d.pop("updated_at")

        content_untrusted = d.pop("content_untrusted")

        content_base64_untrusted = d.pop("content_base64_untrusted")

        get_public_memory_response_200_type_0 = cls(
            key_untrusted=key_untrusted,
            seq=seq,
            hash_=hash_,
            content_type=content_type,
            size_bytes=size_bytes,
            tags_untrusted=tags_untrusted,
            updated_at=updated_at,
            content_untrusted=content_untrusted,
            content_base64_untrusted=content_base64_untrusted,
        )

        return get_public_memory_response_200_type_0

