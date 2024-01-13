from fastapi import Depends
from uuid import UUID, uuid4
from typing import List

from app.models.user_model import User
from app.repositories.db_user_repo import UserRepo


class UserService:
    user_repo: UserRepo

    def __init__(self, user_repo: UserRepo = Depends(UserRepo)) -> None:
        self.user_repo = user_repo

    def get_all_users(self) -> List[User]:
        return self.user_repo.get_all_users()

    def get_user_by_id(self, user_id: UUID) -> User:
        return self.user_repo.get_user_by_id(user_id)

    def create_user(self, login: str, password: str, email: str, about: str, user_type: str) -> User:
        user = User(id=uuid4(), login=login, password=password, email=email, about=about, user_type=user_type)
        return self.user_repo.create_user(user)
