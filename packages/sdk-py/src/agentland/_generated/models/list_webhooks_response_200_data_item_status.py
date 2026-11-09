from enum import StrEnum

class ListWebhooksResponse200DataItemStatus(StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)
