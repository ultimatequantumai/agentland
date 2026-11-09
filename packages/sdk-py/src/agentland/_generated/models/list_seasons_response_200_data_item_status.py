from enum import StrEnum

class ListSeasonsResponse200DataItemStatus(StrEnum):
    ACTIVE = "active"
    FINAL = "final"
    UPCOMING = "upcoming"

    def __str__(self) -> str:
        return str(self.value)
