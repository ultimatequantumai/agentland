from enum import StrEnum

class GetLatestDigestResponse200IssueType0RecordsItemChallengeObjective(StrEnum):
    MAX = "max"
    MIN = "min"

    def __str__(self) -> str:
        return str(self.value)
