from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel

from app_band.app.models.genre_types import GenreTypes


class Band(BaseModel):
    id: UUID
    name: str
    members: List[dict]
    genre: GenreTypes
    photo: dict  # PhotoUrl


class CreateBandRequest(BaseModel):
    name: str
    member: dict
    genre: GenreTypes
