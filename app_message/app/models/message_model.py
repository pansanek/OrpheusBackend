from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict



class Message(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    chat_id: UUID
    from_user: dict
    timestamp: str
    content: str


class CreateMessageRequest(BaseModel):
    chat_id: UUID
    from_user: dict
    timestamp: str
    content: str
