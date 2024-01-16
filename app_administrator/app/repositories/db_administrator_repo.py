import traceback
from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.administrator_model import Administrator
from app.schemas.administrator_schema import Administrator as DBAdministrator


class AdministratorRepo:
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, administrator: DBAdministrator) -> Administrator:
        result = Administrator.from_orm(administrator)
        return result

    def _map_to_schema(self, administrator: Administrator) -> DBAdministrator:
        data = dict(administrator)
        result = DBAdministrator(**data)
        return result

    def create_administrator(self, administrator: Administrator) -> Administrator:
        try:
            db_administrator = self._map_to_schema(administrator)
            self.db.add(db_administrator)
            self.db.commit()
            return self._map_to_model(db_administrator)
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
            raise e

    def get_all_administrators(self) -> List[Administrator]:
        administrators = []
        for admin in self.db.query(DBAdministrator).all():
            administrators.append(self._map_to_model(admin))
        return administrators

    def get_administrator_by_id(self, admin_id: UUID) -> Administrator:
        administrator = self.db \
            .query(DBAdministrator) \
            .filter(DBAdministrator.id == admin_id) \
            .first()

        if administrator is None:
            raise KeyError(f"Administrator with id {admin_id} not found.")
        return self._map_to_model(administrator)
