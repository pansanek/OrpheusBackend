import traceback
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from app_user.app.database import get_db
from app_post.app.models.post_model import Post
from app_post.app.schemas.post_schema import Post as DBPost

class PostRepo:
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, post: DBPost) -> Post:
        result = Post.from_orm(post)
        return result

    def _map_to_schema(self, post: Post) -> DBPost:
        data = dict(post)
        result = DBPost(**data)
        return result

    def create_post(self, post: Post) -> Post:
        try:
            db_post = self._map_to_schema(post)
            self.db.add(db_post)
            self.db.commit()
            return self._map_to_model(db_post)
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
            raise e

    def get_all_posts(self) -> List[Post]:
        posts = []
        for p in self.db.query(DBPost).all():
            posts.append(self._map_to_model(p))
        return posts

    def get_post_by_id(self, post_id: UUID) -> Post:
        post = self.db \
            .query(DBPost) \
            .filter(DBPost.post_id == post_id) \
            .first()

        if post is None:
            raise KeyError(f"Post with id {post_id} not found.")
        return self._map_to_model(post)
