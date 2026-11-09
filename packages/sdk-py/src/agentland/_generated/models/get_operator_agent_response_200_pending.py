from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_operator_agent_response_200_pending_key_challenges_item import GetOperatorAgentResponse200PendingKeyChallengesItem
  from ..models.get_operator_agent_response_200_pending_recovery_type_0 import GetOperatorAgentResponse200PendingRecoveryType0
  from ..models.get_operator_agent_response_200_pending_transfer_type_0 import GetOperatorAgentResponse200PendingTransferType0





T = TypeVar("T", bound="GetOperatorAgentResponse200Pending")



@_attrs_define
class GetOperatorAgentResponse200Pending:
    """ 
        Attributes:
            key_challenges (list[GetOperatorAgentResponse200PendingKeyChallengesItem]):
            recovery (GetOperatorAgentResponse200PendingRecoveryType0 | None):
            transfer (GetOperatorAgentResponse200PendingTransferType0 | None):
     """

    key_challenges: list[GetOperatorAgentResponse200PendingKeyChallengesItem]
    recovery: GetOperatorAgentResponse200PendingRecoveryType0 | None
    transfer: GetOperatorAgentResponse200PendingTransferType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_operator_agent_response_200_pending_key_challenges_item import GetOperatorAgentResponse200PendingKeyChallengesItem # noqa: PLC0415
        from ..models.get_operator_agent_response_200_pending_recovery_type_0 import GetOperatorAgentResponse200PendingRecoveryType0 # noqa: PLC0415
        from ..models.get_operator_agent_response_200_pending_transfer_type_0 import GetOperatorAgentResponse200PendingTransferType0 # noqa: PLC0415
        key_challenges = []
        for key_challenges_item_data in self.key_challenges:
            key_challenges_item = key_challenges_item_data.to_dict()
            key_challenges.append(key_challenges_item)



        recovery: dict[str, Any] | None
        if isinstance(self.recovery, GetOperatorAgentResponse200PendingRecoveryType0):
            recovery = self.recovery.to_dict()
        else:
            recovery = self.recovery

        transfer: dict[str, Any] | None
        if isinstance(self.transfer, GetOperatorAgentResponse200PendingTransferType0):
            transfer = self.transfer.to_dict()
        else:
            transfer = self.transfer


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key_challenges": key_challenges,
            "recovery": recovery,
            "transfer": transfer,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_operator_agent_response_200_pending_key_challenges_item import GetOperatorAgentResponse200PendingKeyChallengesItem # noqa: PLC0415
        from ..models.get_operator_agent_response_200_pending_recovery_type_0 import GetOperatorAgentResponse200PendingRecoveryType0 # noqa: PLC0415
        from ..models.get_operator_agent_response_200_pending_transfer_type_0 import GetOperatorAgentResponse200PendingTransferType0 # noqa: PLC0415
        d = dict(src_dict)
        key_challenges = []
        _key_challenges = d.pop("key_challenges")
        for key_challenges_item_data in (_key_challenges):
            key_challenges_item = GetOperatorAgentResponse200PendingKeyChallengesItem.from_dict(key_challenges_item_data)



            key_challenges.append(key_challenges_item)


        def _parse_recovery(data: object) -> GetOperatorAgentResponse200PendingRecoveryType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                recovery_type_0 = GetOperatorAgentResponse200PendingRecoveryType0.from_dict(data)



                return recovery_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetOperatorAgentResponse200PendingRecoveryType0 | None, data)

        recovery = _parse_recovery(d.pop("recovery"))


        def _parse_transfer(data: object) -> GetOperatorAgentResponse200PendingTransferType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transfer_type_0 = GetOperatorAgentResponse200PendingTransferType0.from_dict(data)



                return transfer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetOperatorAgentResponse200PendingTransferType0 | None, data)

        transfer = _parse_transfer(d.pop("transfer"))


        get_operator_agent_response_200_pending = cls(
            key_challenges=key_challenges,
            recovery=recovery,
            transfer=transfer,
        )

        return get_operator_agent_response_200_pending

