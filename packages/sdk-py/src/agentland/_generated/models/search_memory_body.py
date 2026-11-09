from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchMemoryBody")



@_attrs_define
class SearchMemoryBody:
    """ 
        Attributes:
            q (str):
            limit (int | Unset):  Default: 50.
            cursor (str | Unset):
            tags (list[str] | Unset):
     """

    q: str
    limit: int | Unset = 50
    cursor: str | Unset = UNSET
    tags: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        q = self.q

        limit = self.limit

        cursor = self.cursor

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "q": q,
        })
        if limit is not UNSET:
            field_dict["limit"] = limit
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        q = d.pop("q")

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))


        search_memory_body = cls(
            q=q,
            limit=limit,
            cursor=cursor,
            tags=tags,
        )

        return search_memory_body

