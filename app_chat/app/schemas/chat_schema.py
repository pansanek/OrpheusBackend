from sqlalchemy import Column, String, JSON, Enum
from sqlalchemy.dialects.postgresql import UUID

from app_chat.app.schemas.base_schema import Base


class Chat(Base):
    __tablename__ = 'chats'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    users = Column(JSON, nullable=False)
    last_message = Column(String, nullable=False)
