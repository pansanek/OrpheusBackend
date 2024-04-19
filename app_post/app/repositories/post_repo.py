from typing import List
from uuid import uuid4

from app_post.app.models.post_model import Post, CreatorTypes

from app_post.app.models.photo_url_model import PhotoUrl

posts: list[Post] = [
    Post(
        post_id=uuid4(),
        creatorId=uuid4(),
        creatorName="pansanek",
        creatorPicture=PhotoUrl(
            id=uuid4(),
            url="https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        ),
        text="First post",
        date="15/2/2024 12:37",
        likes=[],
        comments=[],
        attachment={},
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
