from enum import StrEnum

class CreateWebhookResponse201Status(StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)
