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

class Chat(BaseModel):
    id: UUID
    users: List[dict]
    last_message: str


class CreateChatRequest(BaseModel):
    creator: User
    second_user: User
