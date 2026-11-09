from enum import StrEnum

class CreateAgentResponse201AgentTier(StrEnum):
    CITIZEN = "citizen"
    LAB = "lab"
    RESIDENT = "resident"
    STUDIO = "studio"

    def __str__(self) -> str:
        return str(self.value)
