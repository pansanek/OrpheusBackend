import pytest
from uuid import uuid4
from app_location.app.models.location_model import Location
from app_location.app.services.location_service import LocationService
from unittest.mock import MagicMock


@pytest.fixture(scope='session')
def location_service() -> LocationService:
    return LocationService(location_repo=MagicMock())


def test_get_all_locations(location_service: LocationService) -> None:
    location_service.location_repo.get_locations.return_value = [
        Location(
            id=uuid4(),
            admin={},
            name="Test Location",
            address="Test Address",
            about="Test About",
            profile_picture={}
        )
    ]

    locations = location_service.get_all_locations()
    assert len(locations) == 1
    assert isinstance(locations[0], Location)


def test_create_location(location_service: LocationService) -> None:
    location_data = {
        "admin": {},
        "name": "Test Location",
        "address": "Test Address",
        "about": "Test About",
        "profile_picture": {}
    }

    location_service.create_location(**location_data)

    location_service.location_repo.create_location.assert_called_once()


def test_update_location(location_service: LocationService) -> None:
    location_id = uuid4()
    location_data = {
        "location_id": location_id,
        "admin": {},
        "name": "Test Location",
        "address": "Test Address",
        "about": "Test About",
        "profile_picture": {}
    }

    location_service.update_location(**location_data)

    location_service.location_repo.update_location.assert_called_once_with(
        Location(id=location_id, **location_data)
    )
