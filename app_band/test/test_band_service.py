import pytest
from uuid import uuid4
from app_band.app.models.band_model import Band
from app_band.app.services.band_service import BandService
from unittest.mock import MagicMock
from app_band.app.models.genre_types import GenreTypes


@pytest.fixture(scope='session')
def band_service() -> BandService:
    return BandService(band_repo=MagicMock())


def test_get_all_bands(band_service: BandService) -> None:
    band_service.band_repo.get_bands.return_value = [
        Band(
            id=uuid4(),
            name="Test Band",
            members=[],
            genre=GenreTypes.ROCK,
            photo={}
        )
    ]

    bands = band_service.get_all_bands()
    assert len(bands) == 1
    assert isinstance(bands[0], Band)


def test_create_band(band_service: BandService) -> None:
    band_data = {
        "name": "Test Band",
        "members": [],
        "genre": GenreTypes.ROCK,
        "photo": {}
    }

    band_service.create_band(**band_data)

    band_service.band_repo.create_band.assert_called_once()


def test_update_band(band_service: BandService) -> None:
    band_id = uuid4()
    band_data = {
        "band_id": band_id,
        "name": "Test Band",
        "members": [],
        "genre": GenreTypes.ROCK,
        "photo": {}
    }

    band_service.update_band(**band_data)

    band_service.band_repo.update_band.assert_called_once_with(
        Band(id=band_id, **band_data)
    )
