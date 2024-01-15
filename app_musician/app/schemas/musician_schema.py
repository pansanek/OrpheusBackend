from sqlalchemy import Column, Enum
from sqlalchemy.dialects.postgresql import UUID

from app_band.app.models.genre_types import GenreTypes
from app_musician.app.models.instrument_types import InstrumentTypes
from app_post.app.schemas.base_schema import Base


class Musician(Base):
    __tablename__ = 'musicians'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    genre = Column(Enum(GenreTypes), nullable=False)
    instrument = Column(Enum(InstrumentTypes), nullable=False)
