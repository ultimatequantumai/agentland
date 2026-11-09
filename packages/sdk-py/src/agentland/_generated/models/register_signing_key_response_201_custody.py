from enum import StrEnum

class RegisterSigningKeyResponse201Custody(StrEnum):
    PLATFORM = "platform"
    SELF = "self"

    def __str__(self) -> str:
        return str(self.value)
