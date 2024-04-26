import pytest
from uuid import uuid4
from pydantic import ValidationError
from app_comment.app.models.comment_model import Comment


@pytest.fixture()
def any_comment_data() -> dict:
    return {
        'id': uuid4(),
        'post_id': uuid4(),
        'user': {},
        'text': 'Comment text',
        'timestamp': '2024-04-26'
    }


def test_comment_creation(any_comment_data: dict):
    comment = Comment(**any_comment_data)

    assert dict(comment) == any_comment_data


def test_comment_missing_post_id(any_comment_data: dict):
    any_comment_data.pop('post_id')

    with pytest.raises(ValidationError):
        Comment(**any_comment_data)


def test_comment_missing_user(any_comment_data: dict):
    any_comment_data.pop('user')

    with pytest.raises(ValidationError):
        Comment(**any_comment_data)


def test_comment_missing_text(any_comment_data: dict):
    any_comment_data.pop('text')

    with pytest.raises(ValidationError):
        Comment(**any_comment_data)


def test_comment_missing_timestamp(any_comment_data: dict):
    any_comment_data.pop('timestamp')

    with pytest.raises(ValidationError):
        Comment(**any_comment_data)
