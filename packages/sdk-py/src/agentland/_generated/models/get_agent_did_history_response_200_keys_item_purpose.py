from enum import StrEnum

class GetAgentDidHistoryResponse200KeysItemPurpose(StrEnum):
    ENCRYPTION = "encryption"
    SIGNING = "signing"

    def __str__(self) -> str:
        return str(self.value)
