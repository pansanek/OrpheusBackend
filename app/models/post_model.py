from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List

class Post(BaseModel):
    post_id: UUID
    user_id: UUID
    caption: str
    image: str
    timestamp: datetime
    likes: List[UUID]


class CreatePostRequest(BaseModel):
    user_id: UUID
    caption: str
    image: str