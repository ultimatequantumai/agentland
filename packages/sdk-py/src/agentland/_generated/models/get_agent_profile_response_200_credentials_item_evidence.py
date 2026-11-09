from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetAgentProfileResponse200CredentialsItemEvidence")



@_attrs_define
class GetAgentProfileResponse200CredentialsItemEvidence:
    """ 
        Attributes:
            season (str):
            n (int):
            shrunk_edge (float):
            audit_root (str):
     """

    season: str
    n: int
    shrunk_edge: float
    audit_root: str





    def to_dict(self) -> dict[str, Any]:
        season = self.season

        n = self.n

        shrunk_edge = self.shrunk_edge

        audit_root = self.audit_root


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "season": season,
            "n": n,
            "shrunk_edge": shrunk_edge,
            "audit_root": audit_root,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        season = d.pop("season")

        n = d.pop("n")

        shrunk_edge = d.pop("shrunk_edge")

        audit_root = d.pop("audit_root")

        get_agent_profile_response_200_credentials_item_evidence = cls(
            season=season,
            n=n,
            shrunk_edge=shrunk_edge,
            audit_root=audit_root,
        )

        return get_agent_profile_response_200_credentials_item_evidence

