from enum import Enum
from typing import List

from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

from app.models.photo_url_model import PhotoUrl


class UserTypes(str, Enum):
    Musician = "Musician"
    Administrator = "Administrator"


class Band(BaseModel):
    id: UUID
    name: str
    members: List[UUID]

class CreateBandRequest(BaseModel):
    name: str