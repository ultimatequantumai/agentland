from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.poll_events_response_200_data_item_payload import PollEventsResponse200DataItemPayload





T = TypeVar("T", bound="PollEventsResponse200DataItem")



@_attrs_define
class PollEventsResponse200DataItem:
    """ 
        Attributes:
            id (str):
            cursor (str):
            type_ (str):
            agent_id (None | UUID):
            payload (PollEventsResponse200DataItemPayload):
            created_at (str):
     """

    id: str
    cursor: str
    type_: str
    agent_id: None | UUID
    payload: PollEventsResponse200DataItemPayload
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.poll_events_response_200_data_item_payload import PollEventsResponse200DataItemPayload # noqa: PLC0415
        id = self.id

        cursor = self.cursor

        type_ = self.type_

        agent_id: None | str
        if isinstance(self.agent_id, UUID):
            agent_id = str(self.agent_id)
        else:
            agent_id = self.agent_id

        payload = self.payload.to_dict()

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "cursor": cursor,
            "type": type_,
            "agent_id": agent_id,
            "payload": payload,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_events_response_200_data_item_payload import PollEventsResponse200DataItemPayload # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        cursor = d.pop("cursor")

        type_ = d.pop("type")

        def _parse_agent_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_id_type_0 = UUID(data)



                return agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        agent_id = _parse_agent_id(d.pop("agent_id"))


        payload = PollEventsResponse200DataItemPayload.from_dict(d.pop("payload"))




        created_at = d.pop("created_at")

        poll_events_response_200_data_item = cls(
            id=id,
            cursor=cursor,
            type_=type_,
            agent_id=agent_id,
            payload=payload,
            created_at=created_at,
        )

        return poll_events_response_200_data_item

