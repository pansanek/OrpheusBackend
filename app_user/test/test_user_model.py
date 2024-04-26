import pytest
from uuid import uuid4
from datetime import datetime
from pydantic import ValidationError

from app_user.app.models.user_model import User, UserTypes


@pytest.fixture()
def any_user_data() -> dict:
    return {
        'id': uuid4(),
        'login': 'user_login',
        'name': 'User Name',
        'password': 'password123',
        'email': 'user@example.com',
        'about': 'About the user',
        'user_type': UserTypes.MUSICIAN,
        'profile_picture': {},  # Assuming empty dictionary for simplicity
        'background_picture': {},  # Assuming empty dictionary for simplicity
        'settings': {}  # Assuming empty dictionary for simplicity
    }


def test_user_creation(any_user_data: dict):
    user = User(**any_user_data)

    assert dict(user) == any_user_data


def test_user_missing_login(any_user_data: dict):
    any_user_data.pop('login')

    with pytest.raises(ValidationError):
        User(**any_user_data)


def test_user_missing_name(any_user_data: dict):
    any_user_data.pop('name')

    with pytest.raises(ValidationError):
        User(**any_user_data)


def test_user_invalid_user_type(any_user_data: dict):
    any_user_data['user_type'] = 'invalid_user_type'

    with pytest.raises(ValidationError):
        User(**any_user_data)
