from typing import List
from uuid import uuid4

from app_comment.app.models.comment_model import Comment

from app_comment.app.models.photo_url_model import PhotoUrl
from app_comment.app.models.user_model import UserTypes, User
from app_comment.app.models.user_settings_model import UserSettings

from uuid import uuid4

comments = [
    {
        "id": str(uuid4()),
        "post_id": str(uuid4()),
        "user": {
            "id": str(uuid4()),
            "login": "pansanek",
            "name": "Alex",
            "password": "1234",
            "email": "1@gmail.com",
            "about": "Hehe",
            "user_type": "ADMINISTRATOR",
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
            },
        },
        "text": "Hello!",
        "timestamp": "15/2/2024 12:37"
    }
]


class CommentRepo:
    def get_comments(self) -> list[Comment]:
        return comments

    def create_comment(self, comments) -> Comment:
        comments.append(comments)
        return comments

    def get_comments_by_id(self, id):
        for i in comments:
            if i.id == id:
                return i
        raise KeyError
