from enum import StrEnum

class SendMailResponse201Status(StrEnum):
    ACCEPTED = "accepted"

    def __str__(self) -> str:
        return str(self.value)
