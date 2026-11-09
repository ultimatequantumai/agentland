from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetOperatorAgentResponse200VaultLimits")



@_attrs_define
class GetOperatorAgentResponse200VaultLimits:
    """ 
        Attributes:
            vault_entries (None | str):
            vault_bytes (None | str):
     """

    vault_entries: None | str
    vault_bytes: None | str





    def to_dict(self) -> dict[str, Any]:
        vault_entries: None | str
        vault_entries = self.vault_entries

        vault_bytes: None | str
        vault_bytes = self.vault_bytes


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "vault_entries": vault_entries,
            "vault_bytes": vault_bytes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_vault_entries(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        vault_entries = _parse_vault_entries(d.pop("vault_entries"))


        def _parse_vault_bytes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        vault_bytes = _parse_vault_bytes(d.pop("vault_bytes"))


        get_operator_agent_response_200_vault_limits = cls(
            vault_entries=vault_entries,
            vault_bytes=vault_bytes,
        )

        return get_operator_agent_response_200_vault_limits

