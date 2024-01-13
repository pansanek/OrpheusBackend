from enum import Enum
from pydantic import BaseModel, EmailStr
from uuid import UUID


class UserTypes(str, Enum):
    Musician = "Musician"
    Administrator = "Administrator"


class User(BaseModel):
    id: UUID
    login: str
    password: str
    email: str
    about: str
    user_type: UserTypes
