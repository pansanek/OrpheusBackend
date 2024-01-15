from enum import Enum

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List

from app_attachment.app.models.attachment_model import Attachment
from app_post.app.models.photo_url_model import PhotoUrl


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
