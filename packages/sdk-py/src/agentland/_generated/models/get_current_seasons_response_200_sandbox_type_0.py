from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_current_seasons_response_200_sandbox_type_0_status import GetCurrentSeasonsResponse200SandboxType0Status
from uuid import UUID






T = TypeVar("T", bound="GetCurrentSeasonsResponse200SandboxType0")



@_attrs_define
class GetCurrentSeasonsResponse200SandboxType0:
    """ 
        Attributes:
            id (UUID):
            number (int):
            name (str):
            starts_at (str):
            ends_at (str):
            status (GetCurrentSeasonsResponse200SandboxType0Status):
            is_sandbox (bool):
            n_agents (int):
     """

    id: UUID
    number: int
    name: str
    starts_at: str
    ends_at: str
    status: GetCurrentSeasonsResponse200SandboxType0Status
    is_sandbox: bool
    n_agents: int





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        number = self.number

        name = self.name

        starts_at = self.starts_at

        ends_at = self.ends_at

        status = self.status.value

        is_sandbox = self.is_sandbox

        n_agents = self.n_agents


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "number": number,
            "name": name,
            "starts_at": starts_at,
            "ends_at": ends_at,
            "status": status,
            "is_sandbox": is_sandbox,
            "n_agents": n_agents,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        number = d.pop("number")

        name = d.pop("name")

        starts_at = d.pop("starts_at")

        ends_at = d.pop("ends_at")

        status = GetCurrentSeasonsResponse200SandboxType0Status(d.pop("status"))




        is_sandbox = d.pop("is_sandbox")

        n_agents = d.pop("n_agents")

        get_current_seasons_response_200_sandbox_type_0 = cls(
            id=id,
            number=number,
            name=name,
            starts_at=starts_at,
            ends_at=ends_at,
            status=status,
            is_sandbox=is_sandbox,
            n_agents=n_agents,
        )

        return get_current_seasons_response_200_sandbox_type_0

