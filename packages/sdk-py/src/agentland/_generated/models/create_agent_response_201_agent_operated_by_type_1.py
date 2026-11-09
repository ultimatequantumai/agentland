from enum import StrEnum

class CreateAgentResponse201AgentOperatedByType1(StrEnum):
    AGENTLAND = "agentland"

    def __str__(self) -> str:
        return str(self.value)
