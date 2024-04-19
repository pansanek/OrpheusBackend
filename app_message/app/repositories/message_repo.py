from typing import List
from uuid import uuid4


from app_message.app.models.message_model import Message

from app_message.app.models.photo_url_model import PhotoUrl
from app_message.app.models.user_model import UserTypes, User
from app_message.app.models.user_settings_model import UserSettings

messages: list[Message] = [
    Message(
        id=uuid4(),
        from_user=dict(User(
            id=uuid4(),
            login="pansanek",
            name="Alex",
            password="1234",
            email="1@gmail.com",
            about="Hehe",
            user_type=UserTypes.MUSICIAN,
            profile_picture=dict(PhotoUrl(
                id=uuid4(),
                url="https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
            )),
            background_picture=dict(PhotoUrl(
                id=uuid4(),
                url="https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
            )),
            settings=dict(UserSettings(can_receive_messages_for_new_chats=True,
                                  can_receive_band_invitations=True)),
        )),
        timestamp="15/2/2024 12:37",
        content="Hello!"
    )
]


class MessageRepo:
    def get_messages(self) -> list[Message]:
        return messages

    def create_message(self, messages) -> Message:
        messages.append(messages)
        return messages

    def get_messages_by_id(self, id):
        for i in messages:
            if i.id == id:
                return i
        raise KeyError
