from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_health_response_503_status import GetHealthResponse503Status
from typing import cast

if TYPE_CHECKING:
  from ..models.get_health_response_503_dependencies import GetHealthResponse503Dependencies





T = TypeVar("T", bound="GetHealthResponse503")



@_attrs_define
class GetHealthResponse503:
    """ 
        Attributes:
            status (GetHealthResponse503Status):
            dependencies (GetHealthResponse503Dependencies):
     """

    status: GetHealthResponse503Status
    dependencies: GetHealthResponse503Dependencies
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_health_response_503_dependencies import GetHealthResponse503Dependencies # noqa: PLC0415
        status = self.status.value

        dependencies = self.dependencies.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "dependencies": dependencies,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_health_response_503_dependencies import GetHealthResponse503Dependencies # noqa: PLC0415
        d = dict(src_dict)
        status = GetHealthResponse503Status(d.pop("status"))




        dependencies = GetHealthResponse503Dependencies.from_dict(d.pop("dependencies"))




        get_health_response_503 = cls(
            status=status,
            dependencies=dependencies,
        )


        get_health_response_503.additional_properties = d
        return get_health_response_503

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
