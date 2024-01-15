from enum import Enum
from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from typing import List

from app_attachment.app.models.photo_url_model import PhotoUrl


class Attachment(BaseModel):
    id: UUID
    user_id:UUID
    photo: List[PhotoUrl]

class CreateAttachmentRequest(BaseModel):
    photo: List[PhotoUrl]