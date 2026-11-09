from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetChallengeResponse200BaselineType0")



@_attrs_define
class GetChallengeResponse200BaselineType0:
    """ 
        Attributes:
            heuristic (str):
            version (int):
            artifact_url (str):
            log_url (str):
     """

    heuristic: str
    version: int
    artifact_url: str
    log_url: str





    def to_dict(self) -> dict[str, Any]:
        heuristic = self.heuristic

        version = self.version

        artifact_url = self.artifact_url

        log_url = self.log_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "heuristic": heuristic,
            "version": version,
            "artifact_url": artifact_url,
            "log_url": log_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        heuristic = d.pop("heuristic")

        version = d.pop("version")

        artifact_url = d.pop("artifact_url")

        log_url = d.pop("log_url")

        get_challenge_response_200_baseline_type_0 = cls(
            heuristic=heuristic,
            version=version,
            artifact_url=artifact_url,
            log_url=log_url,
        )

        return get_challenge_response_200_baseline_type_0

