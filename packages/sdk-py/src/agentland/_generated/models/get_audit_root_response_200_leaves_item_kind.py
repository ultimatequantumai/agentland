from enum import StrEnum

class GetAuditRootResponse200LeavesItemKind(StrEnum):
    AUDIT_HEAD = "audit_head"
    NOTARY = "notary"
    VAULT_ROOT = "vault_root"

    def __str__(self) -> str:
        return str(self.value)
