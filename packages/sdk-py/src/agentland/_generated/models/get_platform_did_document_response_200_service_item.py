from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_platform_did_document_response_200_service_item_type import GetPlatformDidDocumentResponse200ServiceItemType






T = TypeVar("T", bound="GetPlatformDidDocumentResponse200ServiceItem")



@_attrs_define
class GetPlatformDidDocumentResponse200ServiceItem:
    """ 
        Attributes:
            id (str):
            type_ (GetPlatformDidDocumentResponse200ServiceItemType):
            service_endpoint (str):
     """

    id: str
    type_: GetPlatformDidDocumentResponse200ServiceItemType
    service_endpoint: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        service_endpoint = self.service_endpoint


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "type": type_,
            "serviceEndpoint": service_endpoint,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = GetPlatformDidDocumentResponse200ServiceItemType(d.pop("type"))




        service_endpoint = d.pop("serviceEndpoint")

        get_platform_did_document_response_200_service_item = cls(
            id=id,
            type_=type_,
            service_endpoint=service_endpoint,
        )

        return get_platform_did_document_response_200_service_item

