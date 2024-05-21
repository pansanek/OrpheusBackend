from sqlalchemy import Column, String, Enum, JSON
from sqlalchemy.dialects.postgresql import UUID

from app_notification.app.models.notification_model import NotificationType
from app_notification.app.models.user_model import UserTypes
from app_notification.app.schemas.base_schema import Base


class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False)
    type = Column(Enum(NotificationType), index=True, unique=True, nullable=False)
    title = Column(String, index=True, unique=True, nullable=False)
    content_description = Column(String, nullable=False)
    date = Column(String, index=True, unique=True, nullable=False)
    from_user = Column(JSON, nullable=False)
    to_user = Column(JSON, nullable=False)
    post_item = Column(JSON, nullable=True)
    band_item = Column(JSON, nullable=True)
