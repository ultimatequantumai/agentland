from enum import StrEnum

class CreateAgentBodyPublicSigningKeyKty(StrEnum):
    OKP = "OKP"

    def __str__(self) -> str:
        return str(self.value)
