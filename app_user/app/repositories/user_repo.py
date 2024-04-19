from typing import List
from uuid import uuid4

from app.models.User import User

from app_user.app.models.photo_url_model import PhotoUrl
from app_user.app.models.user_model import UserTypes
from app_user.app.models.user_settings_model import UserSettings

users: list[User] = [
    User(
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
                                   can_receive_band_invitations=True))
    )
]


class UserRepo:
    def get_users(self) -> list[User]:
        return users

    def create_user(self, users) -> User:
        users.append(users)
        return users

    def get_users_by_id(self, id):
        for i in users:
            if i.id == id:
                return i
        raise KeyError
