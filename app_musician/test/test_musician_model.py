import pytest
from uuid import uuid4
from pydantic import ValidationError
from app_musician.app.models.musician_model import Musician, GenreTypes, InstrumentTypes


@pytest.fixture()
def any_musician_data() -> dict:
    return {
        'id': uuid4(),
        'user': {},
        'genre': GenreTypes.ROCK,
        'instrument': InstrumentTypes.GUITAR
    }


def test_musician_creation(any_musician_data: dict):
    musician = Musician(**any_musician_data)

    assert dict(musician) == any_musician_data


def test_musician_missing_genre(any_musician_data: dict):
    any_musician_data.pop('genre')

    with pytest.raises(ValidationError):
        Musician(**any_musician_data)


def test_musician_missing_instrument(any_musician_data: dict):
    any_musician_data.pop('instrument')

    with pytest.raises(ValidationError):
        Musician(**any_musician_data)


def test_musician_invalid_genre(any_musician_data: dict):
    any_musician_data['genre'] = 'invalid_genre_type'

    with pytest.raises(ValidationError):
        Musician(**any_musician_data)


def test_musician_invalid_instrument(any_musician_data: dict):
    any_musician_data['instrument'] = 'invalid_instrument_type'

    with pytest.raises(ValidationError):
        Musician(**any_musician_data)
