import pytest
from uuid import UUID, uuid4
from app_user.app.models.user_model import User, UserTypes
from app_user.app.services.user_service import UserService
from unittest.mock import MagicMock


@pytest.fixture(scope='session')
def user_service() -> UserService:
    return UserService(user_repo=MagicMock())


def test_get_all_users(user_service: UserService) -> None:
    user_service.user_repo.get_users.return_value = [User(id=uuid4(), login="test_login", name="Test User", password="password", email="test@example.com", about="Test about", user_type=UserTypes.MUSICIAN, profile_picture={}, background_picture={}, settings={})]

    users = user_service.get_all_users()
    assert len(users) == 1
    assert isinstance(users[0], User)


def test_create_user(user_service: UserService) -> None:
    user_data = {
        "login": "test_login",
        "name": "Test User",
        "password": "password",
        "email": "test@example.com",
        "about": "Test about",
        "user_type": "Musician",
        "profile_picture": {},
        "background_picture": {},
        "settings": {}
    }

    user_service.create_user(**user_data)

    user_service.user_repo.create_user.assert_called_once()


def test_update_user(user_service: UserService) -> None:
    user_id = uuid4()
    user_data = {
        "user_id": user_id,
        "login": "test_login",
        "name": "Test User",
        "password": "password",
        "email": "test@example.com",
        "about": "Test about",
        "user_type": "Musician",
        "profile_picture": {},
        "background_picture": {},
        "settings": {}
    }

    user_service.update_user(**user_data)

    user_service.user_repo.update_user.assert_called_once_with(User(id=user_id, **user_data))
