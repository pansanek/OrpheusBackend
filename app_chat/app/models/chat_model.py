from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict




class Chat(BaseModel):
    model_config = ConfigDict(from_attributes=True)
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
