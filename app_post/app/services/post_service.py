from datetime import datetime
from typing import List
from uuid import UUID, uuid4

from fastapi import Depends

from app.models.post_model import Post
from app.repositories.db_post_repo import PostRepo


class PostService:
    post_repo: PostRepo

    def __init__(self, post_repo: PostRepo = Depends(PostRepo)) -> None:
        self.post_repo = post_repo

    def get_all_posts(self) -> List[Post]:
        return self.post_repo.get_all_posts()

    def get_post_by_id(self, post_id: UUID) -> Post:
        return self.post_repo.get_post_by_id(post_id)

    def create_post(self, creator_id: UUID, caption: str, creator_type: str) -> Post:
        post = Post(post_id=uuid4(), creator_id=creator_id, caption=caption, timestamp=datetime.utcnow(), likes=[],
                    comments=[], attachment=[], creator_type=creator_type, views=0)
        return self.post_repo.create_post(post)
