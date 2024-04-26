import pytest
from uuid import uuid4
from app_message.app.models.message_model import Message
from app_message.app.repositories.message_repo import MessageRepo


@pytest.fixture(scope='session')
def message_repo() -> MessageRepo:
    return MessageRepo()


@pytest.fixture(scope='session')
def sample_message() -> Message:
    return Message(
        id=uuid4(),
        chat_id=uuid4(),
        from_user={},
        timestamp="2024-04-26",
        content="Hello!"
    )


def test_create_message(message_repo: MessageRepo, sample_message: Message) -> None:
    created_message = message_repo.create_message(sample_message)
    assert created_message == sample_message


def test_create_message_duplicate(message_repo: MessageRepo, sample_message: Message) -> None:
    with pytest.raises(KeyError):
        message_repo.create_message(sample_message)


def test_update_message(message_repo: MessageRepo, sample_message: Message) -> None:
    sample_message.content = "Updated content"
    updated_message = message_repo.update_message(sample_message)
    assert updated_message.content == "Updated content"
