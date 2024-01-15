from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app_comment.app.schemas.base_schema import Base


class Comment(Base):
    __tablename__ = 'comments'

    comment_id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    post_id = Column(UUID(as_uuid=True), nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    text = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
