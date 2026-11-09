from enum import StrEnum

class GetOperatorAgentResponse200PendingTransferType0Status(StrEnum):
    ACCEPTED = "accepted"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
