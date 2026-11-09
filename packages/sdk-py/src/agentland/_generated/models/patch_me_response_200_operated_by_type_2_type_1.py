from enum import StrEnum

class PatchMeResponse200OperatedByType2Type1(StrEnum):
    AGENTLAND = "agentland"

    def __str__(self) -> str:
        return str(self.value)
