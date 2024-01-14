from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List

from app.models.attachment_model import Attachment
from app.models.comment_model import Comment


class Post(BaseModel):
    post_id: UUID
    user_id: UUID
    caption: str
    image: str
    timestamp: datetime
    likes: List[UUID]
    comments: List[Comment]
    attachment: List[Attachment]


class CreatePostRequest(BaseModel):
    user_id: UUID
    caption: str
    image: str