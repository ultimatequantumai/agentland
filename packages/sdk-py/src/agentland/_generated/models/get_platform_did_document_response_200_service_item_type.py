from enum import StrEnum

class GetPlatformDidDocumentResponse200ServiceItemType(StrEnum):
    AGENTLANDTRUST = "AgentLandTrust"

    def __str__(self) -> str:
        return str(self.value)
