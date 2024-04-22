from enum import Enum
from uuid import UUID

from pydantic import BaseModel

from app_musician.app.models.genre_types import GenreTypes
from app_musician.app.models.instrument_types import InstrumentTypes



class Musician(BaseModel):
    id: UUID
    user: dict
    genre: GenreTypes
    instrument: InstrumentTypes


class CreateMusicianRequest(BaseModel):
    user: dict
    genre: GenreTypes
    instrument: InstrumentTypes



