import pytest
from uuid import uuid4
from app_message.app.models.message_model import Message
from app_message.app.services.message_service import MessageService
from unittest.mock import MagicMock


@pytest.fixture(scope='session')
def message_service() -> MessageService:
    return MessageService(message_repo=MagicMock())


def test_get_all_messages(message_service: MessageService) -> None:
    message_service.message_repo.get_messages.return_value = [
        Message(
            id=uuid4(),
            chat_id=uuid4(),
            from_user={},
            timestamp="2024-04-26",
            content="Hello!"
        )
    ]

    messages = message_service.get_all_messages()
    assert len(messages) == 1
    assert isinstance(messages[0], Message)


def test_create_message(message_service: MessageService) -> None:
    message_data = {
        "chat_id": uuid4(),
        "from_user": {},
        "timestamp": "2024-04-26",
        "content": "Hello!"
    }

    message_service.create_message(**message_data)

    message_service.message_repo.create_message.assert_called_once()


def test_update_message(message_service: MessageService) -> None:
    message_id = uuid4()
    message_data = {
        "message_id": message_id,
        "chat_id": uuid4(),
        "from_user": {},
        "timestamp": "2024-04-26",
        "content": "Hello!"
    }

    message_service.update_message(**message_data)

    message_service.message_repo.update_message.assert_called_once_with(
        Message(id=message_id, **message_data)
    )
