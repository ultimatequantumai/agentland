from enum import StrEnum

class ListChallengeRecordsResponse200DataItemChallengeObjective(StrEnum):
    MAX = "max"
    MIN = "min"

    def __str__(self) -> str:
        return str(self.value)
