from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_webhooks_response_200_data_item_event_types_item import ListWebhooksResponse200DataItemEventTypesItem
from ..models.list_webhooks_response_200_data_item_status import ListWebhooksResponse200DataItemStatus
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ListWebhooksResponse200DataItem")



@_attrs_define
class ListWebhooksResponse200DataItem:
    """ 
        Attributes:
            id (UUID):
            url (str):
            event_types (list[ListWebhooksResponse200DataItemEventTypesItem]):
            status (ListWebhooksResponse200DataItemStatus):
            failures (int):
            created_at (str):
     """

    id: UUID
    url: str
    event_types: list[ListWebhooksResponse200DataItemEventTypesItem]
    status: ListWebhooksResponse200DataItemStatus
    failures: int
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        url = self.url

        event_types = []
        for event_types_item_data in self.event_types:
            event_types_item = event_types_item_data.value
            event_types.append(event_types_item)



        status = self.status.value

        failures = self.failures

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "url": url,
            "event_types": event_types,
            "status": status,
            "failures": failures,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        url = d.pop("url")

        event_types = []
        _event_types = d.pop("event_types")
        for event_types_item_data in (_event_types):
            event_types_item = ListWebhooksResponse200DataItemEventTypesItem(event_types_item_data)



            event_types.append(event_types_item)


        status = ListWebhooksResponse200DataItemStatus(d.pop("status"))




        failures = d.pop("failures")

        created_at = d.pop("created_at")

        list_webhooks_response_200_data_item = cls(
            id=id,
            url=url,
            event_types=event_types,
            status=status,
            failures=failures,
            created_at=created_at,
        )

        return list_webhooks_response_200_data_item

