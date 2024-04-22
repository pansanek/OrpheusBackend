from typing import List
from uuid import uuid4

from app_chat.app.models.chat_model import Chat

from app_chat.app.models.photo_url_model import PhotoUrl
from app_chat.app.models.user_model import UserTypes, User
from app_chat.app.models.user_settings_model import UserSettings

users = [
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
    },
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
]
chats: list[Chat] = [
    Chat(
        id=uuid4(),
        users=users,
        last_message="HELLO",
        picture=dict(PhotoUrl(
            id=uuid4(),
            url="https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        )),
        name = "pansanek"
    )
]


class ChatRepo:
    def get_chats(self) -> list[Chat]:
        return chats

    def create_chat(self, chat) -> Chat:
        chats.append(chat)
        return chat

    def get_chats_by_id(self, id):
        for i in chats:
            if i.id == id:
                return i
        raise KeyError
