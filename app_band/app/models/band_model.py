from enum import Enum
from typing import List

from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

from app_band.app.models.photo_url_model import PhotoUrl
from app_band.app.models.genre_types import GenreTypes


class Band(BaseModel):
    id: UUID
    name: str
    members: List[dict]
    genre: GenreTypes
    photo: dict  # PhotoUrl


class CreateBandRequest(BaseModel):
    name: str
    member: UUID
    genre: GenreTypes
