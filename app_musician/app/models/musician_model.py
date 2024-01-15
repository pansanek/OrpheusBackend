from uuid import UUID
from pydantic import BaseModel

from app_musician.app.models.genre_types import GenreTypes
from app_musician.app.models.instrument_types import InstrumentTypes
from uuid import UUID

from pydantic import BaseModel

from app_musician.app.models.genre_types import GenreTypes
from app_musician.app.models.instrument_types import InstrumentTypes


class Musician(BaseModel):
    id: UUID
    user_id: UUID
    genre: GenreTypes
    instrument: InstrumentTypes


class CreateMusicianRequest(BaseModel):
    user_id: UUID
    genre: GenreTypes
    instrument: InstrumentTypes
