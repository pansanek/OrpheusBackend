import pytest
from uuid import uuid4
from app_musician.app.models.musician_model import Musician
from app_musician.app.services.musician_service import MusicianService
from unittest.mock import MagicMock


@pytest.fixture(scope='session')
def musician_service() -> MusicianService:
    return MusicianService(musician_repo=MagicMock())


def test_get_all_musicians(musician_service: MusicianService) -> None:
    musician_service.musician_repo.get_musicians.return_value = [
        Musician(
            id=uuid4(),
            user={},
            genre="Metalcore",
            instrument="Drums"
        )
    ]

    musicians = musician_service.get_all_musicians()
    assert len(musicians) == 1
    assert isinstance(musicians[0], Musician)


def test_create_musician(musician_service: MusicianService) -> None:
    musician_data = {
        "user": {},
        "genre": "Metalcore",
        "instrument": "Drums"
    }

    musician_service.create_musician(**musician_data)

    musician_service.musician_repo.create_musician.assert_called_once()


def test_update_musician(musician_service: MusicianService) -> None:
    musician_id = uuid4()
    musician_data = {
        "musician_id": musician_id,
        "user": {},
        "genre": "Metalcore",
        "instrument": "Drums"
    }

    musician_service.update_musician(**musician_data)

    musician_service.musician_repo.update_musician.assert_called_once_with(
        Musician(id=musician_id, **musician_data)
    )
