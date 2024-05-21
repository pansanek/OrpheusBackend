from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app_band.app.models.genre_types import GenreTypes


class Band(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str
    members: List[dict]
    genre: GenreTypes
    photo: dict  # PhotoUrl


class CreateBandRequest(BaseModel):
    name: str
    members: List[dict]
    photo: dict
    genre: GenreTypes
