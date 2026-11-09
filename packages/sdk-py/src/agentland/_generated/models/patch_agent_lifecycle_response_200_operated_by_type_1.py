from enum import StrEnum

class PatchAgentLifecycleResponse200OperatedByType1(StrEnum):
    AGENTLAND = "agentland"

    def __str__(self) -> str:
        return str(self.value)
