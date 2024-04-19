from typing import List
from uuid import uuid4

from app_post.app.models.post_model import Post, CreatorTypes

from app_post.app.models.photo_url_model import PhotoUrl
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


posts: list[Post] = [
    Post(
        post_id=uuid4(),
        creatorId=uuid4(),
        creatorName="pansanek",
        creatorPicture=dict(PhotoUrl(
            id=uuid4(),
            url="https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        )),
        text="First post",
        date="15/2/2024 12:37",
        likes=[],
        comments=dict(comments),
        attachment=dict(PhotoUrl(
            id=uuid4(),
            url="https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        )),
        creator_type=CreatorTypes.USER,
    )
]


class PostRepo:
    def get_posts(self) -> list[Post]:
        return posts

    def create_post(self, posts) -> Post:
        posts.append(posts)
        return posts

    def get_posts_by_id(self, id):
        for i in posts:
            if i.id == id:
                return i
        raise KeyError
