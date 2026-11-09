from enum import StrEnum

class RotateSigningKeyBodyNewPublicKeyKty(StrEnum):
    OKP = "OKP"

    def __str__(self) -> str:
        return str(self.value)
