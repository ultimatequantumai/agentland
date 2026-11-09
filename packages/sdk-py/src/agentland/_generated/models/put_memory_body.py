from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutMemoryBody")



@_attrs_define
class PutMemoryBody:
    """ 
        Attributes:
            content (str | Unset):
            content_base64 (str | Unset):
            content_type (str | Unset):  Default: 'text/plain; charset=utf-8'.
            tags (list[str] | Unset):
            if_seq (str | Unset):
            signature (str | Unset):
     """

    content: str | Unset = UNSET
    content_base64: str | Unset = UNSET
    content_type: str | Unset = 'text/plain; charset=utf-8'
    tags: list[str] | Unset = UNSET
    if_seq: str | Unset = UNSET
    signature: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content = self.content

        content_base64 = self.content_base64

        content_type = self.content_type

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags



        if_seq = self.if_seq

        signature = self.signature


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content is not UNSET:
            field_dict["content"] = content
        if content_base64 is not UNSET:
            field_dict["content_base64"] = content_base64
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if tags is not UNSET:
            field_dict["tags"] = tags
        if if_seq is not UNSET:
            field_dict["if_seq"] = if_seq
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content", UNSET)

        content_base64 = d.pop("content_base64", UNSET)

        content_type = d.pop("content_type", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))


        if_seq = d.pop("if_seq", UNSET)

        signature = d.pop("signature", UNSET)

        put_memory_body = cls(
            content=content,
            content_base64=content_base64,
            content_type=content_type,
            tags=tags,
            if_seq=if_seq,
            signature=signature,
        )

        return put_memory_body

