from enum import Enum
from uuid import UUID

from pydantic import BaseModel

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
    profile_picture: dict  # PhotoUrl
    background_picture: dict  # PhotoUrl
    settings: dict  # UserSettings

class Administrator(BaseModel):
    id: UUID
    user: User
    location_id: UUID


class CreateAdministratorRequest(BaseModel):
    user_id: str
    location_id: UUID
