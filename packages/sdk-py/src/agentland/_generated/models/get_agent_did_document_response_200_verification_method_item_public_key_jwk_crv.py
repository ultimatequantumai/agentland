from enum import StrEnum

class GetAgentDidDocumentResponse200VerificationMethodItemPublicKeyJwkCrv(StrEnum):
    ED25519 = "Ed25519"
    X25519 = "X25519"

    def __str__(self) -> str:
        return str(self.value)
