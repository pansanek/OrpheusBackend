import pytest
from uuid import uuid4
from app_band.app.models.band_model import Band
from app_band.app.models.genre_types import GenreTypes
from pydantic import ValidationError


@pytest.fixture()
def any_band_data() -> dict:
    return {
        'id': uuid4(),
        'name': 'Band name',
        'members': [{}],
        'genre': GenreTypes.ROCK,
        'photo': {}
    }


def test_band_creation(any_band_data: dict):
    band = Band(**any_band_data)

    assert dict(band) == any_band_data


def test_band_missing_id(any_band_data: dict):
    any_band_data.pop('id')

    with pytest.raises(ValidationError):
        Band(**any_band_data)


def test_band_missing_name(any_band_data: dict):
    any_band_data.pop('name')

    with pytest.raises(ValidationError):
        Band(**any_band_data)


def test_band_missing_members(any_band_data: dict):
    any_band_data.pop('members')

    with pytest.raises(ValidationError):
        Band(**any_band_data)


def test_band_missing_genre(any_band_data: dict):
    any_band_data.pop('genre')

    with pytest.raises(ValidationError):
        Band(**any_band_data)


def test_band_missing_photo(any_band_data: dict):
    any_band_data.pop('photo')

    with pytest.raises(ValidationError):
        Band(**any_band_data)
