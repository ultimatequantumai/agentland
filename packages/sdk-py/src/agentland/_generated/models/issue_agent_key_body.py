from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.issue_agent_key_body_scopes_item import IssueAgentKeyBodyScopesItem
from typing import cast






T = TypeVar("T", bound="IssueAgentKeyBody")



@_attrs_define
class IssueAgentKeyBody:
    """ 
        Attributes:
            scopes (list[IssueAgentKeyBodyScopesItem]):
     """

    scopes: list[IssueAgentKeyBodyScopesItem]





    def to_dict(self) -> dict[str, Any]:
        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "scopes": scopes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in (_scopes):
            scopes_item = IssueAgentKeyBodyScopesItem(scopes_item_data)



            scopes.append(scopes_item)


        issue_agent_key_body = cls(
            scopes=scopes,
        )

        return issue_agent_key_body

