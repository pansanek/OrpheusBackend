from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Location(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    admin: dict
    name: str
    address: str
    about: str
    profile_picture: dict  # PhotoUrl


class CreateLocationRequest(BaseModel):
    admin: dict
    name: str
    address: str
    about: str
    profile_picture: dict
