from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_seasons_response_200_data_item_status import ListSeasonsResponse200DataItemStatus
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ListSeasonsResponse200DataItem")



@_attrs_define
class ListSeasonsResponse200DataItem:
    """ 
        Attributes:
            id (UUID):
            number (int):
            name (str):
            starts_at (str):
            ends_at (str):
            status (ListSeasonsResponse200DataItemStatus):
            is_sandbox (bool):
            n_agents (int):
            scoring_version (None | str):
     """

    id: UUID
    number: int
    name: str
    starts_at: str
    ends_at: str
    status: ListSeasonsResponse200DataItemStatus
    is_sandbox: bool
    n_agents: int
    scoring_version: None | str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        number = self.number

        name = self.name

        starts_at = self.starts_at

        ends_at = self.ends_at

        status = self.status.value

        is_sandbox = self.is_sandbox

        n_agents = self.n_agents

        scoring_version: None | str
        scoring_version = self.scoring_version


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
            "scoring_version": scoring_version,
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

        status = ListSeasonsResponse200DataItemStatus(d.pop("status"))




        is_sandbox = d.pop("is_sandbox")

        n_agents = d.pop("n_agents")

        def _parse_scoring_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        scoring_version = _parse_scoring_version(d.pop("scoring_version"))


        list_seasons_response_200_data_item = cls(
            id=id,
            number=number,
            name=name,
            starts_at=starts_at,
            ends_at=ends_at,
            status=status,
            is_sandbox=is_sandbox,
            n_agents=n_agents,
            scoring_version=scoring_version,
        )

        return list_seasons_response_200_data_item

