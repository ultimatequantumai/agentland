from enum import StrEnum

class PatchAgentLifecycleResponse200Status(StrEnum):
    ACTIVE = "active"
    PAUSED = "paused"
    RETIRED = "retired"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
