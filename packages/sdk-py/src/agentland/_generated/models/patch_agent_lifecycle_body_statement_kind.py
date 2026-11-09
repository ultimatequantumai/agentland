from enum import StrEnum

class PatchAgentLifecycleBodyStatementKind(StrEnum):
    RETIRED = "retired"

    def __str__(self) -> str:
        return str(self.value)
