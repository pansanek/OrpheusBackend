import pytest
from uuid import uuid4
from app_chat.app.models.chat_model import Chat
from app_chat.app.repositories.chat_repo import ChatRepo


@pytest.fixture(scope='session')
def chat_repo() -> ChatRepo:
    return ChatRepo()


@pytest.fixture(scope='session')
def sample_chat() -> Chat:
    return Chat(
        id=uuid4(),
        users=[
            {
                "id": str(uuid4()),
                "login": "pansanek",
                "name": "Alex",
                "password": "1234",
                "email": "1@gmail.com",
                "about": "Hehe",
                "user_type": "MUSICIAN",
                "profile_picture": {
                    "id": str(uuid4()),
                    "url": "https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
                },
                "background_picture": {
                    "id": str(uuid4()),
                    "url": "https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
                },
                "settings": {
                    "can_receive_messages_for_new_chats": True,
                    "can_receive_band_invitations": True
                }
            }
        ],
        last_message="HELLO",
        picture={
            "id": str(uuid4()),
            "url": "https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        },
        name="pansanek"
    )


def test_create_chat(chat_repo: ChatRepo, sample_chat: Chat) -> None:
    created_chat = chat_repo.create_chat(sample_chat)
    assert created_chat == sample_chat


def test_create_chat_duplicate(chat_repo: ChatRepo, sample_chat: Chat) -> None:
    with pytest.raises(KeyError):
        chat_repo.create_chat(sample_chat)


def test_update_chat(chat_repo: ChatRepo, sample_chat: Chat) -> None:
    sample_chat.name = "Updated chat name"
    updated_chat = chat_repo.update_chat(sample_chat)
    assert updated_chat.name == "Updated chat name"
