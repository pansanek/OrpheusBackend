import traceback
from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user_model import Notification
from app.schemas.user_schema import Notification as DBNotification


class NotificationRepo:
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, user: DBNotification) -> Notification:
        result = Notification.from_orm(user)
        return result

    def _map_to_schema(self, user: Notification) -> DBNotification:
        data = dict(user)
        result = DBNotification(**data)
        return result

    def create_user(self, user: Notification) -> Notification:
        try:
            db_user = self._map_to_schema(user)
            self.db.add(db_user)
            self.db.commit()
            return self._map_to_model(db_user)
        except Exception as e:
            traceback.print_exc()
            self.db.rollback()
            raise e

    def get_all_users(self) -> List[Notification]:
        users = []
        for u in self.db.query(DBNotification).all():
            users.append(self._map_to_model(u))
        return users

    def get_user_by_id(self, user_id: UUID) -> Notification:
        user = self.db \
            .query(DBNotification) \
            .filter(DBNotification.id == user_id) \
            .first()

        if user is None:
            raise KeyError(f"Notification with id {user_id} not found.")
        return self._map_to_model(user)

    def authorize(self, login: str, password: str) -> str:
        user = self.db \
            .query(DBNotification) \
            .filter((DBNotification.login == login) & (DBNotification.password == password)) \
            .first()
        if user is None:
            return "NOT OK"
        return str(user.id)