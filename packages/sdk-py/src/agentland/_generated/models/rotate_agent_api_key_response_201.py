from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.rotate_agent_api_key_response_201_api_key import RotateAgentApiKeyResponse201ApiKey





T = TypeVar("T", bound="RotateAgentApiKeyResponse201")



@_attrs_define
class RotateAgentApiKeyResponse201:
    """ 
        Attributes:
            api_key (RotateAgentApiKeyResponse201ApiKey):
            previous_key_expires_at (str):
     """

    api_key: RotateAgentApiKeyResponse201ApiKey
    previous_key_expires_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.rotate_agent_api_key_response_201_api_key import RotateAgentApiKeyResponse201ApiKey # noqa: PLC0415
        api_key = self.api_key.to_dict()

        previous_key_expires_at = self.previous_key_expires_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "api_key": api_key,
            "previous_key_expires_at": previous_key_expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rotate_agent_api_key_response_201_api_key import RotateAgentApiKeyResponse201ApiKey # noqa: PLC0415
        d = dict(src_dict)
        api_key = RotateAgentApiKeyResponse201ApiKey.from_dict(d.pop("api_key"))




        previous_key_expires_at = d.pop("previous_key_expires_at")

        rotate_agent_api_key_response_201 = cls(
            api_key=api_key,
            previous_key_expires_at=previous_key_expires_at,
        )

        return rotate_agent_api_key_response_201

