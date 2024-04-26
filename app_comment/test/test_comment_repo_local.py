import pytest
from uuid import uuid4
from app_comment.app.models.comment_model import Comment
from app_comment.app.repositories.comment_repo import CommentRepo


@pytest.fixture(scope='session')
def comment_repo() -> CommentRepo:
    return CommentRepo()


@pytest.fixture(scope='session')
def sample_comment() -> Comment:
    return Comment(
        id=str(uuid4()),
        post_id=str(uuid4()),
        user={
            "id": str(uuid4()),
            "login": "pansanek",
            "name": "Alex",
            "password": "1234",
            "email": "1@gmail.com",
            "about": "Hehe",
            "user_type": "ADMINISTRATOR",
            "profile_picture": {
                "id": str(uuid4()),
                "url": "https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
            },
            "background_picture": {
                "id": str(uuid4()),
                "url": "https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
            },
            "settings": {
                "can_receive_messages_for_new_chats": True,
                "can_receive_band_invitations": True
            },
        },
        text="Hello!",
        timestamp="15/2/2024 12:37"
    )


def test_create_comment(comment_repo: CommentRepo, sample_comment: Comment) -> None:
    created_comment = comment_repo.create_comment(sample_comment)
    assert created_comment == sample_comment


def test_create_comment_duplicate(comment_repo: CommentRepo, sample_comment: Comment) -> None:
    with pytest.raises(KeyError):
        comment_repo.create_comment(sample_comment)


def test_update_comment(comment_repo: CommentRepo, sample_comment: Comment) -> None:
    sample_comment.text = "Updated comment text"
    updated_comment = comment_repo.update_comment(sample_comment)
    assert updated_comment.text == "Updated comment text"
