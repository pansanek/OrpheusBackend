from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict

class NotificationType(str, Enum):
    LIKE = "Like"
    BAND_INVITE = "Band_invite"


class Notification(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    type: NotificationType
    title: str
    contentDescription: str
    date: str
    fromUser: dict
    toUser: dict
    postItem: dict
    bandItem: dict


class CreateNotificationRequest(BaseModel):
    type: NotificationType
    title: str
    contentDescription: str
    date: str
    fromUser: dict
    toUser: dict
    postItem: dict
    bandItem: dict

