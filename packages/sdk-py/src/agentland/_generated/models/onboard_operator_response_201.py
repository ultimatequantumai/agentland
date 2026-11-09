from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.onboard_operator_response_201_kind import OnboardOperatorResponse201Kind
from ..models.onboard_operator_response_201_status import OnboardOperatorResponse201Status
from ..models.onboard_operator_response_201_tier import OnboardOperatorResponse201Tier
from uuid import UUID






T = TypeVar("T", bound="OnboardOperatorResponse201")



@_attrs_define
class OnboardOperatorResponse201:
    """ 
        Attributes:
            id (UUID):
            email (str):
            name (str):
            kind (OnboardOperatorResponse201Kind):
            tier (OnboardOperatorResponse201Tier):
            status (OnboardOperatorResponse201Status):
     """

    id: UUID
    email: str
    name: str
    kind: OnboardOperatorResponse201Kind
    tier: OnboardOperatorResponse201Tier
    status: OnboardOperatorResponse201Status





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        email = self.email

        name = self.name

        kind = self.kind.value

        tier = self.tier.value

        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "email": email,
            "name": name,
            "kind": kind,
            "tier": tier,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        email = d.pop("email")

        name = d.pop("name")

        kind = OnboardOperatorResponse201Kind(d.pop("kind"))




        tier = OnboardOperatorResponse201Tier(d.pop("tier"))




        status = OnboardOperatorResponse201Status(d.pop("status"))




        onboard_operator_response_201 = cls(
            id=id,
            email=email,
            name=name,
            kind=kind,
            tier=tier,
            status=status,
        )

        return onboard_operator_response_201

