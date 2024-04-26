import pytest
from uuid import uuid4
from pydantic import ValidationError
from app_location.app.models.location_model import Location


@pytest.fixture()
def any_location_data() -> dict:
    return {
        'id': uuid4(),
        'admin': {},
        'name': 'Location Name',
        'address': '123 Street, City',
        'about': 'About the location',
        'profile_picture': {}  # Assuming empty dictionary for simplicity
    }


def test_location_creation(any_location_data: dict):
    location = Location(**any_location_data)

    assert dict(location) == any_location_data


def test_location_missing_admin(any_location_data: dict):
    any_location_data.pop('admin')

    with pytest.raises(ValidationError):
        Location(**any_location_data)


def test_location_missing_name(any_location_data: dict):
    any_location_data.pop('name')

    with pytest.raises(ValidationError):
        Location(**any_location_data)


def test_location_missing_address(any_location_data: dict):
    any_location_data.pop('address')

    with pytest.raises(ValidationError):
        Location(**any_location_data)


def test_location_missing_about(any_location_data: dict):
    any_location_data.pop('about')

    with pytest.raises(ValidationError):
        Location(**any_location_data)


def test_location_missing_profile_picture(any_location_data: dict):
    any_location_data.pop('profile_picture')

    with pytest.raises(ValidationError):
        Location(**any_location_data)
