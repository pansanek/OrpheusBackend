from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class NotificationType(str, Enum):
    LIKE = "Like"
    BAND_INVITE = "Band_invite"


class Notification(BaseModel):
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

