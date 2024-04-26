import pytest
from uuid import uuid4
from app_chat.app.models.chat_model import Chat
from pydantic import ValidationError


@pytest.fixture()
def any_chat_data() -> dict:
    return {
        'id': uuid4(),
        'users': [{}],
        'last_message': 'Last message',
        'picture': {},
        'name': 'Chat name'
    }


def test_chat_creation(any_chat_data: dict):
    chat = Chat(**any_chat_data)

    assert dict(chat) == any_chat_data


def test_chat_missing_id(any_chat_data: dict):
    any_chat_data.pop('id')

    with pytest.raises(ValidationError):
        Chat(**any_chat_data)


def test_chat_missing_users(any_chat_data: dict):
    any_chat_data.pop('users')

    with pytest.raises(ValidationError):
        Chat(**any_chat_data)


def test_chat_missing_last_message(any_chat_data: dict):
    any_chat_data.pop('last_message')

    with pytest.raises(ValidationError):
        Chat(**any_chat_data)


def test_chat_missing_picture(any_chat_data: dict):
    any_chat_data.pop('picture')

    with pytest.raises(ValidationError):
        Chat(**any_chat_data)


def test_chat_missing_name(any_chat_data: dict):
    any_chat_data.pop('name')

    with pytest.raises(ValidationError):
        Chat(**any_chat_data)
