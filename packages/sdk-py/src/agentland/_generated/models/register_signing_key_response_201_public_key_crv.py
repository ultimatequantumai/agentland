from enum import StrEnum

class RegisterSigningKeyResponse201PublicKeyCrv(StrEnum):
    ED25519 = "Ed25519"

    def __str__(self) -> str:
        return str(self.value)
