from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_platform_did_document_response_200_context_item_type_1 import GetPlatformDidDocumentResponse200ContextItemType1
  from ..models.get_platform_did_document_response_200_service_item import GetPlatformDidDocumentResponse200ServiceItem
  from ..models.get_platform_did_document_response_200_verification_method_item import GetPlatformDidDocumentResponse200VerificationMethodItem





T = TypeVar("T", bound="GetPlatformDidDocumentResponse200")



@_attrs_define
class GetPlatformDidDocumentResponse200:
    """ 
        Attributes:
            context (list[GetPlatformDidDocumentResponse200ContextItemType1 | str]):
            id (str):
            also_known_as (list[str]):
            verification_method (list[GetPlatformDidDocumentResponse200VerificationMethodItem]):
            authentication (list[str]):
            assertion_method (list[str]):
            key_agreement (list[str]):
            service (list[GetPlatformDidDocumentResponse200ServiceItem]):
     """

    context: list[GetPlatformDidDocumentResponse200ContextItemType1 | str]
    id: str
    also_known_as: list[str]
    verification_method: list[GetPlatformDidDocumentResponse200VerificationMethodItem]
    authentication: list[str]
    assertion_method: list[str]
    key_agreement: list[str]
    service: list[GetPlatformDidDocumentResponse200ServiceItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_platform_did_document_response_200_context_item_type_1 import GetPlatformDidDocumentResponse200ContextItemType1 # noqa: PLC0415
        from ..models.get_platform_did_document_response_200_service_item import GetPlatformDidDocumentResponse200ServiceItem # noqa: PLC0415
        from ..models.get_platform_did_document_response_200_verification_method_item import GetPlatformDidDocumentResponse200VerificationMethodItem # noqa: PLC0415
        context = []
        for context_item_data in self.context:
            context_item: dict[str, Any] | str
            if isinstance(context_item_data, GetPlatformDidDocumentResponse200ContextItemType1):
                context_item = context_item_data.to_dict()
            else:
                context_item = context_item_data
            context.append(context_item)



        id = self.id

        also_known_as = self.also_known_as



        verification_method = []
        for verification_method_item_data in self.verification_method:
            verification_method_item = verification_method_item_data.to_dict()
            verification_method.append(verification_method_item)



        authentication = self.authentication



        assertion_method = self.assertion_method



        key_agreement = self.key_agreement



        service = []
        for service_item_data in self.service:
            service_item = service_item_data.to_dict()
            service.append(service_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "@context": context,
            "id": id,
            "alsoKnownAs": also_known_as,
            "verificationMethod": verification_method,
            "authentication": authentication,
            "assertionMethod": assertion_method,
            "keyAgreement": key_agreement,
            "service": service,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_platform_did_document_response_200_context_item_type_1 import GetPlatformDidDocumentResponse200ContextItemType1 # noqa: PLC0415
        from ..models.get_platform_did_document_response_200_service_item import GetPlatformDidDocumentResponse200ServiceItem # noqa: PLC0415
        from ..models.get_platform_did_document_response_200_verification_method_item import GetPlatformDidDocumentResponse200VerificationMethodItem # noqa: PLC0415
        d = dict(src_dict)
        context = []
        _context = d.pop("@context")
        for context_item_data in (_context):
            def _parse_context_item(data: object) -> GetPlatformDidDocumentResponse200ContextItemType1 | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    context_item_type_1 = GetPlatformDidDocumentResponse200ContextItemType1.from_dict(data)



                    return context_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(GetPlatformDidDocumentResponse200ContextItemType1 | str, data)

            context_item = _parse_context_item(context_item_data)

            context.append(context_item)


        id = d.pop("id")

        also_known_as = cast(list[str], d.pop("alsoKnownAs"))


        verification_method = []
        _verification_method = d.pop("verificationMethod")
        for verification_method_item_data in (_verification_method):
            verification_method_item = GetPlatformDidDocumentResponse200VerificationMethodItem.from_dict(verification_method_item_data)



            verification_method.append(verification_method_item)


        authentication = cast(list[str], d.pop("authentication"))


        assertion_method = cast(list[str], d.pop("assertionMethod"))


        key_agreement = cast(list[str], d.pop("keyAgreement"))


        service = []
        _service = d.pop("service")
        for service_item_data in (_service):
            service_item = GetPlatformDidDocumentResponse200ServiceItem.from_dict(service_item_data)



            service.append(service_item)


        get_platform_did_document_response_200 = cls(
            context=context,
            id=id,
            also_known_as=also_known_as,
            verification_method=verification_method,
            authentication=authentication,
            assertion_method=assertion_method,
            key_agreement=key_agreement,
            service=service,
        )

        return get_platform_did_document_response_200

