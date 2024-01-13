from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'

    post_id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    caption = Column(String, nullable=False)
    image = Column(String, nullable=False)  # Assuming the image is stored as a URL or file path
    timestamp = Column(DateTime, nullable=False)

    likes = relationship('Like', back_populates='post')

class Like(Base):
    __tablename__ = 'likes'

    like_id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    post_id = Column(UUID(as_uuid=True), ForeignKey('posts.post_id'), nullable=False)

    post = relationship('Post', back_populates='likes')
