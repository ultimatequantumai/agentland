from enum import StrEnum

class GetLatestDigestResponse200IssueType0RationalesItemRationaleOutcomeType(StrEnum):
    BINARY = "binary"
    MULTI = "multi"
    NUMERIC = "numeric"

    def __str__(self) -> str:
        return str(self.value)
