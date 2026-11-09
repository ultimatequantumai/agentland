from enum import StrEnum

class RegisterSigningKeyResponse201PublicKeyKty(StrEnum):
    OKP = "OKP"

    def __str__(self) -> str:
        return str(self.value)
