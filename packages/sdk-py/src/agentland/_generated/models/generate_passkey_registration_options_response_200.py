from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.generate_passkey_registration_options_response_200_authenticator_selection import GeneratePasskeyRegistrationOptionsResponse200AuthenticatorSelection
  from ..models.generate_passkey_registration_options_response_200_exclude_credentials_item import GeneratePasskeyRegistrationOptionsResponse200ExcludeCredentialsItem
  from ..models.generate_passkey_registration_options_response_200_extensions import GeneratePasskeyRegistrationOptionsResponse200Extensions
  from ..models.generate_passkey_registration_options_response_200_pub_key_cred_params_item import GeneratePasskeyRegistrationOptionsResponse200PubKeyCredParamsItem
  from ..models.generate_passkey_registration_options_response_200_rp import GeneratePasskeyRegistrationOptionsResponse200Rp
  from ..models.generate_passkey_registration_options_response_200_user import GeneratePasskeyRegistrationOptionsResponse200User





T = TypeVar("T", bound="GeneratePasskeyRegistrationOptionsResponse200")



@_attrs_define
class GeneratePasskeyRegistrationOptionsResponse200:
    """ 
        Attributes:
            challenge (str | Unset):
            rp (GeneratePasskeyRegistrationOptionsResponse200Rp | Unset):
            user (GeneratePasskeyRegistrationOptionsResponse200User | Unset):
            pub_key_cred_params (list[GeneratePasskeyRegistrationOptionsResponse200PubKeyCredParamsItem] | Unset):
            timeout (float | Unset):
            exclude_credentials (list[GeneratePasskeyRegistrationOptionsResponse200ExcludeCredentialsItem] | Unset):
            authenticator_selection (GeneratePasskeyRegistrationOptionsResponse200AuthenticatorSelection | Unset):
            attestation (str | Unset):
            extensions (GeneratePasskeyRegistrationOptionsResponse200Extensions | Unset):
     """

    challenge: str | Unset = UNSET
    rp: GeneratePasskeyRegistrationOptionsResponse200Rp | Unset = UNSET
    user: GeneratePasskeyRegistrationOptionsResponse200User | Unset = UNSET
    pub_key_cred_params: list[GeneratePasskeyRegistrationOptionsResponse200PubKeyCredParamsItem] | Unset = UNSET
    timeout: float | Unset = UNSET
    exclude_credentials: list[GeneratePasskeyRegistrationOptionsResponse200ExcludeCredentialsItem] | Unset = UNSET
    authenticator_selection: GeneratePasskeyRegistrationOptionsResponse200AuthenticatorSelection | Unset = UNSET
    attestation: str | Unset = UNSET
    extensions: GeneratePasskeyRegistrationOptionsResponse200Extensions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.generate_passkey_registration_options_response_200_authenticator_selection import GeneratePasskeyRegistrationOptionsResponse200AuthenticatorSelection # noqa: PLC0415
        from ..models.generate_passkey_registration_options_response_200_exclude_credentials_item import GeneratePasskeyRegistrationOptionsResponse200ExcludeCredentialsItem # noqa: PLC0415
        from ..models.generate_passkey_registration_options_response_200_extensions import GeneratePasskeyRegistrationOptionsResponse200Extensions # noqa: PLC0415
        from ..models.generate_passkey_registration_options_response_200_pub_key_cred_params_item import GeneratePasskeyRegistrationOptionsResponse200PubKeyCredParamsItem # noqa: PLC0415
        from ..models.generate_passkey_registration_options_response_200_rp import GeneratePasskeyRegistrationOptionsResponse200Rp # noqa: PLC0415
        from ..models.generate_passkey_registration_options_response_200_user import GeneratePasskeyRegistrationOptionsResponse200User # noqa: PLC0415
        challenge = self.challenge

        rp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rp, Unset):
            rp = self.rp.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        pub_key_cred_params: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pub_key_cred_params, Unset):
            pub_key_cred_params = []
            for pub_key_cred_params_item_data in self.pub_key_cred_params:
                pub_key_cred_params_item = pub_key_cred_params_item_data.to_dict()
                pub_key_cred_params.append(pub_key_cred_params_item)



        timeout = self.timeout

        exclude_credentials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exclude_credentials, Unset):
            exclude_credentials = []
            for exclude_credentials_item_data in self.exclude_credentials:
                exclude_credentials_item = exclude_credentials_item_data.to_dict()
                exclude_credentials.append(exclude_credentials_item)



        authenticator_selection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authenticator_selection, Unset):
            authenticator_selection = self.authenticator_selection.to_dict()

        attestation = self.attestation

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
        if pub_key_cred_params is not UNSET:
            field_dict["pubKeyCredParams"] = pub_key_cred_params
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if exclude_credentials is not UNSET:
            field_dict["excludeCredentials"] = exclude_credentials
        if authenticator_selection is not UNSET:
            field_dict["authenticatorSelection"] = authenticator_selection
        if attestation is not UNSET:
            field_dict["attestation"] = attestation
        if extensions is not UNSET:
            field_dict["extensions"] = extensions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_passkey_registration_options_response_200_authenticator_selection import GeneratePasskeyRegistrationOptionsResponse200AuthenticatorSelection # noqa: PLC0415
        from ..models.generate_passkey_registration_options_response_200_exclude_credentials_item import GeneratePasskeyRegistrationOptionsResponse200ExcludeCredentialsItem # noqa: PLC0415
        from ..models.generate_passkey_registration_options_response_200_extensions import GeneratePasskeyRegistrationOptionsResponse200Extensions # noqa: PLC0415
        from ..models.generate_passkey_registration_options_response_200_pub_key_cred_params_item import GeneratePasskeyRegistrationOptionsResponse200PubKeyCredParamsItem # noqa: PLC0415
        from ..models.generate_passkey_registration_options_response_200_rp import GeneratePasskeyRegistrationOptionsResponse200Rp # noqa: PLC0415
        from ..models.generate_passkey_registration_options_response_200_user import GeneratePasskeyRegistrationOptionsResponse200User # noqa: PLC0415
        d = dict(src_dict)
        challenge = d.pop("challenge", UNSET)

        _rp = d.pop("rp", UNSET)
        rp: GeneratePasskeyRegistrationOptionsResponse200Rp | Unset
        if isinstance(_rp,  Unset):
            rp = UNSET
        else:
            rp = GeneratePasskeyRegistrationOptionsResponse200Rp.from_dict(_rp)




        _user = d.pop("user", UNSET)
        user: GeneratePasskeyRegistrationOptionsResponse200User | Unset
        if isinstance(_user,  Unset):
            user = UNSET
        else:
            user = GeneratePasskeyRegistrationOptionsResponse200User.from_dict(_user)




        _pub_key_cred_params = d.pop("pubKeyCredParams", UNSET)
        pub_key_cred_params: list[GeneratePasskeyRegistrationOptionsResponse200PubKeyCredParamsItem] | Unset = UNSET
        if _pub_key_cred_params is not UNSET:
            pub_key_cred_params = []
            for pub_key_cred_params_item_data in _pub_key_cred_params:
                pub_key_cred_params_item = GeneratePasskeyRegistrationOptionsResponse200PubKeyCredParamsItem.from_dict(pub_key_cred_params_item_data)



                pub_key_cred_params.append(pub_key_cred_params_item)


        timeout = d.pop("timeout", UNSET)

        _exclude_credentials = d.pop("excludeCredentials", UNSET)
        exclude_credentials: list[GeneratePasskeyRegistrationOptionsResponse200ExcludeCredentialsItem] | Unset = UNSET
        if _exclude_credentials is not UNSET:
            exclude_credentials = []
            for exclude_credentials_item_data in _exclude_credentials:
                exclude_credentials_item = GeneratePasskeyRegistrationOptionsResponse200ExcludeCredentialsItem.from_dict(exclude_credentials_item_data)



                exclude_credentials.append(exclude_credentials_item)


        _authenticator_selection = d.pop("authenticatorSelection", UNSET)
        authenticator_selection: GeneratePasskeyRegistrationOptionsResponse200AuthenticatorSelection | Unset
        if isinstance(_authenticator_selection,  Unset):
            authenticator_selection = UNSET
        else:
            authenticator_selection = GeneratePasskeyRegistrationOptionsResponse200AuthenticatorSelection.from_dict(_authenticator_selection)




        attestation = d.pop("attestation", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: GeneratePasskeyRegistrationOptionsResponse200Extensions | Unset
        if isinstance(_extensions,  Unset):
            extensions = UNSET
        else:
            extensions = GeneratePasskeyRegistrationOptionsResponse200Extensions.from_dict(_extensions)




        generate_passkey_registration_options_response_200 = cls(
            challenge=challenge,
            rp=rp,
            user=user,
            pub_key_cred_params=pub_key_cred_params,
            timeout=timeout,
            exclude_credentials=exclude_credentials,
            authenticator_selection=authenticator_selection,
            attestation=attestation,
            extensions=extensions,
        )


        generate_passkey_registration_options_response_200.additional_properties = d
        return generate_passkey_registration_options_response_200

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
