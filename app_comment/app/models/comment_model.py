from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel



class Comment(BaseModel):
    id: UUID
    post_id: UUID
    user: dict
    text: str
    timestamp: str


class CreateCommentRequest(BaseModel):
    user: dict
    post_id: UUID
    text: str
    timestamp: str
