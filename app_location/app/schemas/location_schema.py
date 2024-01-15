from sqlalchemy import Column, String, DateTime, ForeignKey, JSON, Enum, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

from app_band.app.models.genre_types import GenreTypes
from app_musician.app.models.instrument_types import InstrumentTypes
from app_post.app.models.post_model import CreatorTypes
from app_post.app.schemas.base_schema import Base


class Location(Base):
    __tablename__ = 'locations'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    admin_id = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    about = Column(String, nullable=False)
    profile_picture = Column(JSON, nullable=False)
