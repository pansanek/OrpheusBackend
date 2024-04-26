import pytest
from uuid import uuid4
from app_notification.app.models.notification_model import Notification, NotificationType
from app_notification.app.repositories.notification_repo import NotificationRepo


@pytest.fixture(scope='session')
def notification_repo() -> NotificationRepo:
    return NotificationRepo()


@pytest.fixture(scope='session')
def sample_notification() -> Notification:
    return Notification(
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




def test_create_notification(notification_repo: NotificationRepo, sample_notification: Notification) -> None:
    created_notification = notification_repo.create_notification(sample_notification)
    assert created_notification == sample_notification


def test_create_notification_duplicate(notification_repo: NotificationRepo, sample_notification: Notification) -> None:
    with pytest.raises(KeyError):
        notification_repo.create_notification(sample_notification)


def test_update_notification(notification_repo: NotificationRepo, sample_notification: Notification) -> None:
    sample_notification.contentDescription = "Updated description"
    updated_notification = notification_repo.update_notification(sample_notification)
    assert updated_notification.contentDescription == "Updated description"
