
import pytest
from uuid import uuid4
from pydantic import ValidationError
from app_post.app.models.post_model import Post, CreatorTypes


@pytest.fixture()
def any_post_data() -> dict:
    return {
        'post_id': uuid4(),
        'creatorId': uuid4(),
        'creatorName': 'John Doe',
        'creatorPicture': {},
        'text': 'Sample post text',
        'date': '2024-04-26',
        'likes': [],
        'comments': [],
        'attachment': {},
        'creator_type': CreatorTypes.USER
    }


def test_post_creation(any_post_data: dict):
    post = Post(**any_post_data)

    assert dict(post) == any_post_data


def test_post_missing_creatorId(any_post_data: dict):
    any_post_data.pop('creatorId')

    with pytest.raises(ValidationError):
        Post(**any_post_data)


def test_post_missing_text(any_post_data: dict):
    any_post_data.pop('text')

    with pytest.raises(ValidationError):
        Post(**any_post_data)


def test_post_invalid_creator_type(any_post_data: dict):
    any_post_data['creator_type'] = 'invalid_creator_type'

    with pytest.raises(ValidationError):
        Post(**any_post_data)
