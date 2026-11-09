from enum import StrEnum

class GetAuditRootResponse200Format(StrEnum):
    AGENTLAND_AUDIT_ROOT1 = "agentland-audit-root/1"

    def __str__(self) -> str:
        return str(self.value)
