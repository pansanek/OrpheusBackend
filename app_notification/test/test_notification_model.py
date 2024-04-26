import pytest
from uuid import uuid4
from pydantic import ValidationError
from app_notification.app.models.notification_model import Notification, NotificationType


@pytest.fixture()
def any_notification_data() -> dict:
    return {
        'id': uuid4(),
        'type': NotificationType.LIKE,
        'title': 'New Like',
        'contentDescription': 'You have received a new like on your post',
        'date': '2024-04-26',
        'fromUser': {},
        'toUser': {},
        'postItem': {},
        'bandItem': {}
    }


def test_notification_creation(any_notification_data: dict):
    notification = Notification(**any_notification_data)

    assert dict(notification) == any_notification_data


def test_notification_missing_type(any_notification_data: dict):
    any_notification_data.pop('type')

    with pytest.raises(ValidationError):
        Notification(**any_notification_data)


def test_notification_missing_title(any_notification_data: dict):
    any_notification_data.pop('title')

    with pytest.raises(ValidationError):
        Notification(**any_notification_data)


def test_notification_invalid_type(any_notification_data: dict):
    any_notification_data['type'] = 'invalid_notification_type'

    with pytest.raises(ValidationError):
        Notification(**any_notification_data)
