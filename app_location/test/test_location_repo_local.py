import pytest
from uuid import uuid4
from app_location.app.models.location_model import Location
from app_location.app.repositories.location_repo import LocationRepo


@pytest.fixture(scope='session')
def location_repo() -> LocationRepo:
    return LocationRepo()


@pytest.fixture(scope='session')
def sample_location() -> Location:
    return Location(
        id=uuid4(),
        admin=dict(
            id=uuid4(),
            login="pansanek",
            name="Alex",
            password="1234",
            email="1@gmail.com",
            about="Hehe",
            user_type="MUSICIAN",
            profile_picture={},
            background_picture={},
            settings={}
        ),
        address="DOM 4",
        name="Hello!",
        about="ABOUT",
        profile_picture={}
    )


def test_create_location(location_repo: LocationRepo, sample_location: Location) -> None:
    created_location = location_repo.create_location(sample_location)
    assert created_location == sample_location


def test_create_location_duplicate(location_repo: LocationRepo, sample_location: Location) -> None:
    with pytest.raises(KeyError):
        location_repo.create_location(sample_location)


def test_update_location(location_repo: LocationRepo, sample_location: Location) -> None:
    sample_location.name = "Updated Location Name"
    updated_location = location_repo.update_location(sample_location)
    assert updated_location.name == "Updated Location Name"
