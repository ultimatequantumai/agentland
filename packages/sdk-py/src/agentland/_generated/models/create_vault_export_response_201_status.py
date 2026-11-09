from enum import StrEnum

class CreateVaultExportResponse201Status(StrEnum):
    BUILDING = "building"
    FAILED = "failed"
    PENDING = "pending"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
