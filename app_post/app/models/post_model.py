from enum import Enum

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List

from app_attachment.app.models.attachment_model import Attachment
from app_comment.app.models.comment_model import Comment

class CreatorTypes(str, Enum):
    USER = "User"
    BAND = "Band"
    LOCATION = "Location"

class Post(BaseModel):
    post_id: UUID
    creator_id: UUID
    caption: str
    image: str
    timestamp: datetime
    likes: List[UUID]
    views: int
    comments: List[Comment]
    attachment: List[Attachment]
    creator_type: CreatorTypes



class CreatePostRequest(BaseModel):
    user_id: UUID
    caption: str
    image: str
    creator_type: CreatorTypes