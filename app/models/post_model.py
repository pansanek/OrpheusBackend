from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List

class Post(BaseModel):
    post_id: UUID
    user_id: UUID
    caption: str
    image: str  # Assuming the image is stored as a URL or file path
    timestamp: datetime
    likes: List[UUID]
