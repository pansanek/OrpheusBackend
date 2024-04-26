import pytest
from uuid import uuid4
from app_post.app.models.post_model import Post, CreatorTypes
from app_post.app.repositories.post_repo import PostRepo
from app_post.app.models.photo_url_model import PhotoUrl


@pytest.fixture(scope='session')
def post_repo() -> PostRepo:
    return PostRepo()


@pytest.fixture(scope='session')
def sample_post() -> Post:
    return Post(
        post_id=uuid4(),
        creatorId=uuid4(),
        creatorName="pansanek",
        creatorPicture=dict(PhotoUrl(
            id=uuid4(),
            url="https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        )),
        text="First post",
        date="15/2/2024 12:37",
        likes=[],
        comments=[],
        attachment=dict(PhotoUrl(
            id=uuid4(),
            url="https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        )),
        creator_type=CreatorTypes.USER,
    )


def test_create_post(post_repo: PostRepo, sample_post: Post) -> None:
    created_post = post_repo.create_post(sample_post)
    assert created_post == sample_post


def test_create_post_duplicate(post_repo: PostRepo, sample_post: Post) -> None:
    with pytest.raises(KeyError):
        post_repo.create_post(sample_post)


def test_update_post(post_repo: PostRepo, sample_post: Post) -> None:
    sample_post.text = "Updated post text"
    updated_post = post_repo.update_post(sample_post)
    assert updated_post.text == "Updated post text"
