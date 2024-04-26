import pytest
from uuid import uuid4
from app_post.app.models.post_model import Post, CreatorTypes
from app_post.app.services.post_service import PostService
from unittest.mock import MagicMock


@pytest.fixture(scope='session')
def post_service() -> PostService:
    return PostService(post_repo=MagicMock())


def test_get_all_posts(post_service: PostService) -> None:
    post_service.post_repo.get_posts.return_value = [
        Post(
            id=uuid4(),
            creatorId=uuid4(),
            creatorName="Test Creator",
            creatorPicture={},
            text="Test Post",
            date="2024-04-26",
            likes=[],
            comments=[],
            attachment={},
            creator_type=CreatorTypes.USER
        )
    ]

    posts = post_service.get_all_posts()
    assert len(posts) == 1
    assert isinstance(posts[0], Post)


def test_create_post(post_service: PostService) -> None:
    post_data = {
        "creatorId": uuid4(),
        "creatorName": "Test Creator",
        "creatorPicture": {},
        "text": "Test Post",
        "date": "2024-04-26",
        "likes": [],
        "comments": [],
        "attachment": {},
        "creator_type": CreatorTypes.USER
    }

    post_service.create_post(**post_data)

    post_service.post_repo.create_post.assert_called_once()


def test_update_post(post_service: PostService) -> None:
    post_id = uuid4()
    post_data = {
        "post_id": post_id,
        "creatorId": uuid4(),
        "creatorName": "Test Creator",
        "creatorPicture": {},
        "text": "Test Post",
        "date": "2024-04-26",
        "likes": [],
        "comments": [],
        "attachment": {},
        "creator_type": CreatorTypes.USER
    }

    post_service.update_post(**post_data)

    post_service.post_repo.update_post.assert_called_once_with(
        Post(id=post_id, **post_data)
    )
