import traceback
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from app_comment.app.database import get_db
from app_comment.app.models.comment_model import Comment
from app_comment.app.schemas.comment_schema import Comment as DBComment

class CommentRepo:
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, comment: DBComment) -> Comment:
        result = Comment.from_orm(comment)
        return result

    def _map_to_schema(self, comment: Comment) -> DBComment:
        data = dict(comment)
        result = DBComment(**data)
        return result

    def create_comment(self, comment: Comment) -> Comment:
        try:
            db_comment = self._map_to_schema(comment)
            self.db.add(db_comment)
            self.db.commit()
            return self._map_to_model(db_comment)
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
            raise e

    def get_all_comments(self) -> List[Comment]:
        comments = []
        for c in self.db.query(DBComment).all():
            comments.append(self._map_to_model(c))
        return comments

    def get_comment_by_id(self, comment_id: UUID) -> Comment:
        comment = self.db \
            .query(DBComment) \
            .filter(DBComment.id == comment_id) \
            .first()

        if comment is None:
            raise KeyError(f"Comment with id {comment_id} not found.")
        return self._map_to_model(comment)
