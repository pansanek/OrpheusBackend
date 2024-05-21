from uuid import UUID

from pydantic import BaseModel, ConfigDict
class PhotoUrl(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    url: str


class CreatePhotoUrlRequest(BaseModel):
    url: str
