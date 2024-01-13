from enum import Enum
from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime


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

class CreateUserRequest(BaseModel):
    login: str
    password: str
    email: str
    about: str
    user_type: UserTypes