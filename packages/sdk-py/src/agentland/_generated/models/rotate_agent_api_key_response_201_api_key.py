from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rotate_agent_api_key_response_201_api_key_prefix import RotateAgentApiKeyResponse201ApiKeyPrefix
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="RotateAgentApiKeyResponse201ApiKey")



@_attrs_define
class RotateAgentApiKeyResponse201ApiKey:
    """ 
        Attributes:
            id (UUID):
            prefix (RotateAgentApiKeyResponse201ApiKeyPrefix):
            last4 (str):
            key (str):
            expires_at (None | str):
     """

    id: UUID
    prefix: RotateAgentApiKeyResponse201ApiKeyPrefix
    last4: str
    key: str
    expires_at: None | str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        prefix = self.prefix.value

        last4 = self.last4

        key = self.key

        expires_at: None | str
        expires_at = self.expires_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "prefix": prefix,
            "last4": last4,
            "key": key,
            "expires_at": expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        prefix = RotateAgentApiKeyResponse201ApiKeyPrefix(d.pop("prefix"))




        last4 = d.pop("last4")

        key = d.pop("key")

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))


        rotate_agent_api_key_response_201_api_key = cls(
            id=id,
            prefix=prefix,
            last4=last4,
            key=key,
            expires_at=expires_at,
        )

        return rotate_agent_api_key_response_201_api_key

