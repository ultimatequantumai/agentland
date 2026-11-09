from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_webhook_body_event_types_item import CreateWebhookBodyEventTypesItem
from typing import cast






T = TypeVar("T", bound="CreateWebhookBody")



@_attrs_define
class CreateWebhookBody:
    """ 
        Attributes:
            url (str):
            event_types (list[CreateWebhookBodyEventTypesItem]):
     """

    url: str
    event_types: list[CreateWebhookBodyEventTypesItem]





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        event_types = []
        for event_types_item_data in self.event_types:
            event_types_item = event_types_item_data.value
            event_types.append(event_types_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "url": url,
            "event_types": event_types,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        event_types = []
        _event_types = d.pop("event_types")
        for event_types_item_data in (_event_types):
            event_types_item = CreateWebhookBodyEventTypesItem(event_types_item_data)



            event_types.append(event_types_item)


        create_webhook_body = cls(
            url=url,
            event_types=event_types,
        )

        return create_webhook_body

