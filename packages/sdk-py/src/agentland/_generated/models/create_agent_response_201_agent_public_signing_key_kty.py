from enum import StrEnum

class CreateAgentResponse201AgentPublicSigningKeyKty(StrEnum):
    OKP = "OKP"

    def __str__(self) -> str:
        return str(self.value)
