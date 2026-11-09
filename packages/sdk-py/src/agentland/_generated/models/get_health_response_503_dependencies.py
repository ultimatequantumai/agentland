from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_health_response_503_dependencies_postgres import GetHealthResponse503DependenciesPostgres
from ..models.get_health_response_503_dependencies_redis import GetHealthResponse503DependenciesRedis






T = TypeVar("T", bound="GetHealthResponse503Dependencies")



@_attrs_define
class GetHealthResponse503Dependencies:
    """ 
        Attributes:
            postgres (GetHealthResponse503DependenciesPostgres):
            redis (GetHealthResponse503DependenciesRedis):
     """

    postgres: GetHealthResponse503DependenciesPostgres
    redis: GetHealthResponse503DependenciesRedis
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        postgres = self.postgres.value

        redis = self.redis.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "postgres": postgres,
            "redis": redis,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        postgres = GetHealthResponse503DependenciesPostgres(d.pop("postgres"))




        redis = GetHealthResponse503DependenciesRedis(d.pop("redis"))




        get_health_response_503_dependencies = cls(
            postgres=postgres,
            redis=redis,
        )


        get_health_response_503_dependencies.additional_properties = d
        return get_health_response_503_dependencies

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
