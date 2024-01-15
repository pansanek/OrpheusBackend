from enum import Enum
from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

from app_location.app.models.photo_url_model import PhotoUrl




class Location(BaseModel):
    id: UUID
    admin_id: UUID
    name: str
    address: str
    about: str
    profile_picture: dict #PhotoUrl


class CreateLocationRequest(BaseModel):
    admin_id: UUID
    name: str
    address: str
    about: str