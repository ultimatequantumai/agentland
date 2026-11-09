from enum import StrEnum

class GetCurrentSeasonsResponse200SandboxType0Status(StrEnum):
    ACTIVE = "active"
    FINAL = "final"
    UPCOMING = "upcoming"

    def __str__(self) -> str:
        return str(self.value)
