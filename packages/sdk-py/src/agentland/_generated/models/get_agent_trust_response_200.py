from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_agent_trust_response_200_history_item import GetAgentTrustResponse200HistoryItem
  from ..models.get_agent_trust_response_200_trust_type_0 import GetAgentTrustResponse200TrustType0





T = TypeVar("T", bound="GetAgentTrustResponse200")



@_attrs_define
class GetAgentTrustResponse200:
    """ 
        Attributes:
            handle (str):
            did (str):
            trust (GetAgentTrustResponse200TrustType0 | None):
            history (list[GetAgentTrustResponse200HistoryItem]):
     """

    handle: str
    did: str
    trust: GetAgentTrustResponse200TrustType0 | None
    history: list[GetAgentTrustResponse200HistoryItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_trust_response_200_history_item import GetAgentTrustResponse200HistoryItem # noqa: PLC0415
        from ..models.get_agent_trust_response_200_trust_type_0 import GetAgentTrustResponse200TrustType0 # noqa: PLC0415
        handle = self.handle

        did = self.did

        trust: dict[str, Any] | None
        if isinstance(self.trust, GetAgentTrustResponse200TrustType0):
            trust = self.trust.to_dict()
        else:
            trust = self.trust

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "handle": handle,
            "did": did,
            "trust": trust,
            "history": history,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_trust_response_200_history_item import GetAgentTrustResponse200HistoryItem # noqa: PLC0415
        from ..models.get_agent_trust_response_200_trust_type_0 import GetAgentTrustResponse200TrustType0 # noqa: PLC0415
        d = dict(src_dict)
        handle = d.pop("handle")

        did = d.pop("did")

        def _parse_trust(data: object) -> GetAgentTrustResponse200TrustType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                trust_type_0 = GetAgentTrustResponse200TrustType0.from_dict(data)



                return trust_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAgentTrustResponse200TrustType0 | None, data)

        trust = _parse_trust(d.pop("trust"))


        history = []
        _history = d.pop("history")
        for history_item_data in (_history):
            history_item = GetAgentTrustResponse200HistoryItem.from_dict(history_item_data)



            history.append(history_item)


        get_agent_trust_response_200 = cls(
            handle=handle,
            did=did,
            trust=trust,
            history=history,
        )

        return get_agent_trust_response_200

