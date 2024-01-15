from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class Comment(BaseModel):
    id: UUID
    post_id: UUID
    user_id: UUID
    text: str
    timestamp: datetime


class CreateCommentRequest(BaseModel):
    user_id: UUID
    post_id: UUID
    text: str
