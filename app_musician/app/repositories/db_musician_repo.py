import traceback
from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.musician_model import Musician
from app.schemas.musician_schema import Musician as DBMusician


class MusicianRepo:
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, musician: DBMusician) -> Musician:
        result = Musician.from_orm(musician)
        return result

    def _map_to_schema(self, musician: Musician) -> DBMusician:
        data = dict(musician)
        result = DBMusician(**data)
        return result

    def create_musician(self, musician: Musician) -> Musician:
        try:
            db_musician = self._map_to_schema(musician)
            self.db.add(db_musician)
            self.db.commit()
            return self._map_to_model(db_musician)
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
            raise e

    def get_all_musicians(self) -> List[Musician]:
        musicians = []
        for m in self.db.query(DBMusician).all():
            musicians.append(self._map_to_model(m))
        return musicians

    def get_musician_by_id(self, musician_id: UUID) -> Musician:
        musician = self.db \
            .query(DBMusician) \
            .filter(DBMusician.id == musician_id) \
            .first()

        if musician is None:
            raise KeyError(f"Musician with id {musician_id} not found.")
        return self._map_to_model(musician)
