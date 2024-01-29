from sqlalchemy import Column, JSON
from sqlalchemy.dialects.postgresql import UUID

from app.schemas.base_schema import Base


class Administrator(Base):
    __tablename__ = 'administrator'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    user = Column(JSON, nullable=False)
    location_id = Column(UUID(as_uuid=True), nullable=False)
