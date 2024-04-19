from uuid import UUID

from pydantic import BaseModel



class Location(BaseModel):
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
