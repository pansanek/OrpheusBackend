from datetime import datetime
from typing import List
from uuid import UUID, uuid4

from fastapi import Depends

from app_post.app.models.post_model import Post
from app_post.app.repositories.post_repo import PostRepo

from app_post.app.models.post_model import CreatorTypes


class PostService:
    post_repo: PostRepo

    def __init__(self, post_repo: PostRepo = Depends(PostRepo)) -> None:
        self.post_repo = post_repo

    def get_all_posts(self) -> List[Post]:
        return self.post_repo.get_posts()

    def get_post_by_id(self, post_id: UUID) -> Post:
        return self.post_repo.get_post_by_id(post_id)

    def create_post(self, creatorId: UUID,
                    creatorName: str,
                    creatorPicture: dict,
                    text: str,
                    date: str,
                    likes: List[dict],
                    comments: List[dict],
                    attachment: dict,
                    creator_type: CreatorTypes) -> Post:
        post = Post(post_id=uuid4(), creatorId=creatorId, text=text, date=date, likes=likes,
                    comments=comments, attachment=attachment, creator_type=creator_type, views=0,
                    creatorName=creatorName, creatorPicture=creatorPicture)
        return self.post_repo.create_post(post)

    def update_post(self, post_id: UUID, creatorId: UUID,
                    creatorName: str,
                    creatorPicture: dict,
                    text: str,
                    date: str,
                    likes: List[dict],
                    comments: List[dict],
                    attachment: dict,
                    creator_type: CreatorTypes) -> Post:
        post = Post(id=post_id, creatorId=creatorId, text=text, date=date, likes=likes,
                    comments=comments, attachment=attachment, creator_type=creator_type, views=0,
                    creatorName=creatorName, creatorPicture=creatorPicture)
        return self.post_repo.update_post(post)
