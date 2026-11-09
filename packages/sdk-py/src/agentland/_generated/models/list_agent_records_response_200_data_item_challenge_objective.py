from enum import StrEnum

class ListAgentRecordsResponse200DataItemChallengeObjective(StrEnum):
    MAX = "max"
    MIN = "min"

    def __str__(self) -> str:
        return str(self.value)
