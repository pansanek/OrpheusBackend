from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel

from app_band.app.models.genre_types import GenreTypes

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

class Band(BaseModel):
    id: UUID
    name: str
    members: List[dict]
    genre: GenreTypes
    photo: dict  # PhotoUrl


class CreateBandRequest(BaseModel):
    name: str
    member: User
    genre: GenreTypes
