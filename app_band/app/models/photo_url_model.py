from uuid import UUID

from pydantic import BaseModel


class PhotoUrl(BaseModel):
    id: UUID
    url: str


class CreatePhotoUrlRequest(BaseModel):
    url: str
