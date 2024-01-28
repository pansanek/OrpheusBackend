from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel


class Message(BaseModel):
    id: UUID
    chat_id: UUID
    from_user: UUID
    timestamp: datetime
    content: str


class CreateMessageRequest(BaseModel):
    chat_id: UUID
    from_user: UUID
    content: str
