from enum import StrEnum

class RegisterSigningKeyBodyPublicKeyKty(StrEnum):
    OKP = "OKP"

    def __str__(self) -> str:
        return str(self.value)
