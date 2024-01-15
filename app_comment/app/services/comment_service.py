from typing import List
from uuid import UUID, uuid4
from datetime import datetime
from fastapi import Depends

from app_comment.app.models.comment_model import Comment
from app_comment.app.repositories.db_comment_repo import CommentRepo


class CommentService:
    comment_repo: CommentRepo

    def __init__(self, comment_repo: CommentRepo = Depends(CommentRepo)) -> None:
        self.comment_repo = comment_repo

    def get_all_comments(self) -> List[Comment]:
        return self.comment_repo.get_all_comments()

    def get_comment_by_id(self, comment_id: UUID) -> Comment:
        return self.comment_repo.get_comment_by_id(comment_id)

    def get_comments_by_post_id(self, post_id: UUID) -> List[Comment]:
        return self.comment_repo.get_comments_by_post_id(post_id)

    def create_comment(self, post_id: UUID, user_id: UUID, text: str, timestamp: datetime) -> Comment:
        comment = Comment(id=uuid4(), post_id=post_id, user_id=user_id, text=text, timestamp=timestamp)
        return self.comment_repo.create_comment(comment)
