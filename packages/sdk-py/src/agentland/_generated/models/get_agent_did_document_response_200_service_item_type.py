from enum import StrEnum

class GetAgentDidDocumentResponse200ServiceItemType(StrEnum):
    AGENTLANDTRUST = "AgentLandTrust"

    def __str__(self) -> str:
        return str(self.value)
