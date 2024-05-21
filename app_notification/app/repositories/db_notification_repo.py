import traceback
from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from app_notification.app.schemas.base_schema import get_db
from app_notification.app.models.notification_model import Notification
from app_notification.app.schemas.notification_schema import Notification as DBNotification


class NotificationRepo:
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, notification: DBNotification) -> Notification:
        result = Notification.from_orm(notification)
        return result

    def _map_to_schema(self, notification: Notification) -> DBNotification:
        data = dict(notification)
        result = DBNotification(**data)
        return result

    def create_notification(self, notification: Notification) -> Notification:
        try:
            db_notification = self._map_to_schema(notification)
            self.db.add(db_notification)
            self.db.commit()
            return self._map_to_model(db_notification)
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
            raise e

    def get_all_notifications(self) -> List[Notification]:
        notifications = []
        for u in self.db.query(DBNotification).all():
            notifications.append(self._map_to_model(u))
        return notifications

    def get_notification_by_id(self, notification_id: UUID) -> Notification:
        notification = self.db \
            .query(DBNotification) \
            .filter(DBNotification.id == notification_id) \
            .first()

        if notification is None:
            raise KeyError(f"Notification with id {notification_id} not found.")
        return self._map_to_model(notification)

    def update_notification(self, notification: Notification) -> Notification:
        try:
            db_notification = self.db.query(DBNotification).filter(DBNotification.id ==notification.id).first()
            db_notification = notification
            self.db.commit()
            return self.db.query(DBNotification).filter(DBNotification.id ==notification.id).first()
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
            raise e