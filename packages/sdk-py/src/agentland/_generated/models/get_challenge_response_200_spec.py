from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetChallengeResponse200Spec")



@_attrs_define
class GetChallengeResponse200Spec:
    """ 
        Attributes:
            sha256 (str):
            bytes_ (int):
            url (str):
     """

    sha256: str
    bytes_: int
    url: str





    def to_dict(self) -> dict[str, Any]:
        sha256 = self.sha256

        bytes_ = self.bytes_

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "sha256": sha256,
            "bytes": bytes_,
            "url": url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sha256 = d.pop("sha256")

        bytes_ = d.pop("bytes")

        url = d.pop("url")

        get_challenge_response_200_spec = cls(
            sha256=sha256,
            bytes_=bytes_,
            url=url,
        )

        return get_challenge_response_200_spec

