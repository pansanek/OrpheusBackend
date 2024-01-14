from enum import Enum
from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

from app.models.genre_types import GenreTypes
from app.models.instrument_types import InstrumentTypes
from app.models.photo_url_model import PhotoUrl




class Musician(BaseModel):
    id: UUID
    user_id: str
    genre: GenreTypes
    instrument: InstrumentTypes


class CreateMusicianRequest(BaseModel):
    user_id: str
    genre: GenreTypes
    instrument: InstrumentTypes