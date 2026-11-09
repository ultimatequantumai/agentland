from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_webhook_response_201_event_types_item import CreateWebhookResponse201EventTypesItem
from ..models.create_webhook_response_201_status import CreateWebhookResponse201Status
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="CreateWebhookResponse201")



@_attrs_define
class CreateWebhookResponse201:
    """ 
        Attributes:
            id (UUID):
            url (str):
            event_types (list[CreateWebhookResponse201EventTypesItem]):
            status (CreateWebhookResponse201Status):
            failures (int):
            created_at (str):
            secret (str):
     """

    id: UUID
    url: str
    event_types: list[CreateWebhookResponse201EventTypesItem]
    status: CreateWebhookResponse201Status
    failures: int
    created_at: str
    secret: str





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

        secret = self.secret


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "url": url,
            "event_types": event_types,
            "status": status,
            "failures": failures,
            "created_at": created_at,
            "secret": secret,
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
            event_types_item = CreateWebhookResponse201EventTypesItem(event_types_item_data)



            event_types.append(event_types_item)


        status = CreateWebhookResponse201Status(d.pop("status"))




        failures = d.pop("failures")

        created_at = d.pop("created_at")

        secret = d.pop("secret")

        create_webhook_response_201 = cls(
            id=id,
            url=url,
            event_types=event_types,
            status=status,
            failures=failures,
            created_at=created_at,
            secret=secret,
        )

        return create_webhook_response_201

