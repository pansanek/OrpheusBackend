from enum import Enum
from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime


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
