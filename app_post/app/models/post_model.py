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
    creatorId: UUID
    creatorName: str
    creatorPicture: dict
    text: str
    date: str
    likes: List[dict]
    comments: List[dict]
    attachment:dict
    creator_type: CreatorTypes




class CreatePostRequest(BaseModel):
    creatorId: UUID
    creatorName: str
    creatorPicture: dict
    text: str
    date: str
    likes: List[dict]
    comments: List[dict]
    attachment: dict
    creator_type: CreatorTypes
