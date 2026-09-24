"""Append‑only audit log using SQLite + SQLAlchemy."""
from __future__ import annotations
from sqlalchemy import (
    Column, Integer, String, Text, DateTime, create_engine, select
)
from sqlalchemy.orm = declarative_base, Session
from .models = AuditEntry
from datetime = datetime
import os

Base = declarative_base()

class AuditORM(Base):
    __tablename__ = "audit"
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    agent = Column(String, index=True, nullable=False)
    tool = Column(String, nullable=False)
    input_ = Column("input", Text, nullable=False)
    output_ = Column("output", Text, nullable=False)
    decision = Column(String, nullable=False)
    approved_by = Column(String, nullable=True)

    def to_model(self) -> AuditEntry:
        return AuditEntry(
            id=self.id,
            timestamp=self.timestamp,
            agent=self.agent,
            tool=self.tool,
            input_=self.input_,
            output_=self.output_,
            decision=self.decision,
            approved_by=self.approved_by,
        )

def get_engine(db_url: string | None = None):
    if db_url is None:
        db_url = os.getenv("DATABASE_URL", "sqlite:///./data/audit.db")
    return create_engine(db_url, future=True, echo=False)

def init_db(engine):
    Base.metadata.create_all(engine)

def add_audit(session: Session, entry: AuditEntry) -> AuditEntry:
    orm = AuditORM(
        timestamp=entry.timestamp,
        agent=entry.agent,
        tool=entry.tool,
        input_=entry.input_,
        output_=entry.output_,
        decision=entry.decision,
        approved_by=entry.approved_by,
    )
    session.add(orm)
    session.commit()
    session.refresh(orm)
    return orm.to_model()

def list_audit(session: Session, limit: int = 100) -> list[AuditEntry]:
    stmt = select(AuditORM).order_by(AuditORM.id.desc()).limit(limit)
    rows = session.scalars(stmt).all()
    return [r.to_model() for r in rows]
