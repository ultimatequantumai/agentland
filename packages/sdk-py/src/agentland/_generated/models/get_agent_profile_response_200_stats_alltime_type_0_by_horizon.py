from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_agent_profile_response_200_stats_alltime_type_0_by_horizon_additional_property import GetAgentProfileResponse200StatsAlltimeType0ByHorizonAdditionalProperty





T = TypeVar("T", bound="GetAgentProfileResponse200StatsAlltimeType0ByHorizon")



@_attrs_define
class GetAgentProfileResponse200StatsAlltimeType0ByHorizon:
    

    additional_properties: dict[str, GetAgentProfileResponse200StatsAlltimeType0ByHorizonAdditionalProperty] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_profile_response_200_stats_alltime_type_0_by_horizon_additional_property import GetAgentProfileResponse200StatsAlltimeType0ByHorizonAdditionalProperty # noqa: PLC0415
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_profile_response_200_stats_alltime_type_0_by_horizon_additional_property import GetAgentProfileResponse200StatsAlltimeType0ByHorizonAdditionalProperty # noqa: PLC0415
        d = dict(src_dict)
        get_agent_profile_response_200_stats_alltime_type_0_by_horizon = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GetAgentProfileResponse200StatsAlltimeType0ByHorizonAdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        get_agent_profile_response_200_stats_alltime_type_0_by_horizon.additional_properties = additional_properties
        return get_agent_profile_response_200_stats_alltime_type_0_by_horizon

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> GetAgentProfileResponse200StatsAlltimeType0ByHorizonAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: GetAgentProfileResponse200StatsAlltimeType0ByHorizonAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
