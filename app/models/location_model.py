from enum import Enum
from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

from app.models.genre_types import GenreTypes
from app.models.instrument_types import InstrumentTypes
from app.models.photo_url_model import PhotoUrl




class Location(BaseModel):
    id: UUID
    admin_id: str
    name: str
    address: str
    about: str
    profile_picture: PhotoUrl


class CreateLocationRequest(BaseModel):
    admin_id: str