from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel




class Chat(BaseModel):
    id: UUID
    users: List[dict]
    last_message: str
    picture: dict
    name: str


class CreateChatRequest(BaseModel):
    users: List[dict]
    last_message: str
    picture: dict
    name: str
