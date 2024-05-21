from typing import List
from uuid import UUID, uuid4

from fastapi import Depends

from app_musician.app.models.musician_model import Musician
from app_musician.app.repositories.db_musician_repo import MusicianRepo


class MusicianService:
    musician_repo: MusicianRepo

    def __init__(self, musician_repo: MusicianRepo = Depends(MusicianRepo)) -> None:
        self.musician_repo = musician_repo

    def get_all_musicians(self) -> List[Musician]:
        return self.musician_repo.get_all_musicians()


    def create_musician(self, user: dict, genre: str, instrument: str) -> Musician:
        musician = Musician(id=uuid4(), user=user, genre=genre, instrument=instrument)
        return self.musician_repo.create_musician(musician)

    def update_musician(self, musician_id: UUID, user: dict, genre: str, instrument: str) -> Musician:
        musician = Musician(id=musician_id, user=user, genre=genre, instrument=instrument)
        return self.musician_repo.update_musician(musician)