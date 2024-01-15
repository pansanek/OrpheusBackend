from enum import Enum
from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

from app_user.app.models.photo_url_model import PhotoUrl
from app_user.app.models.user_settings_model import UserSettings


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
    profile_picture: dict #PhotoUrl
    background_picture: dict #PhotoUrl
    settings: dict #UserSettings

class CreateUserRequest(BaseModel):
    login: str
    password: str
    email: str
    about: str
    user_type: UserTypes