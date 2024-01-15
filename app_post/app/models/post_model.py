from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel


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


class CreatePostRequest(BaseModel):
    creator_id: UUID
    caption: str
    creator_type: CreatorTypes
