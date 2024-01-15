from sqlalchemy import Column, String, JSON, Enum
from sqlalchemy.dialects.postgresql import UUID

from app_band.app.models.genre_types import GenreTypes
from app_post.app.schemas.base_schema import Base


class Band(Base):
    __tablename__ = 'bands'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    members = Column(JSON, nullable=False)
    genre = Column(Enum(GenreTypes), nullable=False)
    photo = Column(JSON, nullable=True)
