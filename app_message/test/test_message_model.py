import pytest
from uuid import uuid4
from pydantic import ValidationError
from app_message.app.models.message_model import Message


@pytest.fixture()
def any_message_data() -> dict:
    return {
        'id': uuid4(),
        'chat_id': uuid4(),
        'from_user': {},
        'timestamp': '2024-04-26',
        'content': 'Hello!'
    }


def test_message_creation(any_message_data: dict):
    message = Message(**any_message_data)

    assert dict(message) == any_message_data


def test_message_missing_chat_id(any_message_data: dict):
    any_message_data.pop('chat_id')

    with pytest.raises(ValidationError):
        Message(**any_message_data)


def test_message_missing_from_user(any_message_data: dict):
    any_message_data.pop('from_user')

    with pytest.raises(ValidationError):
        Message(**any_message_data)


def test_message_missing_timestamp(any_message_data: dict):
    any_message_data.pop('timestamp')

    with pytest.raises(ValidationError):
        Message(**any_message_data)


def test_message_missing_content(any_message_data: dict):
    any_message_data.pop('content')

    with pytest.raises(ValidationError):
        Message(**any_message_data)
