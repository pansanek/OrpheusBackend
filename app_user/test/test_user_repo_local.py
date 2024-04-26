import pytest
from uuid import UUID, uuid4
from app_user.app.models.user_model import User, UserTypes
from app_user.app.models.photo_url_model import PhotoUrl
from app_user.app.models.user_settings_model import UserSettings
from app_user.app.repositories.user_repo import UserRepo


@pytest.fixture(scope='session')
def user_repo() -> UserRepo:
    return UserRepo()


@pytest.fixture(scope='session')
def sample_user() -> User:
    return User(
        id=uuid4(),
        login="pansanek",
        name="Alex",
        password="1234",
        email="1@gmail.com",
        about="Hehe",
        user_type=UserTypes.MUSICIAN,
        profile_picture=dict(PhotoUrl(
            id=uuid4(),
            url="https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        )),
        background_picture=dict(PhotoUrl(
            id=uuid4(),
            url="https://sun1-88.userapi.com/impg/SsYpAAyxKG2SXIKXfY8iBvf2BTxZH9XYP2PFmA/lSVeMDXQuDM.jpg?size=1435x1435&quality=95&sign=c2dff2cc261588cb4a712c853c116199&type=album"
        )),
        settings=dict(UserSettings(can_receive_messages_for_new_chats=True,
                                   can_receive_band_invitations=True))
    )




def test_create_user(user_repo: UserRepo, sample_user: User) -> None:
    created_user = user_repo.create_user(sample_user)
    assert created_user == sample_user


def test_create_user_duplicate(user_repo: UserRepo, sample_user: User) -> None:
    with pytest.raises(KeyError):
        user_repo.create_user(sample_user)




def test_update_user(user_repo: UserRepo, sample_user: User) -> None:
    sample_user.name = "Updated Name"
    updated_user = user_repo.update_user(sample_user)
    assert updated_user.name == "Updated Name"
