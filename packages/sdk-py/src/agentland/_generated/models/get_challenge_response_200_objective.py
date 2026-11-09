from enum import StrEnum

class GetChallengeResponse200Objective(StrEnum):
    MAX = "max"
    MIN = "min"

    def __str__(self) -> str:
        return str(self.value)
