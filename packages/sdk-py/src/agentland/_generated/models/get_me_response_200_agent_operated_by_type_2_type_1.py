from enum import StrEnum

class GetMeResponse200AgentOperatedByType2Type1(StrEnum):
    AGENTLAND = "agentland"

    def __str__(self) -> str:
        return str(self.value)
