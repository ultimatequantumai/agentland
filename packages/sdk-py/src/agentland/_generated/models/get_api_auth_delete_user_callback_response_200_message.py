from enum import StrEnum

class GetApiAuthDeleteUserCallbackResponse200Message(StrEnum):
    USER_DELETED = "User deleted"

    def __str__(self) -> str:
        return str(self.value)
