from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID

from app_post.app.schemas.base_schema import Base


class Administrator(Base):
    __tablename__ = 'administrator'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    location_id = Column(UUID(as_uuid=True), nullable=False)
