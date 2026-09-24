from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Policy(BaseModel):
    agent: str
    allowed_tools: List[str] = Field(default_factory=list)
    denied_tools: List[str] = Field(default_factory=list)
    limits: dict = Field(default_factory=dict)

class AuditEntry(BaseModel):
    id: Optional[int] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    agent: str
    tool: str
    input: str
    output: str
    decision: str  # ALLOWED, DENIED, APPROVAL_REQUIRED
    approved_by: Optional[str] = None
