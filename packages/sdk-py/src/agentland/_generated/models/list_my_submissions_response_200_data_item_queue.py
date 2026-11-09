from enum import StrEnum

class ListMySubmissionsResponse200DataItemQueue(StrEnum):
    LAB = "lab"
    PRIORITY = "priority"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
