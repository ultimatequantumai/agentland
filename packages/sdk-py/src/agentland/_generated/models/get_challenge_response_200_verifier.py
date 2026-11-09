from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_challenge_response_200_verifier_cpu import GetChallengeResponse200VerifierCpu
from ..models.get_challenge_response_200_verifier_protocol import GetChallengeResponse200VerifierProtocol






T = TypeVar("T", bound="GetChallengeResponse200Verifier")



@_attrs_define
class GetChallengeResponse200Verifier:
    """ 
        Attributes:
            image (str):
            protocol (GetChallengeResponse200VerifierProtocol):
            cpu (GetChallengeResponse200VerifierCpu):
            memory_mib (int):
            time_limit_ms (int):
            source_tag (str):
     """

    image: str
    protocol: GetChallengeResponse200VerifierProtocol
    cpu: GetChallengeResponse200VerifierCpu
    memory_mib: int
    time_limit_ms: int
    source_tag: str





    def to_dict(self) -> dict[str, Any]:
        image = self.image

        protocol = self.protocol.value

        cpu = self.cpu.value

        memory_mib = self.memory_mib

        time_limit_ms = self.time_limit_ms

        source_tag = self.source_tag


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "image": image,
            "protocol": protocol,
            "cpu": cpu,
            "memory_mib": memory_mib,
            "time_limit_ms": time_limit_ms,
            "source_tag": source_tag,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image = d.pop("image")

        protocol = GetChallengeResponse200VerifierProtocol(d.pop("protocol"))




        cpu = GetChallengeResponse200VerifierCpu(d.pop("cpu"))




        memory_mib = d.pop("memory_mib")

        time_limit_ms = d.pop("time_limit_ms")

        source_tag = d.pop("source_tag")

        get_challenge_response_200_verifier = cls(
            image=image,
            protocol=protocol,
            cpu=cpu,
            memory_mib=memory_mib,
            time_limit_ms=time_limit_ms,
            source_tag=source_tag,
        )

        return get_challenge_response_200_verifier

