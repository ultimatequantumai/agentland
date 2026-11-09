from enum import StrEnum

class GetLatestDigestResponse200IssueType0RationalesItemRationalePublish(StrEnum):
    CLOSE = "close"
    RESOLVE = "resolve"

    def __str__(self) -> str:
        return str(self.value)
