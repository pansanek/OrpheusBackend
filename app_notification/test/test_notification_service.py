import pytest
from uuid import uuid4
from app_notification.app.models.notification_model import Notification, NotificationType
from app_notification.app.services.notification_service import NotificationService
from unittest.mock import MagicMock


@pytest.fixture(scope='session')
def notification_service() -> NotificationService:
    return NotificationService(notification_repo=MagicMock())


def test_get_all_notifications(notification_service: NotificationService) -> None:
    notification_service.notification_repo.get_notifications.return_value = [
        Notification(
            id=uuid4(),
            type=NotificationType.LIKE,
            bandItem={},
            contentDescription="Someone liked your post",
            title="New Like",
            fromUser={},
            toUser={},
            date="2024-04-26",
            postItem={}
        )
    ]

    notifications = notification_service.get_all_notifications()
    assert len(notifications) == 1
    assert isinstance(notifications[0], Notification)


def test_create_notification(notification_service: NotificationService) -> None:
    notification_data = {
        "type": NotificationType.LIKE,
        "title": "New Like",
        "contentDescription": "Someone liked your post",
        "date": "2024-04-26",
        "fromUser": {},
        "toUser": {},
        "postItem": {},
        "bandItem": {}
    }

    notification_service.create_notification(**notification_data)

    notification_service.notification_repo.create_notification.assert_called_once()


def test_update_notification(notification_service: NotificationService) -> None:
    notification_id = uuid4()
    notification_data = {
        "notification_id": notification_id,
        "type": NotificationType.LIKE,
        "title": "New Like",
        "contentDescription": "Someone liked your post",
        "date": "2024-04-26",
        "fromUser": {},
        "toUser": {},
        "postItem": {},
        "bandItem": {}
    }

    notification_service.update_notification(**notification_data)

    notification_service.notification_repo.update_notification.assert_called_once_with(
        Notification(id=notification_id, **notification_data)
    )
