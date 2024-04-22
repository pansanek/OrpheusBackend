from typing import List
from uuid import UUID, uuid4

from fastapi import Depends

from app_notification.app.models.notification_model import Notification
from app_notification.app.repositories.notification_repo import NotificationRepo

from app_notification.app.models.notification_model import NotificationType


class NotificationService:
    notification_repo: NotificationRepo

    def __init__(self, notification_repo: NotificationRepo = Depends(NotificationRepo)) -> None:
        self.notification_repo = notification_repo

    def get_all_notifications(self) -> List[Notification]:
        return self.notification_repo.get_notifications()

    def get_notification_by_id(self, notification_id: UUID) -> Notification:
        return self.notification_repo.get_notification_by_id(notification_id)

    def create_notification(self, type=NotificationType,
                            title=str,
                            contentDescription=str,
                            date=str,
                            fromUser=dict,
                            toUser=dict,
                            postItem=dict,
                            bandItem=dict, ) -> Notification:
        notification = Notification(id=uuid4(), type=type,
                                    title=title,
                                    contentDescription=contentDescription,
                                    date=date,
                                    fromUser=fromUser,
                                    toUser=toUser,
                                    postItem=postItem,
                                    bandItem=bandItem)
        return self.notification_repo.create_notification(notification)

    def update_notification(self, notification_id: UUID, type=NotificationType,
                            title=str,
                            contentDescription=str,
                            date=str,
                            fromUser=dict,
                            toUser=dict,
                            postItem=dict,
                            bandItem=dict, ) -> Notification:
        notification = Notification(id=notification_id, type=type,
                                    title=title,
                                    contentDescription=contentDescription,
                                    date=date,
                                    fromUser=fromUser,
                                    toUser=toUser,
                                    postItem=postItem,
                                    bandItem=bandItem)
        return self.notification_repo.update_notification(notification)
