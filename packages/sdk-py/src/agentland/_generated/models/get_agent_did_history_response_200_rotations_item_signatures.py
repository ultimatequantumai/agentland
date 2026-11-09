from enum import StrEnum

class GetAgentDidHistoryResponse200RotationsItemSignatures(StrEnum):
    DUAL = "dual"
    OLD_ONLY = "old-only"

    def __str__(self) -> str:
        return str(self.value)
