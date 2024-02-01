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


class Message(BaseModel):
    id: UUID
    chat_id: UUID
    from_user: User
    timestamp: datetime
    content: str


class CreateMessageRequest(BaseModel):
    chat_id: UUID
    from_user: UUID
    content: str
