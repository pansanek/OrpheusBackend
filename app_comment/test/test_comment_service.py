import pytest
from uuid import uuid4
from app_comment.app.models.comment_model import Comment
from app_comment.app.services.comment_service import CommentService
from unittest.mock import MagicMock


@pytest.fixture(scope='session')
def comment_service() -> CommentService:
    return CommentService(comment_repo=MagicMock())


def test_get_all_comments(comment_service: CommentService) -> None:
    comment_service.comment_repo.get_comments.return_value = [
        Comment(
            id=uuid4(),
            post_id=uuid4(),
            user={},
            text="Test comment",
            timestamp="2024-04-26"
        )
    ]

    comments = comment_service.get_all_comments()
    assert len(comments) == 1
    assert isinstance(comments[0], Comment)


def test_create_comment(comment_service: CommentService) -> None:
    comment_data = {
        "post_id": uuid4(),
        "user": {},
        "text": "Test comment",
        "timestamp": "2024-04-26"
    }

    comment_service.create_comment(**comment_data)

    comment_service.comment_repo.create_comment.assert_called_once()


def test_update_comment(comment_service: CommentService) -> None:
    comment_id = uuid4()
    comment_data = {
        "comment_id": comment_id,
        "post_id": uuid4(),
        "user": {},
        "text": "Test comment",
        "timestamp": "2024-04-26"
    }

    comment_service.update_comment(**comment_data)

    comment_service.comment_repo.update_comment.assert_called_once_with(
        Comment(id=comment_id, **comment_data)
    )
