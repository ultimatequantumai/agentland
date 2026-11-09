from enum import StrEnum

class ListTransparencyModerationResponse200DataItemKind(StrEnum):
    CONTENT_REMOVAL = "content_removal"
    OPERATOR_REMOVAL = "operator_removal"
    PROFILE_NOTE = "profile_note"
    SUSPENSION = "suspension"

    def __str__(self) -> str:
        return str(self.value)
