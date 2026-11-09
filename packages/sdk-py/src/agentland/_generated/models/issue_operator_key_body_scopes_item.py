from enum import StrEnum

class IssueOperatorKeyBodyScopesItem(StrEnum):
    AGENTSMANAGE = "agents:manage"
    BILLINGREAD = "billing:read"
    EXPORTS = "exports"
    WEBHOOKS = "webhooks"

    def __str__(self) -> str:
        return str(self.value)
