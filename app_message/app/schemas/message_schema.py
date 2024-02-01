from sqlalchemy import Column, String, DateTime, JSON, Enum, Integer
from sqlalchemy.dialects.postgresql import UUID

from app.schemas.base_schema import Base


class Message(Base):
    __tablename__ = 'messages'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    chat_id = Column(UUID(as_uuid=True), nullable=False)
    from_user = Column(JSON, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    content = Column(String, nullable=False)
