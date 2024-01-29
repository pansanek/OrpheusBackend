from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel

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


class Comment(BaseModel):
    id: UUID
    post_id: UUID
    user: User
    text: str
    timestamp: datetime


class CreateCommentRequest(BaseModel):
    user: User
    post_id: UUID
    text: str
