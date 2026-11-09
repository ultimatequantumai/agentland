from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.passkey_generate_authenticate_options_response_200_allow_credentials_item import PasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem
  from ..models.passkey_generate_authenticate_options_response_200_authenticator_selection import PasskeyGenerateAuthenticateOptionsResponse200AuthenticatorSelection
  from ..models.passkey_generate_authenticate_options_response_200_extensions import PasskeyGenerateAuthenticateOptionsResponse200Extensions
  from ..models.passkey_generate_authenticate_options_response_200_rp import PasskeyGenerateAuthenticateOptionsResponse200Rp
  from ..models.passkey_generate_authenticate_options_response_200_user import PasskeyGenerateAuthenticateOptionsResponse200User





T = TypeVar("T", bound="PasskeyGenerateAuthenticateOptionsResponse200")



@_attrs_define
class PasskeyGenerateAuthenticateOptionsResponse200:
    """ 
        Attributes:
            challenge (str | Unset):
            rp (PasskeyGenerateAuthenticateOptionsResponse200Rp | Unset):
            user (PasskeyGenerateAuthenticateOptionsResponse200User | Unset):
            timeout (float | Unset):
            allow_credentials (list[PasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem] | Unset):
            user_verification (str | Unset):
            authenticator_selection (PasskeyGenerateAuthenticateOptionsResponse200AuthenticatorSelection | Unset):
            extensions (PasskeyGenerateAuthenticateOptionsResponse200Extensions | Unset):
     """

    challenge: str | Unset = UNSET
    rp: PasskeyGenerateAuthenticateOptionsResponse200Rp | Unset = UNSET
    user: PasskeyGenerateAuthenticateOptionsResponse200User | Unset = UNSET
    timeout: float | Unset = UNSET
    allow_credentials: list[PasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem] | Unset = UNSET
    user_verification: str | Unset = UNSET
    authenticator_selection: PasskeyGenerateAuthenticateOptionsResponse200AuthenticatorSelection | Unset = UNSET
    extensions: PasskeyGenerateAuthenticateOptionsResponse200Extensions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.passkey_generate_authenticate_options_response_200_allow_credentials_item import PasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem # noqa: PLC0415
        from ..models.passkey_generate_authenticate_options_response_200_authenticator_selection import PasskeyGenerateAuthenticateOptionsResponse200AuthenticatorSelection # noqa: PLC0415
        from ..models.passkey_generate_authenticate_options_response_200_extensions import PasskeyGenerateAuthenticateOptionsResponse200Extensions # noqa: PLC0415
        from ..models.passkey_generate_authenticate_options_response_200_rp import PasskeyGenerateAuthenticateOptionsResponse200Rp # noqa: PLC0415
        from ..models.passkey_generate_authenticate_options_response_200_user import PasskeyGenerateAuthenticateOptionsResponse200User # noqa: PLC0415
        challenge = self.challenge

        rp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rp, Unset):
            rp = self.rp.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        timeout = self.timeout

        allow_credentials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allow_credentials, Unset):
            allow_credentials = []
            for allow_credentials_item_data in self.allow_credentials:
                allow_credentials_item = allow_credentials_item_data.to_dict()
                allow_credentials.append(allow_credentials_item)



        user_verification = self.user_verification

        authenticator_selection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authenticator_selection, Unset):
            authenticator_selection = self.authenticator_selection.to_dict()

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if challenge is not UNSET:
            field_dict["challenge"] = challenge
        if rp is not UNSET:
            field_dict["rp"] = rp
        if user is not UNSET:
            field_dict["user"] = user
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if allow_credentials is not UNSET:
            field_dict["allowCredentials"] = allow_credentials
        if user_verification is not UNSET:
            field_dict["userVerification"] = user_verification
        if authenticator_selection is not UNSET:
            field_dict["authenticatorSelection"] = authenticator_selection
        if extensions is not UNSET:
            field_dict["extensions"] = extensions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.passkey_generate_authenticate_options_response_200_allow_credentials_item import PasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem # noqa: PLC0415
        from ..models.passkey_generate_authenticate_options_response_200_authenticator_selection import PasskeyGenerateAuthenticateOptionsResponse200AuthenticatorSelection # noqa: PLC0415
        from ..models.passkey_generate_authenticate_options_response_200_extensions import PasskeyGenerateAuthenticateOptionsResponse200Extensions # noqa: PLC0415
        from ..models.passkey_generate_authenticate_options_response_200_rp import PasskeyGenerateAuthenticateOptionsResponse200Rp # noqa: PLC0415
        from ..models.passkey_generate_authenticate_options_response_200_user import PasskeyGenerateAuthenticateOptionsResponse200User # noqa: PLC0415
        d = dict(src_dict)
        challenge = d.pop("challenge", UNSET)

        _rp = d.pop("rp", UNSET)
        rp: PasskeyGenerateAuthenticateOptionsResponse200Rp | Unset
        if isinstance(_rp,  Unset):
            rp = UNSET
        else:
            rp = PasskeyGenerateAuthenticateOptionsResponse200Rp.from_dict(_rp)




        _user = d.pop("user", UNSET)
        user: PasskeyGenerateAuthenticateOptionsResponse200User | Unset
        if isinstance(_user,  Unset):
            user = UNSET
        else:
            user = PasskeyGenerateAuthenticateOptionsResponse200User.from_dict(_user)




        timeout = d.pop("timeout", UNSET)

        _allow_credentials = d.pop("allowCredentials", UNSET)
        allow_credentials: list[PasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem] | Unset = UNSET
        if _allow_credentials is not UNSET:
            allow_credentials = []
            for allow_credentials_item_data in _allow_credentials:
                allow_credentials_item = PasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem.from_dict(allow_credentials_item_data)



                allow_credentials.append(allow_credentials_item)


        user_verification = d.pop("userVerification", UNSET)

        _authenticator_selection = d.pop("authenticatorSelection", UNSET)
        authenticator_selection: PasskeyGenerateAuthenticateOptionsResponse200AuthenticatorSelection | Unset
        if isinstance(_authenticator_selection,  Unset):
            authenticator_selection = UNSET
        else:
            authenticator_selection = PasskeyGenerateAuthenticateOptionsResponse200AuthenticatorSelection.from_dict(_authenticator_selection)




        _extensions = d.pop("extensions", UNSET)
        extensions: PasskeyGenerateAuthenticateOptionsResponse200Extensions | Unset
        if isinstance(_extensions,  Unset):
            extensions = UNSET
        else:
            extensions = PasskeyGenerateAuthenticateOptionsResponse200Extensions.from_dict(_extensions)




        passkey_generate_authenticate_options_response_200 = cls(
            challenge=challenge,
            rp=rp,
            user=user,
            timeout=timeout,
            allow_credentials=allow_credentials,
            user_verification=user_verification,
            authenticator_selection=authenticator_selection,
            extensions=extensions,
        )


        passkey_generate_authenticate_options_response_200.additional_properties = d
        return passkey_generate_authenticate_options_response_200

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
