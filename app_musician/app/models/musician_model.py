from enum import Enum
from uuid import UUID

from pydantic import BaseModel

from app.models.genre_types import GenreTypes
from app.models.instrument_types import InstrumentTypes

class UserTypes(str, Enum):
    MUSICIAN = "Musician"
    ADMINISTRATOR = "Administrator"


class User(BaseModel):
    id: UUID
    login: str
    password: str
    email: str
    about: str
    user_type: UserTypes
    profile_picture: dict  # PhotoUrl
    background_picture: dict  # PhotoUrl
    settings: dict  # UserSettings

class Musician(BaseModel):
    id: UUID
    user: User
    genre: GenreTypes
    instrument: InstrumentTypes


class CreateMusicianRequest(BaseModel):
    user_id: UUID
    genre: GenreTypes
    instrument: InstrumentTypes



