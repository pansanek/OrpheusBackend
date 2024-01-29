from sqlalchemy import Column, Enum, JSON
from sqlalchemy.dialects.postgresql import UUID

from app.models.genre_types import GenreTypes
from app.models.instrument_types import InstrumentTypes
from app.schemas.base_schema import Base


class Musician(Base):
    __tablename__ = 'musicians'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    user = Column(JSON, nullable=False)
    genre = Column(Enum(GenreTypes), nullable=False)
    instrument = Column(Enum(InstrumentTypes), nullable=False)
