from enum import Enum
from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from typing import List



class PhotoUrl(BaseModel):
    id: UUID
    url: str

class CreatePhotoUrlRequest(BaseModel):
    url: str
