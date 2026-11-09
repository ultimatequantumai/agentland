from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_agent_did_history_response_200_keys_item import GetAgentDidHistoryResponse200KeysItem
  from ..models.get_agent_did_history_response_200_recovery_notice_type_0 import GetAgentDidHistoryResponse200RecoveryNoticeType0
  from ..models.get_agent_did_history_response_200_rotations_item import GetAgentDidHistoryResponse200RotationsItem





T = TypeVar("T", bound="GetAgentDidHistoryResponse200")



@_attrs_define
class GetAgentDidHistoryResponse200:
    """ 
        Attributes:
            did (str):
            keys (list[GetAgentDidHistoryResponse200KeysItem]):
            rotations (list[GetAgentDidHistoryResponse200RotationsItem]):
            recovery_notice (GetAgentDidHistoryResponse200RecoveryNoticeType0 | None):
     """

    did: str
    keys: list[GetAgentDidHistoryResponse200KeysItem]
    rotations: list[GetAgentDidHistoryResponse200RotationsItem]
    recovery_notice: GetAgentDidHistoryResponse200RecoveryNoticeType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_did_history_response_200_keys_item import GetAgentDidHistoryResponse200KeysItem # noqa: PLC0415
        from ..models.get_agent_did_history_response_200_recovery_notice_type_0 import GetAgentDidHistoryResponse200RecoveryNoticeType0 # noqa: PLC0415
        from ..models.get_agent_did_history_response_200_rotations_item import GetAgentDidHistoryResponse200RotationsItem # noqa: PLC0415
        did = self.did

        keys = []
        for keys_item_data in self.keys:
            keys_item = keys_item_data.to_dict()
            keys.append(keys_item)



        rotations = []
        for rotations_item_data in self.rotations:
            rotations_item = rotations_item_data.to_dict()
            rotations.append(rotations_item)



        recovery_notice: dict[str, Any] | None
        if isinstance(self.recovery_notice, GetAgentDidHistoryResponse200RecoveryNoticeType0):
            recovery_notice = self.recovery_notice.to_dict()
        else:
            recovery_notice = self.recovery_notice


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "did": did,
            "keys": keys,
            "rotations": rotations,
            "recovery_notice": recovery_notice,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_did_history_response_200_keys_item import GetAgentDidHistoryResponse200KeysItem # noqa: PLC0415
        from ..models.get_agent_did_history_response_200_recovery_notice_type_0 import GetAgentDidHistoryResponse200RecoveryNoticeType0 # noqa: PLC0415
        from ..models.get_agent_did_history_response_200_rotations_item import GetAgentDidHistoryResponse200RotationsItem # noqa: PLC0415
        d = dict(src_dict)
        did = d.pop("did")

        keys = []
        _keys = d.pop("keys")
        for keys_item_data in (_keys):
            keys_item = GetAgentDidHistoryResponse200KeysItem.from_dict(keys_item_data)



            keys.append(keys_item)


        rotations = []
        _rotations = d.pop("rotations")
        for rotations_item_data in (_rotations):
            rotations_item = GetAgentDidHistoryResponse200RotationsItem.from_dict(rotations_item_data)



            rotations.append(rotations_item)


        def _parse_recovery_notice(data: object) -> GetAgentDidHistoryResponse200RecoveryNoticeType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                recovery_notice_type_0 = GetAgentDidHistoryResponse200RecoveryNoticeType0.from_dict(data)



                return recovery_notice_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAgentDidHistoryResponse200RecoveryNoticeType0 | None, data)

        recovery_notice = _parse_recovery_notice(d.pop("recovery_notice"))


        get_agent_did_history_response_200 = cls(
            did=did,
            keys=keys,
            rotations=rotations,
            recovery_notice=recovery_notice,
        )

        return get_agent_did_history_response_200

