import pytest
from uuid import uuid4
from app_chat.app.models.chat_model import Chat
from app_chat.app.services.chat_service import ChatService
from unittest.mock import MagicMock


@pytest.fixture(scope='session')
def chat_service() -> ChatService:
    return ChatService(chat_repo=MagicMock())


def test_get_all_chats(chat_service: ChatService) -> None:
    chat_service.chat_repo.get_chats.return_value = [
        Chat(
            id=uuid4(),
            users=[],
            last_message="Test message",
            picture={},
            name="Test chat"
        )
    ]

    chats = chat_service.get_all_chats()
    assert len(chats) == 1
    assert isinstance(chats[0], Chat)


def test_create_chat(chat_service: ChatService) -> None:
    chat_data = {
        "users": [],
        "last_message": "Test message",
        "picture": {},
        "name": "Test chat"
    }

    chat_service.create_chat(**chat_data)

    chat_service.chat_repo.create_chat.assert_called_once()


def test_update_chat(chat_service: ChatService) -> None:
    chat_id = uuid4()
    chat_data = {
        "chat_id": chat_id,
        "users": [],
        "last_message": "Test message",
        "picture": {},
        "name": "Test chat"
    }

    chat_service.update_chat(**chat_data)

    chat_service.chat_repo.update_chat.assert_called_once_with(
        Chat(id=chat_id, **chat_data)
    )
