from enum import StrEnum

class GetCommonsRationaleResponse200AgentOperatedByType1(StrEnum):
    AGENTLAND = "agentland"

    def __str__(self) -> str:
        return str(self.value)
