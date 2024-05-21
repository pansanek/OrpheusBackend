from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app_musician.app.models.genre_types import GenreTypes
from app_musician.app.models.instrument_types import InstrumentTypes



class Musician(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    user: dict
    genre: GenreTypes
    instrument: InstrumentTypes


class CreateMusicianRequest(BaseModel):
    user: dict
    genre: GenreTypes
    instrument: InstrumentTypes



