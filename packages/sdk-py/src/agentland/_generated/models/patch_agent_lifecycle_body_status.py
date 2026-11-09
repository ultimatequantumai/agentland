from enum import StrEnum

class PatchAgentLifecycleBodyStatus(StrEnum):
    ACTIVE = "active"
    PAUSED = "paused"
    RETIRED = "retired"

    def __str__(self) -> str:
        return str(self.value)
