from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_operator_agent_response_200_vault_limits import GetOperatorAgentResponse200VaultLimits





T = TypeVar("T", bound="GetOperatorAgentResponse200Vault")



@_attrs_define
class GetOperatorAgentResponse200Vault:
    """ 
        Attributes:
            seq (str):
            head_hash (str):
            retained_puts (str):
            retained_bytes (str):
            limits (GetOperatorAgentResponse200VaultLimits):
     """

    seq: str
    head_hash: str
    retained_puts: str
    retained_bytes: str
    limits: GetOperatorAgentResponse200VaultLimits





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_operator_agent_response_200_vault_limits import GetOperatorAgentResponse200VaultLimits # noqa: PLC0415
        seq = self.seq

        head_hash = self.head_hash

        retained_puts = self.retained_puts

        retained_bytes = self.retained_bytes

        limits = self.limits.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "seq": seq,
            "head_hash": head_hash,
            "retained_puts": retained_puts,
            "retained_bytes": retained_bytes,
            "limits": limits,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_operator_agent_response_200_vault_limits import GetOperatorAgentResponse200VaultLimits # noqa: PLC0415
        d = dict(src_dict)
        seq = d.pop("seq")

        head_hash = d.pop("head_hash")

        retained_puts = d.pop("retained_puts")

        retained_bytes = d.pop("retained_bytes")

        limits = GetOperatorAgentResponse200VaultLimits.from_dict(d.pop("limits"))




        get_operator_agent_response_200_vault = cls(
            seq=seq,
            head_hash=head_hash,
            retained_puts=retained_puts,
            retained_bytes=retained_bytes,
            limits=limits,
        )

        return get_operator_agent_response_200_vault

