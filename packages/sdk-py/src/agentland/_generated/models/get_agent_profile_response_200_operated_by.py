from enum import StrEnum

class GetAgentProfileResponse200OperatedBy(StrEnum):
    AGENTLAND = "agentland"

    def __str__(self) -> str:
        return str(self.value)
