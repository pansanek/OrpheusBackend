from uuid import UUID

from pydantic import BaseModel


class Administrator(BaseModel):
    id: UUID
    user_id: str
    location_id: UUID


class CreateAdministratorRequest(BaseModel):
    user_id: str
    location_id: UUID
