from enum import StrEnum

class GetSeasonNotesResponse200RecordsItemChallengeObjective(StrEnum):
    MAX = "max"
    MIN = "min"

    def __str__(self) -> str:
        return str(self.value)
