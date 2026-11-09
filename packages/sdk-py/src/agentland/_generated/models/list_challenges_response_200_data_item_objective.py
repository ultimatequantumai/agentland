from enum import StrEnum

class ListChallengesResponse200DataItemObjective(StrEnum):
    MAX = "max"
    MIN = "min"

    def __str__(self) -> str:
        return str(self.value)
