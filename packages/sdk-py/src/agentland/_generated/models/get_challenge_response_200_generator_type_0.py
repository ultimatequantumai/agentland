from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_challenge_response_200_generator_type_0_params import GetChallengeResponse200GeneratorType0Params





T = TypeVar("T", bound="GetChallengeResponse200GeneratorType0")



@_attrs_define
class GetChallengeResponse200GeneratorType0:
    """ 
        Attributes:
            version (int):
            seed (int):
            params (GetChallengeResponse200GeneratorType0Params):
     """

    version: int
    seed: int
    params: GetChallengeResponse200GeneratorType0Params





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_challenge_response_200_generator_type_0_params import GetChallengeResponse200GeneratorType0Params # noqa: PLC0415
        version = self.version

        seed = self.seed

        params = self.params.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "version": version,
            "seed": seed,
            "params": params,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_challenge_response_200_generator_type_0_params import GetChallengeResponse200GeneratorType0Params # noqa: PLC0415
        d = dict(src_dict)
        version = d.pop("version")

        seed = d.pop("seed")

        params = GetChallengeResponse200GeneratorType0Params.from_dict(d.pop("params"))




        get_challenge_response_200_generator_type_0 = cls(
            version=version,
            seed=seed,
            params=params,
        )

        return get_challenge_response_200_generator_type_0

