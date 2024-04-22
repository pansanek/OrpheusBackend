from sqlalchemy import Column, String, JSON
from sqlalchemy.dialects.postgresql import UUID

from app_location.app.schemas.base_schema import Base


class Location(Base):
    __tablename__ = 'locations'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    admin = Column(JSON, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    about = Column(String, nullable=False)
    profile_picture = Column(JSON, nullable=False)
