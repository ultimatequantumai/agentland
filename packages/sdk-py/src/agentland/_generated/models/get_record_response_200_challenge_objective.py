from enum import StrEnum

class GetRecordResponse200ChallengeObjective(StrEnum):
    MAX = "max"
    MIN = "min"

    def __str__(self) -> str:
        return str(self.value)
