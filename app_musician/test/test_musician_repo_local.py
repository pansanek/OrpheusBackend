import pytest
from uuid import uuid4
from app_musician.app.models.musician_model import Musician
from app_musician.app.repositories.musician_repo import MusicianRepo


@pytest.fixture(scope='session')
def musician_repo() -> MusicianRepo:
    return MusicianRepo()


@pytest.fixture(scope='session')
def sample_musician() -> Musician:
    return Musician(
        id=uuid4(),
        user={},
        genre="Metalcore",
        instrument="Drums"
    )


def test_create_musician(musician_repo: MusicianRepo, sample_musician: Musician) -> None:
    created_musician = musician_repo.create_musician(sample_musician)
    assert created_musician == sample_musician


def test_create_musician_duplicate(musician_repo: MusicianRepo, sample_musician: Musician) -> None:
    with pytest.raises(KeyError):
        musician_repo.create_musician(sample_musician)


def test_update_musician(musician_repo: MusicianRepo, sample_musician: Musician) -> None:
    sample_musician.genre = "Updated Genre"
    updated_musician = musician_repo.update_musician(sample_musician)
    assert updated_musician.genre == "Updated Genre"
