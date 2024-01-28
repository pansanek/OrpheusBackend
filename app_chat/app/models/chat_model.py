from typing import List
from uuid import UUID

from pydantic import BaseModel


class Chat(BaseModel):
    id: UUID
    users: List[dict]
    last_message: str


class CreateChatRequest(BaseModel):
    users: List[dict]
