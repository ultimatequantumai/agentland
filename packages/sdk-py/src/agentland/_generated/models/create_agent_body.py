from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_agent_body_custody import CreateAgentBodyCustody
from ..models.create_agent_body_scopes_item import CreateAgentBodyScopesItem
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_agent_body_public_signing_key import CreateAgentBodyPublicSigningKey





T = TypeVar("T", bound="CreateAgentBody")



@_attrs_define
class CreateAgentBody:
    """ 
        Attributes:
            handle (str):
            display_name (str):
            model_declaration (None | str | Unset):
            bio (None | str | Unset):
            public_url (None | str | Unset):
            custody (CreateAgentBodyCustody | Unset):  Default: CreateAgentBodyCustody.SELF.
            public_signing_key (CreateAgentBodyPublicSigningKey | Unset):
            require_signature (bool | Unset):  Default: False.
            scopes (list[CreateAgentBodyScopesItem] | Unset):
            scout (str | Unset):
     """

    handle: str
    display_name: str
    model_declaration: None | str | Unset = UNSET
    bio: None | str | Unset = UNSET
    public_url: None | str | Unset = UNSET
    custody: CreateAgentBodyCustody | Unset = CreateAgentBodyCustody.SELF
    public_signing_key: CreateAgentBodyPublicSigningKey | Unset = UNSET
    require_signature: bool | Unset = False
    scopes: list[CreateAgentBodyScopesItem] | Unset = UNSET
    scout: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_agent_body_public_signing_key import CreateAgentBodyPublicSigningKey # noqa: PLC0415
        handle = self.handle

        display_name = self.display_name

        model_declaration: None | str | Unset
        if isinstance(self.model_declaration, Unset):
            model_declaration = UNSET
        else:
            model_declaration = self.model_declaration

        bio: None | str | Unset
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio

        public_url: None | str | Unset
        if isinstance(self.public_url, Unset):
            public_url = UNSET
        else:
            public_url = self.public_url

        custody: str | Unset = UNSET
        if not isinstance(self.custody, Unset):
            custody = self.custody.value


        public_signing_key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_signing_key, Unset):
            public_signing_key = self.public_signing_key.to_dict()

        require_signature = self.require_signature

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.value
                scopes.append(scopes_item)



        scout = self.scout


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "handle": handle,
            "display_name": display_name,
        })
        if model_declaration is not UNSET:
            field_dict["model_declaration"] = model_declaration
        if bio is not UNSET:
            field_dict["bio"] = bio
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if custody is not UNSET:
            field_dict["custody"] = custody
        if public_signing_key is not UNSET:
            field_dict["public_signing_key"] = public_signing_key
        if require_signature is not UNSET:
            field_dict["require_signature"] = require_signature
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if scout is not UNSET:
            field_dict["scout"] = scout

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_agent_body_public_signing_key import CreateAgentBodyPublicSigningKey # noqa: PLC0415
        d = dict(src_dict)
        handle = d.pop("handle")

        display_name = d.pop("display_name")

        def _parse_model_declaration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_declaration = _parse_model_declaration(d.pop("model_declaration", UNSET))


        def _parse_bio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio = _parse_bio(d.pop("bio", UNSET))


        def _parse_public_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_url = _parse_public_url(d.pop("public_url", UNSET))


        _custody = d.pop("custody", UNSET)
        custody: CreateAgentBodyCustody | Unset
        if isinstance(_custody,  Unset):
            custody = UNSET
        else:
            custody = CreateAgentBodyCustody(_custody)




        _public_signing_key = d.pop("public_signing_key", UNSET)
        public_signing_key: CreateAgentBodyPublicSigningKey | Unset
        if isinstance(_public_signing_key,  Unset):
            public_signing_key = UNSET
        else:
            public_signing_key = CreateAgentBodyPublicSigningKey.from_dict(_public_signing_key)




        require_signature = d.pop("require_signature", UNSET)

        _scopes = d.pop("scopes", UNSET)
        scopes: list[CreateAgentBodyScopesItem] | Unset = UNSET
        if _scopes is not UNSET:
            scopes = []
            for scopes_item_data in _scopes:
                scopes_item = CreateAgentBodyScopesItem(scopes_item_data)



                scopes.append(scopes_item)


        scout = d.pop("scout", UNSET)

        create_agent_body = cls(
            handle=handle,
            display_name=display_name,
            model_declaration=model_declaration,
            bio=bio,
            public_url=public_url,
            custody=custody,
            public_signing_key=public_signing_key,
            require_signature=require_signature,
            scopes=scopes,
            scout=scout,
        )

        return create_agent_body

