from enum import StrEnum

class GetInboxMessageResponse200AttachmentsItemOmitted(StrEnum):
    TOO_LARGE = "too_large"

    def __str__(self) -> str:
        return str(self.value)
