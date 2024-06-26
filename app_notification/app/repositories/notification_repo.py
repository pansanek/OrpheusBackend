from typing import List
from uuid import uuid4

from app_notification.app.models.notification_model import Notification, NotificationType
from app_notification.app.models.photo_url_model import PhotoUrl
from app_notification.app.models.user_model import User, UserTypes
from app_notification.app.models.user_settings_model import UserSettings

notifications: list[Notification] = [
    Notification(
        id=uuid4(),
        type=NotificationType.LIKE,
        bandItem={},
        contentDescription=" оценил вашу запись от ",
        title="Ваш пост оценили",
        fromUser=dict(User(
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
        )),
        toUser=dict(User(
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
        )),
        date="01-07-2002",
        postItem={}
    )
]


class NotificationRepo:
    def get_notifications(self) -> list[Notification]:
        return notifications

    def create_notification(self, notification) -> Notification:
        notifications.append(notification)
        return notification

    def get_notifications_by_id(self, id):
        for i in notifications:
            if i.id == id:
                return i
        raise KeyError

    def update_notification(self, notification: Notification) -> Notification:
        for index, existing_notification in enumerate(notifications):
            if existing_notification.id == notification.id:
                notifications[index] = notification
                return notification
        raise KeyError("Notification not found")