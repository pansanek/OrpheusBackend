from uuid import UUID

from pydantic import BaseModel


class Location(BaseModel):
    id: UUID
    admin_id: UUID
    name: str
    address: str
    about: str
    profile_picture: dict  # PhotoUrl


class CreateLocationRequest(BaseModel):
    admin_id: UUID
    name: str
    address: str
    about: str
