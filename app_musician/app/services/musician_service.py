from typing import List
from uuid import UUID, uuid4

from fastapi import Depends

from app.models.musician_model import Musician
from app.repositories.db_musician_repo import MusicianRepo


class MusicianService:
    musician_repo: MusicianRepo

    def __init__(self, musician_repo: MusicianRepo = Depends(MusicianRepo)) -> None:
        self.musician_repo = musician_repo

    def get_all_musicians(self) -> List[Musician]:
        return self.musician_repo.get_all_musicians()

    def get_musician_by_id(self, musician_id: UUID) -> Musician:
        return self.musician_repo.get_musician_by_id(musician_id)

    def create_musician(self, user_id: UUID, genre: str, instrument: str) -> Musician:
        musician = Musician(id=uuid4(), user_id=user_id, genre=genre, instrument=instrument)
        return self.musician_repo.create_musician(musician)
