from uuid import UUID

from pydantic import BaseModel

from app.models.administrator_model import User


class Location(BaseModel):
    id: UUID
    admin: User
    name: str
    address: str
    about: str
    profile_picture: dict  # PhotoUrl


class CreateLocationRequest(BaseModel):
    admin: User
    name: str
    address: str
    about: str
