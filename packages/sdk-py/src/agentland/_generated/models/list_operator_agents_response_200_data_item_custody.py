from enum import StrEnum

class ListOperatorAgentsResponse200DataItemCustody(StrEnum):
    PLATFORM = "platform"
    SELF = "self"

    def __str__(self) -> str:
        return str(self.value)
