from enum import StrEnum

class GetOperatorAgentResponse200PublicSigningKeyKty(StrEnum):
    OKP = "OKP"

    def __str__(self) -> str:
        return str(self.value)
