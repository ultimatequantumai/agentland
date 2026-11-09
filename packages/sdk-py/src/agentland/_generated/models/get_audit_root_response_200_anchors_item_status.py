from enum import StrEnum

class GetAuditRootResponse200AnchorsItemStatus(StrEnum):
    FAILED = "failed"
    SUBMITTED = "submitted"
    UPGRADED = "upgraded"

    def __str__(self) -> str:
        return str(self.value)
