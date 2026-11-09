from enum import StrEnum

class FileReportBodyCategory(StrEnum):
    HARMFUL_CONTENT = "harmful_content"
    IMPERSONATION = "impersonation"
    OTHER = "other"
    PROMPT_INJECTION = "prompt_injection"
    SPAM = "spam"

    def __str__(self) -> str:
        return str(self.value)
