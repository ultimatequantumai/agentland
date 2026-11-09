from enum import StrEnum

class ListAuditRootsResponse200DataItemAnchorStatus(StrEnum):
    CONFIRMED = "confirmed"
    SUBMITTED = "submitted"
    UNANCHORED = "unanchored"

    def __str__(self) -> str:
        return str(self.value)
