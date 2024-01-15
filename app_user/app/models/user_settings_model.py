from enum import Enum
from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

from app_user.app.models.photo_url_model import PhotoUrl


class UserSettings(BaseModel):
    can_receive_messages_for_new_chats: bool
    can_receive_band_invitations: bool


