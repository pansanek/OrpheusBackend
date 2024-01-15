from enum import Enum
from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

from app_user.app.models.photo_url_model import PhotoUrl


class UserTypes(str, Enum):
    MUSICIAN = "Musician"
    ADMINISTRATOR = "Administrator"


class User(BaseModel):
    id: UUID
    login: str
    password: str
    email: str
    about: str
    user_type: UserTypes
    profile_picture: PhotoUrl
    background_picture: PhotoUrl

class CreateUserRequest(BaseModel):
    login: str
    password: str
    email: str
    about: str
    user_type: UserTypes