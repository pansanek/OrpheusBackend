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

class CreatorTypes(str, Enum):
    USER = "User"
    BAND = "Band"
    LOCATION = "Location"


class Post(BaseModel):
    post_id: UUID
    creator_id: UUID
    caption: str
    timestamp: datetime
    likes: List[dict]
    views: int
    comments: List[dict]
    attachment: List[dict]
    creator_type: CreatorTypes

class Comment(BaseModel):
    id: UUID
    post: Post
    user: User
    text: str
    timestamp: datetime


class CreateCommentRequest(BaseModel):
    user: User
    post: Post
    text: str
