from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.onboard_operator_body_kind import OnboardOperatorBodyKind
from ..types import UNSET, Unset






T = TypeVar("T", bound="OnboardOperatorBody")



@_attrs_define
class OnboardOperatorBody:
    """ 
        Attributes:
            name (str):
            accepted_terms (bool):
            accepted_aup (bool):
            accepted_honor_code (bool):
            kind (OnboardOperatorBodyKind | Unset):  Default: OnboardOperatorBodyKind.INDIVIDUAL.
     """

    name: str
    accepted_terms: bool
    accepted_aup: bool
    accepted_honor_code: bool
    kind: OnboardOperatorBodyKind | Unset = OnboardOperatorBodyKind.INDIVIDUAL





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        accepted_terms = self.accepted_terms

        accepted_aup = self.accepted_aup

        accepted_honor_code = self.accepted_honor_code

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "accepted_terms": accepted_terms,
            "accepted_aup": accepted_aup,
            "accepted_honor_code": accepted_honor_code,
        })
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        accepted_terms = d.pop("accepted_terms")

        accepted_aup = d.pop("accepted_aup")

        accepted_honor_code = d.pop("accepted_honor_code")

        _kind = d.pop("kind", UNSET)
        kind: OnboardOperatorBodyKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = OnboardOperatorBodyKind(_kind)




        onboard_operator_body = cls(
            name=name,
            accepted_terms=accepted_terms,
            accepted_aup=accepted_aup,
            accepted_honor_code=accepted_honor_code,
            kind=kind,
        )

        return onboard_operator_body

