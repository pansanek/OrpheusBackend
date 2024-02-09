import traceback
from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user_model import User
from app.schemas.user_schema import User as DBUser


class UserRepo:
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, user: DBUser) -> User:
        result = User.from_orm(user)
        return result

    def _map_to_schema(self, user: User) -> DBUser:
        data = dict(user)
        result = DBUser(**data)
        return result

    def create_user(self, user: User) -> User:
        try:
            db_user = self._map_to_schema(user)
            self.db.add(db_user)
            self.db.commit()
            return self._map_to_model(db_user)
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
            raise e

    def get_all_users(self) -> List[User]:
        users = []
        for u in self.db.query(DBUser).all():
            users.append(self._map_to_model(u))
        return users

    def get_user_by_id(self, user_id: UUID) -> User:
        user = self.db \
            .query(DBUser) \
            .filter(DBUser.id == user_id) \
            .first()

        if user is None:
            raise KeyError(f"User with id {user_id} not found.")
        return self._map_to_model(user)

    def authorize(self, login: str, password: str) -> str:
        user = self.db \
            .query(DBUser) \
            .filter((DBUser.login == login) & (DBUser.password == password)) \
            .first()
        if user is None:
            return "NOT OK"
        return str(user.id)