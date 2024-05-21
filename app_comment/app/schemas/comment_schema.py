from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID

from app_comment.app.schemas.base_schema import Base


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    post_id = Column(UUID(as_uuid=True), nullable=False)
    user = Column(JSON, nullable=False)
    text = Column(String, nullable=False)
    timestamp = Column(String, nullable=False)
