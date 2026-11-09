from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.create_agent_response_201_agent import CreateAgentResponse201Agent
  from ..models.create_agent_response_201_api_key import CreateAgentResponse201ApiKey
  from ..models.create_agent_response_201_scout_type_0 import CreateAgentResponse201ScoutType0





T = TypeVar("T", bound="CreateAgentResponse201")



@_attrs_define
class CreateAgentResponse201:
    """ 
        Attributes:
            agent (CreateAgentResponse201Agent):
            api_key (CreateAgentResponse201ApiKey):
            scout (CreateAgentResponse201ScoutType0 | None):
     """

    agent: CreateAgentResponse201Agent
    api_key: CreateAgentResponse201ApiKey
    scout: CreateAgentResponse201ScoutType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_agent_response_201_agent import CreateAgentResponse201Agent # noqa: PLC0415
        from ..models.create_agent_response_201_api_key import CreateAgentResponse201ApiKey # noqa: PLC0415
        from ..models.create_agent_response_201_scout_type_0 import CreateAgentResponse201ScoutType0 # noqa: PLC0415
        agent = self.agent.to_dict()

        api_key = self.api_key.to_dict()

        scout: dict[str, Any] | None
        if isinstance(self.scout, CreateAgentResponse201ScoutType0):
            scout = self.scout.to_dict()
        else:
            scout = self.scout


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "agent": agent,
            "api_key": api_key,
            "scout": scout,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_agent_response_201_agent import CreateAgentResponse201Agent # noqa: PLC0415
        from ..models.create_agent_response_201_api_key import CreateAgentResponse201ApiKey # noqa: PLC0415
        from ..models.create_agent_response_201_scout_type_0 import CreateAgentResponse201ScoutType0 # noqa: PLC0415
        d = dict(src_dict)
        agent = CreateAgentResponse201Agent.from_dict(d.pop("agent"))




        api_key = CreateAgentResponse201ApiKey.from_dict(d.pop("api_key"))




        def _parse_scout(data: object) -> CreateAgentResponse201ScoutType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scout_type_0 = CreateAgentResponse201ScoutType0.from_dict(data)



                return scout_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateAgentResponse201ScoutType0 | None, data)

        scout = _parse_scout(d.pop("scout"))


        create_agent_response_201 = cls(
            agent=agent,
            api_key=api_key,
            scout=scout,
        )

        return create_agent_response_201

