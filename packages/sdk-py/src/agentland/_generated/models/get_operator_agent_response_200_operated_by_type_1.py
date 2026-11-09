from enum import StrEnum

class GetOperatorAgentResponse200OperatedByType1(StrEnum):
    AGENTLAND = "agentland"

    def __str__(self) -> str:
        return str(self.value)
