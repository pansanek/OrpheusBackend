from sqlalchemy import Column, String, DateTime, JSON, Enum, Integer
from sqlalchemy.dialects.postgresql import UUID

from app_post.app.models.post_model import CreatorTypes
from app_post.app.schemas.base_schema import Base


class Post(Base):
    __tablename__ = 'posts'

    post_id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    creator_id = Column(UUID(as_uuid=True), nullable=False)
    creator_name = Column(String, nullable=False)
    creator_picture = Column(JSON, nullable=False)
    text = Column(String, nullable=False)
    date = Column(JSON, nullable=False)
    likes = Column(JSON, nullable=False)
    comments = Column(JSON, nullable=False)
    attachment = Column(JSON, nullable=False)
    creator_type = Column(Enum(CreatorTypes), nullable=False)
