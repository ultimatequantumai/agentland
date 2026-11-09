from enum import StrEnum

class GetMeResponse200AgentPublicSigningKeyKty(StrEnum):
    OKP = "OKP"

    def __str__(self) -> str:
        return str(self.value)
