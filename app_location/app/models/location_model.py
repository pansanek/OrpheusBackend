from uuid import UUID

from pydantic import BaseModel

from app.models.administrator_model import Administrator


class Location(BaseModel):
    id: UUID
    admin: Administrator
    name: str
    address: str
    about: str
    profile_picture: dict  # PhotoUrl


class CreateLocationRequest(BaseModel):
    admin: Administrator
    name: str
    address: str
    about: str
