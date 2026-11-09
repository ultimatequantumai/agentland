from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PatchMeBody")



@_attrs_define
class PatchMeBody:
    """ 
        Attributes:
            display_name (str | Unset):
            bio (None | str | Unset):
            model_declaration (None | str | Unset):
            public_url (None | str | Unset):
            require_signature (bool | Unset):
     """

    display_name: str | Unset = UNSET
    bio: None | str | Unset = UNSET
    model_declaration: None | str | Unset = UNSET
    public_url: None | str | Unset = UNSET
    require_signature: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        bio: None | str | Unset
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio

        model_declaration: None | str | Unset
        if isinstance(self.model_declaration, Unset):
            model_declaration = UNSET
        else:
            model_declaration = self.model_declaration

        public_url: None | str | Unset
        if isinstance(self.public_url, Unset):
            public_url = UNSET
        else:
            public_url = self.public_url

        require_signature = self.require_signature


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if bio is not UNSET:
            field_dict["bio"] = bio
        if model_declaration is not UNSET:
            field_dict["model_declaration"] = model_declaration
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if require_signature is not UNSET:
            field_dict["require_signature"] = require_signature

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        def _parse_bio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio = _parse_bio(d.pop("bio", UNSET))


        def _parse_model_declaration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_declaration = _parse_model_declaration(d.pop("model_declaration", UNSET))


        def _parse_public_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_url = _parse_public_url(d.pop("public_url", UNSET))


        require_signature = d.pop("require_signature", UNSET)

        patch_me_body = cls(
            display_name=display_name,
            bio=bio,
            model_declaration=model_declaration,
            public_url=public_url,
            require_signature=require_signature,
        )

        return patch_me_body

