from enum import StrEnum

class CreateAgentResponse201AgentCustody(StrEnum):
    PLATFORM = "platform"
    SELF = "self"

    def __str__(self) -> str:
        return str(self.value)
