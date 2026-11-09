from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_current_seasons_response_200_public_type_0 import GetCurrentSeasonsResponse200PublicType0
  from ..models.get_current_seasons_response_200_sandbox_type_0 import GetCurrentSeasonsResponse200SandboxType0





T = TypeVar("T", bound="GetCurrentSeasonsResponse200")



@_attrs_define
class GetCurrentSeasonsResponse200:
    """ 
        Attributes:
            public (GetCurrentSeasonsResponse200PublicType0 | None):
            sandbox (GetCurrentSeasonsResponse200SandboxType0 | None):
     """

    public: GetCurrentSeasonsResponse200PublicType0 | None
    sandbox: GetCurrentSeasonsResponse200SandboxType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_current_seasons_response_200_public_type_0 import GetCurrentSeasonsResponse200PublicType0 # noqa: PLC0415
        from ..models.get_current_seasons_response_200_sandbox_type_0 import GetCurrentSeasonsResponse200SandboxType0 # noqa: PLC0415
        public: dict[str, Any] | None
        if isinstance(self.public, GetCurrentSeasonsResponse200PublicType0):
            public = self.public.to_dict()
        else:
            public = self.public

        sandbox: dict[str, Any] | None
        if isinstance(self.sandbox, GetCurrentSeasonsResponse200SandboxType0):
            sandbox = self.sandbox.to_dict()
        else:
            sandbox = self.sandbox


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "public": public,
            "sandbox": sandbox,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_current_seasons_response_200_public_type_0 import GetCurrentSeasonsResponse200PublicType0 # noqa: PLC0415
        from ..models.get_current_seasons_response_200_sandbox_type_0 import GetCurrentSeasonsResponse200SandboxType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_public(data: object) -> GetCurrentSeasonsResponse200PublicType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                public_type_0 = GetCurrentSeasonsResponse200PublicType0.from_dict(data)



                return public_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCurrentSeasonsResponse200PublicType0 | None, data)

        public = _parse_public(d.pop("public"))


        def _parse_sandbox(data: object) -> GetCurrentSeasonsResponse200SandboxType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sandbox_type_0 = GetCurrentSeasonsResponse200SandboxType0.from_dict(data)



                return sandbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetCurrentSeasonsResponse200SandboxType0 | None, data)

        sandbox = _parse_sandbox(d.pop("sandbox"))


        get_current_seasons_response_200 = cls(
            public=public,
            sandbox=sandbox,
        )

        return get_current_seasons_response_200

