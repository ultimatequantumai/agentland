from enum import StrEnum

class StartRecoveryResponse201NewPublicKeyKty(StrEnum):
    OKP = "OKP"

    def __str__(self) -> str:
        return str(self.value)
